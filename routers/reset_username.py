##############################
#   IMPORTS
#   Library imports
from bottle import template, get, post, request, response
import os
import bcrypt
import uuid
import logging
from datetime import datetime, timedelta
from dotenv import load_dotenv
from email.mime.text import MIMEText
import smtplib
from urllib.parse import urljoin

#   Local application imports
from common.colored_logging import setup_logger
import common.content as content
import master

# Load environment variables
load_dotenv('.env')

##############################
#   COLORED LOGGING
try:
    logger = setup_logger(__name__, level=logging.INFO)
    logger.setLevel(logging.INFO)
    logger.success("Logging imported successfully.")
except Exception as e:
    logger.error(f"Error importing logging: {e}")
finally:
    logger.info("Logging import process completed.")

##############################
#   CONTENT VARIABLES
try:
    # Global
    global_content = content.global_content
    # Content for this page
    login_content = content.login_content
    logger.success("Content imported successfully.")
except Exception as e:
    logger.error(f"Error importing content: {e}")
finally:
    logger.info("Content import process completed.")


##############################
#   RESET USERNAME - GET TEMPLATE
@get("/reset_username")
def reset_username():
    page_name = "reset_username"

    try:
        # Securely retrieve user cookie
        user_cookie = request.get_cookie("user", secret=os.getenv('MY_SECRET'))

        # Validate cookie, then fetch user details from db
        if user_cookie and isinstance(user_cookie, dict):
            db = master.db()
            username = user_cookie.get('username')
            user = db.execute("SELECT * FROM users WHERE username = ? LIMIT 1", (username,)).fetchone()
            logger.success(f"Valid user cookie found for /{page_name}, retrieved data from database")
            logger.info(f"Logged in user: {username}")
        else:
            user = username = None
            logger.warning(f"No valid user cookie found for /{page_name}, perhaps user is not logged in yet")

        # Show template
        logger.success(f"Successfully showing template for {page_name}")
        return template(page_name,
                        title="Anmod om Nulstilling af Brugernavn",
                        global_content=global_content,
                        user=user,
                        username=username)

    except Exception as e:
        if "db" in locals():
            db.rollback()
            logger.info("Database transaction rolled back due to exception")
        logger.error(f"Error during request for /{page_name}: {e}")
        raise

    finally:
        if "db" in locals():
            db.close()
            logger.info("Database connection closed")
        logger.info(f"Completed request for /{page_name}")

#   REQUEST RESET USERNAME - SEND EMAIL TO USER
@post("/request_reset_username")
def request_reset_username():
    try:
        email = request.forms.get('email')

        if not email:
            logger.warning("Email er påkrævet")
            response.status = 400
            return {"error": "Email er påkrævet"}

        db = master.db()
        cursor = db.cursor()

        # Generate a new reset token
        token = str(uuid.uuid4())
        expiry_time = datetime.now() + timedelta(hours=1) 

        # Update user record with reset token and expiry time
        cursor.execute("""
            UPDATE users 
            SET reset_token = ?, reset_token_expiry = ?
            WHERE email = ?
        """, (token, expiry_time, email))
        db.commit()

        # Send reset username email with the token
        send_reset_username_email(email, token)

        logger.success("Reset link sent to email")
        return {"message": "Et nulstillingslink er blevet sendt til din email!"}
 
    except Exception as e:
        if "db" in locals():
            db.rollback()
            logger.info("Database transaction rolled back due to exception")
        logger.error(f"Error during request for /request_reset_username: {e}")
        response.status = 500
        return {"error": "Der opstod en fejl"}

    finally:
        if "db" in locals():
            db.close()
            logger.info("Database connection closed")


##############################
#   GET UPDATE USERNAME FORMULAR
@get("/get_reset_username")
def get_reset_username():
    page_name = "new_username"

    try:
        # Securely retrieve user cookie
        user_cookie = request.get_cookie("user", secret=os.getenv('MY_SECRET'))

        # Validate cookie, then fetch user details from db
        if user_cookie and isinstance(user_cookie, dict):
            db = master.db()
            username = user_cookie.get('username')
            user = db.execute("SELECT * FROM users WHERE username = ? LIMIT 1", (username,)).fetchone()
            logger.success(f"Valid user cookie found for /{page_name}, retrieved data from database")
            logger.info(f"Logged in user: {username}")
        else:
            user = username = None
            logger.warning(f"No valid user cookie found for /{page_name}, perhaps user is not logged in yet")

        # Retrieve the token from query parameters
        token = request.query.get('token')

        if not token:
            logger.warning("Ingen token angivet")
            return template('error', error="Ingen token angivet")

        # Show template
        logger.success(f"Successfully showing template for {page_name}")
        return template('new_username',
                        title="UNID Studio - Nyt Brugernavn",
                        global_content=global_content,
                        user=user,
                        username=username,
                        token=token)

    except Exception as e:
        if "db" in locals():
            db.rollback()
            logger.info("Database transaction rolled back due to exception")
        logger.error(f"Error during request for /{page_name}: {e}")
        raise

    finally:
        if "db" in locals():
            db.close()
            logger.info("Database connection closed")
        logger.info(f"Completed request for /{page_name}")

##############################
#   UPDATES USERNAME
@post("/update_username")
def update_username_post():
    try:
        token = request.forms.get('token')
        new_username = request.forms.get('new_username')

        if not token or not new_username:
            logger.warning("Token og nyt brugernavn er påkrævet")
            response.status = 400
            return {"error": "Token og nyt brugernavn er påkrævet"}

        db = master.db()
        cursor = db.cursor()

        # Check if the token is valid and not expired
        cursor.execute("""
            SELECT * FROM users 
            WHERE reset_token = ? 
            AND reset_token_expiry > datetime('now')
        """, (token,))
        user = cursor.fetchone()

        if not user:
            logger.warning("Ugyldigt eller udløbet token")
            response.status = 400
            return {"error": "Ugyldigt eller udløbet token"}

        # Update the user's username and clear the reset token
        cursor.execute("""
            UPDATE users 
            SET username = ?, reset_token = NULL, reset_token_expiry = NULL 
            WHERE reset_token = ?
        """, (new_username, token))
        db.commit()

        logger.success("Brugernavnet er blevet opdateret")
        return {"message": "Dit brugernavn er blevet opdateret!"}

    except Exception as e:
        if "db" in locals():
            db.rollback()
            logger.info("Database transaction rolled back due to exception")
        logger.error(f"Error during request for /update_username: {e}")
        response.status = 500
        return {"error": "Der opstod en fejl. Prøv igen."}

    finally:
        if "db" in locals():
            db.close()
            logger.info("Database connection closed")





def send_reset_username_email(email, token):
    smtp_server = 'smtp.simply.com'
    smtp_port = 587
    smtp_user = os.getenv('EMAIL')
    smtp_password = os.getenv('EMAIL_PASSWORD')
    from_email = 'kontakt@unidstudio.dk'
    reset_link = urljoin('http://127.0.0.1:2500/', f"/get_reset_username?token={token}")

    subject = "Nulstil dit brugernavn"
    body = f"""
    Hej,

    Klik på følgende link for at nulstille dit brugernavn:
    {reset_link}

    Hvis du ikke har anmodet om at nulstille dit brugernavn, kan du ignorere denne e-mail.

    Med venlig hilsen,
    UNID Studio
    """

    msg = MIMEText(body, 'plain')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(from_email, email, msg.as_string())
    except Exception as e:
        logger.error(f"Failed to send username reset email: {e}")



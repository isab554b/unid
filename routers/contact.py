##############################
#   IMPORTS
#   Library imports
from bottle import template, get, request, post
import logging
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



#   Local application imports
from common.colored_logging import setup_logger
import common.content as content
import master
from dotenv import load_dotenv


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
    contact_content = content.contact_content
    logger.success("Content imported successfully.")
except Exception as e:
    logger.error(f"Error importing content: {e}")
finally:
    logger.info("Content import process completed.")


##############################
#   CONTACT
@get("/contact")
def contact():

    page_name = "contact"

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

        # Handle scenarios where no valid cookie is found (e.g., user not logged in)
        else:
            user = username = None
            logger.warning(f"No valid user cookie found for /{page_name}, perhaps user is not logged in yet")

        # Show template
        logger.success(f"Succesfully showing template for {page_name}")
        return template(page_name,
                        title="UNID Studio - Kontakt",
                        # A-Z
                        contact_content=contact_content,
                        global_content=global_content,
                        user=user,
                        username=username
                        )

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
#   CONTACT FORMULAR - SEND EMAIL
def send_email(subject, body, to_email):
    load_dotenv()
    from_email = os.getenv('EMAIL')
    from_password = os.getenv('EMAIL_PASSWORD')

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.simply.com', 587)  # Erstat med SMTP-serveradresse og port for SimplyMail
        server.starttls()  # Start TLS for sikkerhed
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error: {e}")

@post('/send-email')
def send_email_handler():

    function_name = "send_email_handler"

    full_name = request.forms.get('full_name')
    email = request.forms.get('email')
    message = request.forms.get('message')

    subject = f"Kontakformular - {full_name}"
    body = f"Navn: {full_name}\nEmail: {email}\n\nBesked:\n{message}"

    send_email(subject, body, 'kontakt@unidstudio.dk')

    logger.success(f"{function_name} successful")
    return {"info": "Beskeden er blevet sendt!"}




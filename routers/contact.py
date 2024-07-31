##############################
#   IMPORTS
#   Library imports
from bottle import template, get, request, post
import logging
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email_validator import validate_email, EmailNotValidError

#   Local application imports
from common.colored_logging import setup_logger
import common.content as content
import master
from app import app_config


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

@post('/send')
def send_email():
    name = request.forms.get('name')
    email = request.forms.get('email')
    message = request.forms.get('message')

    # Valider e-mail
    try:
        validate_email(email)
    except EmailNotValidError:
        return template('error', message="Invalid email address.")

    # Send e-mail
    try:
        msg = MIMEMultipart()
        msg['From'] = app_config['MAIL_USERNAME']
        msg['To'] = 'kontakt@unidstudio.dk'
        msg['Subject'] = 'New Contact Form Submission'
        
        body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(app_config['MAIL_SERVER'], app_config['MAIL_PORT']) as server:
            server.starttls()
            server.login(app_config['MAIL_USERNAME'], app_config['MAIL_PASSWORD'])
            server.sendmail(msg['From'], msg['To'], msg.as_string())

        return template('success', message="Message sent successfully!")
    except Exception as e:
        return template('error', message=f"Failed to send message. Error: {str(e)}")
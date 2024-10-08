##############################
#   IMPORTS
#   Library imports
from bottle import template, get, request
import logging
import os

#   Local application imports
from common.colored_logging import setup_logger
import common.content as content
import master


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
    blog_content = content.blog_content
    logger.success("Content imported successfully.")
except Exception as e:
    logger.error(f"Error importing content: {e}")
finally:
    logger.info("Content import process completed.")


##############################
#   BLOG
@get("/blog")
def blog():

    page_name = "blog"

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
                        title="UNID Studio - Blog",
                        # A-Z
                        global_content=global_content,
                        blog_content=blog_content,
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
#   BLOG POSTS
@get("/hastighedsoptimering-paa-hjemmesider-er-en-noedvendighed")
def blog():

    page_name = "blog_posts/hastighedsoptimering-paa-hjemmesider-er-en-noedvendighed"

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
                        title="UNID Studio - Hastighedsoptimering på hjemmesider er en nødvendighed!",
                        # A-Z
                        global_content=global_content,
                        blog_content=blog_content,
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


@get("/hastighedsoptimer-din-wordpress-hjemmeside")
def blog():

    page_name = "blog_posts/hastighedsoptimer-din-wordpress-hjemmeside"

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
                        title="UNID Studio - Hastighedsoptimer din WordPress-hjemmeside",
                        # A-Z
                        global_content=global_content,
                        blog_content=blog_content,
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


@get("/hvem-laver-gode-hjemmesider")
def blog():

    page_name = "blog_posts/hvem-laver-gode-hjemmesider"

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
                        title="UNID Studio - Hvem laver gode hjemmesider?",
                        # A-Z
                        global_content=global_content,
                        blog_content=blog_content,
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


@get("/wordpress-webshop-i-woocommerce")
def blog():

    page_name = "blog_posts/wordpress-webshop-i-woocommerce"

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
                        title="UNID Studio - WordPress webshop i WooCommerce ",
                        # A-Z
                        global_content=global_content,
                        blog_content=blog_content,
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
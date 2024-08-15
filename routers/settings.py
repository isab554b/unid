##############################
#   IMPORTS
#   Library imports
from bottle import post, get, request, response, template, delete
import logging
import os
import uuid
import time

#   Local application imports
from common.colored_logging import setup_logger
from common.get_current_user import get_current_user
from common.find_template import *
from common.time_formatting import *
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
    profile_content = content.profile_content
    logger.success("Content imported successfully.")
except Exception as e:
    logger.error(f"Error importing content: {e}")
finally:
    logger.info("Content import process completed.")


##############################
#   ADMIN CUSTOMERS GET
@get('/profile/profile_admin_settings')
def admin_customers_get():
    page_name = "admin_customers_get"

    try:
        # Establish database connection
        db = master.db()
        logger.debug(f"Database connection opened for {page_name}")

        # Set up cursor and execute query to fetch active customers and their user details
        cursor = db.cursor()
        cursor.execute("""
            SELECT
                customers.customer_id,
                customers.website_name,
                customers.website_url,
                users.user_id,
                users.first_name,
                users.last_name,
                users.email,
                users.phone,
                users.is_active,
                CASE
                    WHEN active_clipcards.user_id IS NOT NULL THEN active_clipcards.clipcard_type_title
                    ELSE 'Intet klippekort eller abonnement.'
                END AS clipcard_type
            FROM customers
            JOIN users ON customers.customer_id = users.user_id
            LEFT JOIN (
                SELECT DISTINCT user_id, clipcard_type_title
                FROM active_clipcards
            ) AS active_clipcards ON users.user_id = active_clipcards.user_id
            WHERE users.is_active = 1
        """)

        # Retrieve all customers from the query
        customers = cursor.fetchall()
        
        logger.debug(f"Customers retrieved: {customers}")

        # Find the template and remove path and file extension
        template_path = find_template('profile_admin_settings', template_dirs)
        if template_path is None:
            return "Template not found."
        relative_path = template_path.replace('views/', '').replace('.tpl', '')

        # Show template
        logger.success(f"Successfully showing template for {page_name}")
        return template(relative_path, 
                        global_content=global_content, 
                        customers=customers,
                        profile_content=profile_content
                        )

    except Exception as e:
        if "db" in locals():
            db.rollback()
            logger.info("Database transaction rolled back due to exception")
        logger.error(f"Error during {page_name}: {e}")
        response.status = 500
        return {"error": "Internal Server Error"}

    finally:
        if "db" in locals():
            db.close()
            logger.info("Database connection closed")
        logger.info(f"Completed {page_name}")






##############################
#   DELETE CUSTOMER
@delete('/delete_user')
def delete_user():
    function_name = "delete_user"

    try:
        # Retrieve user ID from the request body
        user_id = request.forms.get('user_id')
        if not user_id:
            logger.warning(f"User ID missing in {function_name}")
            response.status = 400
            return {"info": "User ID is missing."}

        # Confirm current user is logged in
        current_user = get_current_user()
        if not current_user:
            logger.warning(f"User not logged in during {function_name}")
            response.status = 401
            return {"info": "User not logged in."}

        logger.info(f"Attempting to delete user with ID: {user_id}")

        # Establish database connection
        db = master.db()
        cursor = db.cursor()

        # Delete user from users table
        cursor.execute("""
            DELETE FROM users
            WHERE user_id = ?
        """, (user_id,))

        # Optionally delete corresponding customer if necessary
        cursor.execute("""
            DELETE FROM customers
            WHERE customer_id = ?
        """, (user_id,))  # Assuming customer_id = user_id

        # Commit changes to the database
        db.commit()

        # Check if the user was actually found and deleted
        if cursor.rowcount == 0:
            logger.error(f"User with ID {user_id} not found in {function_name}")
            response.status = 404
            return {"info": "User not found."}

        logger.info(f"User with ID {user_id} deleted successfully")
        return {"info": "User deleted."}

    except Exception as e:
        if "db" in locals():
            db.rollback()
            logger.info("Database transaction rolled back due to exception")
        logger.error(f"Error during {function_name}: {e}")
        response.status = 500
        return {"error": "Internal Server Error"}

    finally:
        if "db" in locals():
            db.close()
            logger.info("Database connection closed")
        logger.info(f"Completed {function_name}")



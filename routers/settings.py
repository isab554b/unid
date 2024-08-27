##############################
#   IMPORTS
#   Library imports
from bottle import get, request, response, template, delete, post, redirect
import logging
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
#   ADMIN - GET CUSTOMERS 
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
                COALESCE(active_clipcards.clipcard_type_title, 'Intet klippekort') AS clipcard_type,
                COALESCE(active_subscriptions.subscription_price, 'Intet abonnement') AS subscription_price
            FROM customers
            JOIN users ON customers.customer_id = users.user_id
            LEFT JOIN (
                SELECT DISTINCT user_id, clipcard_type_title
                FROM active_clipcards
            ) AS active_clipcards ON users.user_id = active_clipcards.user_id
            LEFT JOIN (
                SELECT DISTINCT user_id, subscription_price
                FROM active_subscriptions
            ) AS active_subscriptions ON users.user_id = active_subscriptions.user_id
            WHERE users.is_active = 1
        """)

        # Retrieve all customers from the query
        customers = cursor.fetchall()
        
        # Prepare descriptive text for subscription in Python code
        for customer in customers:
            if customer["subscription_price"] != 'Intet abonnement':
                customer["subscription_status"] = "Aktivt abonnement"
            else:
                customer["subscription_status"] = 'Intet abonnement'

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
#   ADMIN - DELETE CUSTOMER
@delete('/delete_user')
def delete_user():
    function_name = "delete_user"

    try:
        user_id = request.forms.get('user_id')
        if not user_id:
            logger.warning(f"User ID missing in {function_name}")
            response.status = 400
            return {"info": "User ID is missing."}

        current_user = get_current_user()
        if not current_user:
            logger.warning(f"User not logged in during {function_name}")
            response.status = 401
            return {"info": "User not logged in."}

        logger.info(f"Attempting to delete user with ID: {user_id}")

        db = master.db()
        cursor = db.cursor()

        # Update the deleted_at field in users table with UNIX timestamp
        cursor.execute("""
            UPDATE users
            SET deleted_at = ?, updated_at = ?
            WHERE user_id = ?
        """, (int(time.time()), int(time.time()), user_id))

        cursor.execute("""
            DELETE FROM customers
            WHERE customer_id = ?
        """, (user_id,))

        db.commit()

        if cursor.rowcount == 0:
            logger.error(f"User with ID {user_id} not found in {function_name}")
            response.status = 404
            return {"info": "User not found."}

        logger.info(f"User with ID {user_id} marked as deleted successfully")
        return {"info": "User deleted."}  # Return the exact message expected by the frontend

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



##############################
#   CUSTOMER - GET PROFILE SETTINGS
@get('/profile/profile_customer_settings')
def profile_customer_settings():
    page_name = "profile_customer_settings"

    try:
        # Confirm current user is logged in
        current_user = get_current_user()
        if not current_user:
            logger.warning(f"User not logged in during {page_name}")
            response.status = 401
            return {"info": "User not logged in."}

        user_id = current_user['user_id']

        # Establish database connection
        db = master.db()
        logger.debug(f"Database connection opened for {page_name}")

        # Set up cursor and execute query to fetch the current user's details
        cursor = db.cursor()
        cursor.execute("""
            SELECT
                users.user_id,
                users.first_name,
                users.last_name,
                users.email,
                users.phone,
                users.username,
                CASE
                    WHEN active_clipcards.user_id IS NOT NULL THEN active_clipcards.clipcard_type_title
                    ELSE 'Intet klippekort eller abonnement.'
                END AS clipcard_type
            FROM users
            LEFT JOIN (
                SELECT DISTINCT user_id, clipcard_type_title
                FROM active_clipcards
            ) AS active_clipcards ON users.user_id = active_clipcards.user_id
            WHERE users.user_id = ?
        """, (user_id,))

        # Retrieve the user's details
        user = cursor.fetchone()

        if not user:
            logger.warning(f"User with ID {user_id} not found during {page_name}")
            response.status = 404
            return {"info": "User not found."}

        logger.debug(f"User retrieved: {user}")

        # Find the template and remove path and file extension
        template_path = find_template('profile_customer_settings', template_dirs)
        if template_path is None:
            return "Template not found."
        relative_path = template_path.replace('views/', '').replace('.tpl', '')

        # Show template
        logger.success(f"Successfully showing template for {page_name}")
        return template(relative_path, 
                        global_content=global_content, 
                        user=user,
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
#   CUSTOMER - UPDATE PROFILE
@post('/update_profile')
def update_profile():
    try:
        username = request.forms.get('username')
        email = request.forms.get('email')
        phone = request.forms.get('phone')
        
        
        current_user = get_current_user()
        if not current_user:
            response.status = 401
            return {"success": False, "error": "User not logged in."}

        user_id = current_user['user_id']

        db = master.db()
        cursor = db.cursor()

        cursor.execute("""
            UPDATE users
            SET username = ?, email = ?, phone = ?
            WHERE user_id = ?
        """, (username, email, phone, user_id))

        db.commit()

        response.status = 200
        return {"info": "Profil opdateret!"}

    except Exception as e:
        if "db" in locals():
            db.rollback()
        response.status = 500
        return {"info": f"Fejl under opdatering af profil: {str(e)}"}

    finally:
        if "db" in locals():
            db.close()


##############################
#   CUSTOMER - DELETE PROFILE
@post('/delete_profile')
def delete_profile():
    function_name = "delete_profile"

    try:
        # Retrieve user ID from the request body
        user_id = request.json.get('user_id')
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

        if current_user['user_id'] != user_id:
            logger.warning(f"User ID mismatch in {function_name}")
            response.status = 403
            return {"info": "You cannot delete another user's profile."}

        logger.info(f"Attempting to delete profile with ID: {user_id}")

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
            return {"info": "Profile not found."}

        logger.info(f"Profile with ID {user_id} deleted successfully")

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

    # Redirect to the homepage after successful deletion
    redirect('/')





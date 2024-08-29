##############################
#   IMPORTS
#   Library imports
from bottle import get, template, post, delete
import time
import logging
import re

#   Local application imports
from common.colored_logging import setup_logger
from common.get_current_user import *
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
    services_and_prices_content = content.services_and_prices_content
    profile_content = content.profile_content
    logger.success("Content imported successfully.")
except Exception as e:
    logger.error(f"Error importing content: {e}")
finally:
    logger.info("Content import process completed.")


##############################
#   DATABASE INITIALIZATION
db = master.db()


##############################
#   ADMIN SUBSCRIPTIONS
@get('/profile/profile_admin_subscriptions')
def admin_subscriptions_get():

    page_name = "profile_admin_subscriptions"

    try:
        # Establish database connection
        db = master.db()
        logger.debug(f"Database connection opened for {page_name}")

        # Load correct template
        template_path = find_template('profile_admin_subscriptions', template_dirs)  # Find the required template
        if template_path is None:
            logger.error(f"Template '{page_name}' not found.")
            return "Template not found."
        relative_path = template_path.replace('views/', '').replace('.tpl', '')  # Normalize the template path

        # Retrieve information about active subscriptions
        cursor = db.cursor()
        cursor.execute("""
            SELECT subscriptions.subscription_id, subscriptions.created_at,
                   users.user_id, users.first_name, users.last_name, users.username, users.email, users.phone,
                   customers.website_name, customers.website_url
            FROM subscriptions
            JOIN subscriptions_payments ON subscriptions.subscription_id = subscriptions_payments.subscription_id
            JOIN users ON subscriptions_payments.user_id = users.user_id
            JOIN customers ON users.user_id = customers.customer_id
            WHERE subscriptions.is_active = 1;
        """)
        active_subscriptions = cursor.fetchall()
        cursor.close()

        if not active_subscriptions:
            logger.info("No active subscriptions found.")
            return template(relative_path, 
                            # A-Z
                            active_subscriptions=[], 
                            active_customers=[],
                            global_content=global_content,
                            profile_content=profile_content,
                            )

       
        active_customers = []
        for subscription in active_subscriptions:
            try:
                # Convert time used and remaining time (from minutes to hours and minutes)
                subscription['formatted_created_at'] = format_created_at(subscription['created_at'])

                # Collect user information conneced with subscription
                active_customers.append({
                    'user_id': subscription['user_id'],
                    'first_name': subscription['first_name'],
                    'last_name': subscription['last_name'],
                    'subscription_id': subscription['subscription_id']
                })

                logger.success(f"Processed subscription {subscription['subscription_id']} for user {subscription['user_id']}")

            except Exception as e:
                logger.error(f"Error processing subscription {subscription['subscription_id']}: {e}")

        # Show template
        logger.success(f"Succesfully showing template for {page_name}")
        return template(relative_path,
                        # A-Z
                        active_subscriptions=active_subscriptions,
                        active_customers=active_customers,
                        global_content=global_content,
                        profile_content=profile_content,
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
#   ADMIN DELETE SUBSCRIPTION
# Regex for at matche ID-formatet
id_pattern = re.compile(r'^sub_[a-zA-Z0-9_]+$')

@delete('/delete_subscription/<subscription_id>')
def delete_subscription(subscription_id):
    function_name = "delete_subscription"

    # Valider ID-formatet
    if not id_pattern.match(subscription_id):
        response.status = 400
        return {"error": "Invalid subscription ID format."}

    try:
        # Establish database connection
        db = master.db()
        logger.debug(f"Database connection opened for {function_name}")

        cursor = db.cursor()

        # Check if the subscription exists
        cursor.execute("SELECT * FROM subscriptions WHERE subscription_id = ?", (subscription_id,))
        existing_subscription = cursor.fetchone()

        # Error if no subscription
        if existing_subscription is None:
            logger.error(f"No subscription found with ID: {subscription_id}")
            response.status = 404
            return {"info": f"The subscription with id {subscription_id} does not exist."}

        # Info if already has been deleted
        if existing_subscription["is_active"] == "0":
            logger.info(f"Subscription {subscription_id} has already been deleted.")
            response.status = 400
            return {"info": f"The subscription with id {subscription_id} has already been deleted."}

        # Update subscription as deleted
        deleted_at = int(time.time())
        cursor.execute("""
            UPDATE subscriptions
            SET deleted_at = ?, is_active = 0
            WHERE subscription_id = ?
        """, (deleted_at, subscription_id))

        # Commit changes to the database
        db.commit()
        logger.success(f"{function_name} successful, subscription {subscription_id} deleted successfully")
        return {"message": f"{function_name} successful"}

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


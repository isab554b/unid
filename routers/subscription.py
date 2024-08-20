##############################
#   IMPORTS
#   Library imports
from bottle import get, template, HTTPResponse
import logging

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

        # Retrieve information about active clipcards
        cursor = db.cursor()
        cursor.execute("""
            SELECT subscriptions.subscription_id, subscriptions.created_at,
                   users.user_id, users.first_name, users.last_name, users.username, users.email, users.phone,
                   customers.website_name, customers.website_url
            FROM subscriptions
            JOIN payments ON subscriptions.subscription_id = payments.subscription_id
            JOIN users ON payments.user_id = users.user_id
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
                
                # Collect user information conneced with clipcard
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
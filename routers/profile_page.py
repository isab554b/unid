##############################
#   IMPORTS
#   Library imports
from bottle import get, template, route, HTTPResponse
import logging
from datetime import datetime
import time

#   Local application imports
from common.colored_logging import setup_logger
from common.get_current_user import *
from common.find_template import *
from common.time_formatting import *
import common.content as content
import routers.messages as messages
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
    global_content = content.global_content
    services_and_prices_content = content.services_and_prices_content
    profile_content = content.profile_content
    logger.success("Content imported successfully.")
except Exception as e:
    logger.error("Error importing content: %s", e)
finally:
    logger.info("Content import process completed.")


##############################
#   LOAD PROFILE DATA
#   Fetching information to be included in customer clipcards / timeregistration
def load_profile_data():

    function_name = "load_profile_data"

    try:
        # Retrieve current user details
        current_user = get_current_user()

        # Redirect if not logged in
        if not current_user:
            logger.info("No current user found, redirecting to login.")
            return HTTPResponse(status=303, headers={"Location": "/"})

        # Establish database connection
        db = master.db()
        logger.debug(f"Database connection opened for {function_name}")

        user = current_user

        # Retrieve active clipcard ID for the current user
        payment_query = """
            SELECT clipcards_payments.clipcard_id
            FROM clipcards_payments
            WHERE clipcards_payments.user_id = ? AND clipcards_payments.clipcard_id IN (SELECT clipcard_id FROM clipcards WHERE is_active = 1)
            LIMIT 1
        """

        # Fetch the result
        payment = db.execute(payment_query, (user['user_id'],)).fetchone()

        # Initialize variables for time
        time_used_hours = time_used_minutes = remaining_hours = remaining_minutes = 0

        # If a valid payment and clipcard are found, retrieve detailed clipcard data
        if payment and payment['clipcard_id']:
            clipcard_data = db.execute("""
                SELECT time_used, remaining_time
                FROM clipcards
                WHERE clipcard_id = ? AND is_active = 1
            """, (payment['clipcard_id'],)).fetchone()

            # If clipcard data is found, convert time
            if clipcard_data:
                time_used_hours, time_used_minutes = minutes_to_hours_minutes(clipcard_data['time_used'])
                remaining_hours, remaining_minutes = minutes_to_hours_minutes(clipcard_data['remaining_time'])
            else:
                logger.info("Active clipcard data not found for user.")
        else:
            logger.info("No active payment found for user.")

        # Count active and inactive clipcards
        active_clipcards_count = db.execute("SELECT COUNT(*) AS count FROM clipcards WHERE is_active = 1").fetchone()['count']
        inactive_clipcards_count = db.execute("SELECT COUNT(*) AS count FROM clipcards WHERE is_active = 0").fetchone()['count']

        # Return a dictionary of all relevant information
        return {
            'user': user,
            'first_name': user['first_name'],
            'last_name': user['last_name'],
            'username': user['username'],
            'active_clipcards_count': active_clipcards_count,
            'inactive_clipcards_count': inactive_clipcards_count,
            'time_used_hours': time_used_hours,
            'time_used_minutes': time_used_minutes,
            'remaining_hours': remaining_hours,
            'remaining_minutes': remaining_minutes,
        }

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
#   PROFILE
@get("/profile")
def profile():

    page_name = "profile"

    try:
        # Check if response is HTTP response
        data = load_profile_data()
        if isinstance(data, HTTPResponse):
            return data

        # Retrieve current user details
        current_user = get_current_user()

        # Handle cases that require detailed user information
        if current_user:
            db = master.db()
            clipcard_info = db.execute("SELECT clipcard_id FROM clipcards_payments WHERE user_id = ? LIMIT 1", (current_user['user_id'],)).fetchone()
            if clipcard_info and clipcard_info['clipcard_id']:
                has_active_clipcard = db.execute("""
                    SELECT COUNT(*) AS active_clipcards
                    FROM clipcards
                    WHERE clipcard_id = ? AND is_active = 1
                """, (clipcard_info['clipcard_id'],)).fetchone()['active_clipcards'] > 0
                current_user['has_active_clipcard'] = has_active_clipcard

        # Handle cases that require detailed user information
        if current_user:
            db = master.db()
            subscription_info = db.execute("""
                SELECT s.subscription_id, s.created_at
                FROM subscriptions s
                JOIN subscriptions_payments sp ON s.subscription_id = sp.subscription_id
                WHERE sp.user_id = ? AND s.is_active = 1
                LIMIT 1
            """, (current_user['user_id'],)).fetchone()

            if subscription_info:
                subscription_start_time = int(subscription_info['created_at'])  
                current_time = time.time() 

                time_difference = current_time - subscription_start_time
                can_cancel = time_difference > 7889472

                current_user['subscription_id'] = subscription_info['subscription_id']
                current_user['has_active_subscription'] = True
            else:
                can_cancel = False
                current_user['has_active_subscription'] = False


        # Show template
        logger.success(f"Succesfully showing template for {page_name}")
        return template('profile', 
                        title="Din profil",
                        # A-Z
                        active_clipcards_count=data['active_clipcards_count'],
                        current_user=current_user,
                        first_name=data['first_name'],
                        global_content=global_content,
                        inactive_clipcards_count=data['inactive_clipcards_count'],
                        last_name=data['last_name'],
                        profile_content=profile_content,
                        remaining_hours=data['remaining_hours'],
                        remaining_minutes=data['remaining_minutes'],
                        services_and_prices_content=services_and_prices_content,
                        time_used_hours=data['time_used_hours'],
                        time_used_minutes=data['time_used_minutes'],
                        user=data['user'],
                        username=data['username'],
                        can_cancel=can_cancel
                        )

    except Exception as e:
        logger.error(f"Error during request for /{page_name}: {e}")
        raise

    finally:
        logger.info(f"Completed request for /{page_name}")


##############################
#   PROFILE TEMPLATE
@route('/profile/<template_name>')
def profile_template(template_name):
    function_name = "profile_template"
  

    try:
        logger.info("Starting profile_template function")
        
        # Load profile data
        data = load_profile_data()
        if isinstance(data, HTTPResponse):
            return data

        # Retrieve current user details
        current_user = get_current_user() 
        logger.info(f"Current user loaded: {current_user}")

        # Determine and load template
        template_path = find_template(template_name, template_dirs)
        if template_path is None:
            logger.error(f"Template '{template_name}' not found.")
            return "Template not found."

        # Initialize relative_path early to avoid undefined variable error
        relative_path = template_path.replace('views/', '').replace('.tpl', '')
        logger.info(f"Template path determined: {relative_path}")

        # Handle cases for 'profile_overview' that require detailed user information
        if template_name == "profile_overview":
            if not current_user:
                logger.error("current_user is not available when required")
            else:
                db = master.db()
                clipcard_info = db.execute(
                    "SELECT clipcard_id FROM clipcards_payments WHERE user_id = ? LIMIT 1", 
                    (current_user.get('user_id'),)
                ).fetchone()

                if clipcard_info and clipcard_info['clipcard_id']:
                    has_active_clipcard = db.execute("""
                        SELECT COUNT(*) AS active_clipcards
                        FROM clipcards
                        WHERE clipcard_id = ? AND is_active = 1
                    """, (clipcard_info['clipcard_id'],)).fetchone()['active_clipcards'] > 0
                    current_user['has_active_clipcard'] = has_active_clipcard
                logger.info(f"Clipcard information updated: {current_user}")

        # Handle cases that require detailed user information
        can_cancel = False 
        if not current_user:
            logger.error("current_user is not available before subscription check")
        else:
            db = master.db()
            subscription_info = db.execute("""
                SELECT s.subscription_id, s.created_at
                FROM subscriptions s
                JOIN subscriptions_payments sp ON s.subscription_id = sp.subscription_id
                WHERE sp.user_id = ? AND s.is_active = 1
                LIMIT 1
            """, (current_user.get('user_id'),)).fetchone()

            if subscription_info:
                subscription_start_time = int(subscription_info['created_at'])
                current_time = time.time()
                time_difference = current_time - subscription_start_time
                can_cancel = time_difference > 7889472
                current_user['subscription_id'] = subscription_info['subscription_id']
                current_user['has_active_subscription'] = True
            else:
                current_user['has_active_subscription'] = False
            logger.info(f"Subscription information updated: {current_user}")

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
        logger.info(f"Active subscriptions retrieved: {len(active_subscriptions)} found")

        active_customers = []
        for subscription in active_subscriptions:
            try:
                subscription['formatted_created_at'] = format_created_at(subscription['created_at'])
                active_customers.append({
                    'user_id': subscription['user_id'],
                    'first_name': subscription['first_name'],
                    'last_name': subscription['last_name'],
                    'subscription_id': subscription['subscription_id']
                })
                logger.success(f"Processed subscription {subscription['subscription_id']} for user {subscription['user_id']}")
            except Exception as e:
                logger.error(f"Error processing subscription {subscription['subscription_id']}: {e}")

        logger.info(f"Rendering template with current_user: {current_user}")
        return template(relative_path,
                        active_clipcards_count=data.get('active_clipcards_count', 0),
                        current_user=current_user, 
                        first_name=data.get('first_name', ''),
                        global_content=global_content,
                        inactive_clipcards_count=data.get('inactive_clipcards_count', 0),
                        last_name=data.get('last_name', ''),
                        profile_content=profile_content,
                        remaining_hours=data.get('remaining_hours', 0),
                        remaining_minutes=data.get('remaining_minutes', 0),
                        services_and_prices_content=services_and_prices_content,
                        time_used_hours=data.get('time_used_hours', 0),
                        time_used_minutes=data.get('time_used_minutes', 0),
                        user=data.get('user', {}),
                        username=data.get('username', ''),
                        can_cancel=can_cancel,
                        active_subscriptions=active_subscriptions)

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







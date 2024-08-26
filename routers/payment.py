##############################
#   IMPORTS
#   Library imports
from bottle import post, request, template, response, get
import uuid
import time
import logging
import os
import re
import stripe
from dotenv import load_dotenv

#   Local application imports
from common.colored_logging import setup_logger
from common.get_current_user import get_current_user
import common.content as content
import master


##############################
#   LOAD ENVIRONMENT VARIABLES
load_dotenv()


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
    profile_content = content.profile_content
    logger.success("Content imported successfully.")
except Exception as e:
    logger.error(f"Error importing content: {e}")
finally:
    logger.info("Content import process completed.")


##############################
#   CLIPCARD CHECKOUT SESSION
#   Set Stripe API key from environment variable
stripe.api_key = "sk_test_51OlrinIT5aFkJJVMeEUrQBIp7uJyMOQEbO295rfabj8ZW3C0Uy5sUzsYyvZOoLqI0hwbSj5qmg9qMrZMKhqOlUyo009gCzGBC9"

# Route to create a Stripe checkout session
@post('/create_checkout_session')
def create_checkout_session():
    try:
        # Retrieve data from the request
        data = request.json
        clipcard_type = data.get('clipcard_type')
        clipcard_price_str = data.get('clipcard_price')

        # Remove any non-numeric characters (e.g., ' DKK') to get the numeric value
        clipcard_price = float(clipcard_price_str.replace(' DKK', '').replace('.', '').replace(',', '.'))

        # Create Stripe checkout session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'dkk',
                    'product_data': {
                        'name': clipcard_type,
                    },
                    'unit_amount': int(clipcard_price * 100),  # convert to øre
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1:2500/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='http://127.0.0.1:2500/cancel',
            metadata={
                'clipcard_type': clipcard_type,  # Save clipcard type in metadata
            }
        )

        return {'id': session.id}
    except Exception as e:
        logger.error(f"Error creating Stripe checkout session: {e}")
        response.status = 500
        return {"error": "Internal Server Error"}


##############################
#   CLIPCARD CHECKOUT SESSION SUCCES
@get('/success')
def payment_success():
    try:
        session_id = request.query.get('session_id')
        session = stripe.checkout.Session.retrieve(session_id)

        if session.payment_status == 'paid':
            # Retrieve current user details
            current_user = get_current_user()
            user_id = current_user['user_id']

            # Retrieve payment details from the form
            clipcard_price = session.amount_total / 100  # convert from øre to DKK
            amount_paid = clipcard_price
            payment_id = str(uuid.uuid4())
            clipcard_id = str(uuid.uuid4())
            created_at = int(time.time())
            updated_at = int(time.time())
            is_active = 1
            clipcard_type_title = session.metadata['clipcard_type']
            time_used = 0

            # Establish database connection
            db = master.db()
            logger.debug(f"Database connection opened for payment success handling")

            # Retrieve clipcard type details from database
            cursor = db.cursor()
            cursor.execute("SELECT clipcard_type_id, clipcard_type_time FROM card_types WHERE clipcard_type_title = ?", (clipcard_type_title,))
            row = cursor.fetchone()

            if not row:
                logger.error("Clipcard type not found.")
                raise Exception('Clipcard type not found')

            clipcard_type_id = row['clipcard_type_id']
            remaining_time = row['clipcard_type_time']

            # Insert payment and clipcard records into the database
            cursor.execute("INSERT INTO clipcards_payments (payment_id, user_id, clipcard_id, amount_paid, created_at) VALUES (?, ?, ?, ?, ?)",
                           (payment_id, user_id, clipcard_id, amount_paid, created_at))
            cursor.execute("INSERT INTO clipcards (clipcard_id, clipcard_type_id, time_used, remaining_time, created_at, updated_at, is_active) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (clipcard_id, clipcard_type_id, time_used, remaining_time, created_at, updated_at, is_active))

            # Commit changes to the database
            db.commit()
            logger.success("Payment success handling completed successfully")
            cursor.close()

            # Redirect to a success page or return a success message
            return template("confirmation",
                        title="Confirmation",
                        # A-Z
                        amount_paid=amount_paid,
                        clipcard_type_title=clipcard_type_title,
                        created_at=created_at,
                        global_content=global_content,
                        payment_id=payment_id,
                        profile_content=profile_content,
                        )

    except Exception as e:
        if "db" in locals():
            db.rollback()
            logger.info("Database transaction rolled back due to exception")
        logger.error(f"Error during payment success handling: {e}")
        response.status = 500
        return {"error": "Internal Server Error"}

    finally:
        if "db" in locals():
            db.close()
            logger.info("Database connection closed")

##############################
#   SUBSCRIPTION CHECKOUT SESSION
# Function to extract price from a string
def extract_price(price_str):
    # Regex to match the numeric part before any non-numeric characters
    match = re.match(r'(\d+)', price_str)
    if match:
        return float(match.group(1))
    else:
        raise ValueError("Price format is incorrect")
    
#   Set Stripe API key from environment variable
stripe.api_key = "sk_test_51OlrinIT5aFkJJVMeEUrQBIp7uJyMOQEbO295rfabj8ZW3C0Uy5sUzsYyvZOoLqI0hwbSj5qmg9qMrZMKhqOlUyo009gCzGBC9"

@post('/create_subscription_checkout_session')
def create_subscription_checkout_session():
    try:
        # Retrieve data from the request
        data = request.json
        subscription_type = data.get('subscription_type')
        subscription_price_str = data.get('subscription_price')

        # Extract the numeric price
        subscription_price = extract_price(subscription_price_str)

        # Create a product in Stripe if it doesn't already exist
        product = stripe.Product.create(name=subscription_type)

        # Create a price object in Stripe for the subscription
        price = stripe.Price.create(
            unit_amount=int(subscription_price * 100),  # convert to øre
            currency='dkk',
            recurring={'interval': 'month'},
            product=product.id,
        )

        # Create Stripe checkout session for subscription
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': price.id,
                'quantity': 1,
            }],
            mode='subscription',
            success_url='http://127.0.0.1:2500/subscription_success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='http://127.0.0.1:2500/cancel',
            metadata={
                'subscription_type': subscription_type,
            }
        )

        return {'id': session.id}
    except Exception as e:
        logger.error(f"Error creating Stripe checkout session: {e}")
        response.status = 500
        return {"error": "Internal Server Error"}

##############################
#   SUBSCRIPTION CHECKOUT SESSION SUCCES
@get('/subscription_success')
def subscription_success():
    try:
        session_id = request.query.get('session_id')
        
        # Retrieve the Stripe session using the session_id
        session = stripe.checkout.Session.retrieve(session_id)
        
        # Check if the payment status is 'paid'
        if session.payment_status == 'paid':
            current_user = get_current_user()
            user_id = current_user['user_id']
            
            # Get subscription ID from the session (if available)
            subscription_id = session.get('subscription')
            
            if not subscription_id:
                raise ValueError("No subscription ID found in the session.")

            # Calculate subscription price and other details
            subscription_price = session.amount_total / 100  # convert from øre to DKK
            amount_paid = subscription_price
            payment_id = str(uuid.uuid4())
            created_at = int(time.time())
            is_active = 1
            
            # Connect to the database
            db = master.db()
            cursor = db.cursor()
            
            # Insert payment details
            cursor.execute("""
                INSERT INTO subscriptions_payments (payment_id, user_id, subscription_id, amount_paid, created_at)
                VALUES (?, ?, ?, ?, ?)
            """, (payment_id, user_id, subscription_id, amount_paid, created_at))
            
            # Insert subscription details
            cursor.execute("""
                INSERT INTO subscriptions (subscription_id, subscription_price, created_at, is_active)
                VALUES (?, ?, ?, ?)
            """, (subscription_id, amount_paid, created_at, is_active))

            # Commit changes
            db.commit()
            cursor.close()
            
            # Return confirmation template
            return template("subscription_confirmation",
                            title="Confirmation",
                            amount_paid=amount_paid,
                            created_at=created_at,
                            global_content=global_content,
                            payment_id=payment_id,
                            profile_content=profile_content,
                            )
    except Exception as e:
        if "db" in locals():
            db.rollback()
        logger.error(f"Error during payment success handling: {e}")
        response.status = 500
        return {"error": "Internal Server Error"}
    finally:
        if "db" in locals():
            db.close()





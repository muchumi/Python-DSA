from datetime import datetime

"""
    Story
    Your online store likes to give out coupons for special occasions. Some customers try to cheat the system by entering invalid codes or using expired coupons.
    Task
    Your mission:
    Write a function called checkCoupon which verifies that a coupon code is valid and not expired.
    A coupon is no more valid on the day AFTER the expiration date. All dates will be passed as strings in this format: "MONTH DATE, YEAR".
"""

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    # Checking if the entered code matches the correct code
    if entered_code != correct_code:
        return False
    
    # Converting the date strings to datetime objects
    current_date_obj = datetime.strptime(current_date, "%B %d, %Y")
    expiration_date_obj = datetime.strptime(expiration_date, "%B %d, %Y")
    
    # Checking if the current date is on or before the expiration date
    return current_date_obj <= expiration_date_obj
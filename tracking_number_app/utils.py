import random
import string

def generate_tracking_number(validated_data):
    origin_country_id = validated_data["origin_country_id"]
    customer_id = validated_data['customer_id']
    chars_from_order = f"{origin_country_id}{str(customer_id)[:4].upper()}"
    random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return chars_from_order+random_chars

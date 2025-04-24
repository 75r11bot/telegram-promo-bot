import re
def extract_promo_codes(message):
    return re.findall(r'\b[a-zA-Z0-9]{8,}\b', message)
import re
import unicodedata

def process_data(data):
    # Normalize data
    normalized_data = unicodedata.normalize('NFKD', data).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    # Convert to lowercase
    normalized_data = normalized_data.lower()
    # Remove punctuation
    normalized_data = re.sub(r'[^\w\s]', '', normalized_data).strip()
    # Tokenize
    tokens = normalized_data.split()
    return tokens


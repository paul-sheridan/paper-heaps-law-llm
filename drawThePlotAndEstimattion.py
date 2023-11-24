import json
import pickle
from processData import process_data

def main():
    file_path = 'data/test.jsonl'
    processed_data = []
    limit = 500000
    prompt_length = 5
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                data_chunk = json.loads(line).get('text', '')  # Assuming each line is a JSON object with an 'abstract' field
                processed_line = process_data(data_chunk)
                if len(processed_line) > prompt_length:  # Check if the processed line has more than 10 words
                    processed_data.append(processed_line)
                    if len(processed_data) >= limit:
                        break
        with open('processData.pickle', 'wb') as f:
            pickle.dump(processed_data, f)
        print("Data has been processed and saved to 'processData.pickle'")
    except FileNotFoundError:
        print("The file was not found. Please check the file path.")
    except json.JSONDecodeError:
        print("Error decoding JSON. Please check the file content.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()


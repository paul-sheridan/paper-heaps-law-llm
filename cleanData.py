import pickle
import random
# Make sure processData.py is in the same directory or in the PYTHONPATH
from processData import process_data

# Path to the original and new pickle files
input_path = 'dataGenaration/result/result-gptNeo2.7b.pkl'
output_path = 'data/proccessData2.7.pkl'

# Load the original pickle file
with open(input_path, 'rb') as file:
    original_data = pickle.load(file)
print(original_data)
random.shuffle(original_data)
# Process the original data using the imported function
processed_data = [process_data(item) for item in original_data]

# Now, we will save the processed data as an array of arrays
with open(output_path, 'wb') as outfile:
    pickle.dump(processed_data, outfile)

print("Data processing complete and saved to proccessData125m.pkl")


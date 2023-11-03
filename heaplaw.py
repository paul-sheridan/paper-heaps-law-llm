import pickle
import random

def process_data(input_file):
    # Initialize counters
    overall_total_words = 0
    overall_unique_words = set()

    with open(input_file, 'rb') as f:
        data = pickle.load(f)

    # Shuffle the main data array
    random.shuffle(data)

    # Initialize the result array
    result = []

    for word_array in data:
        # Update the overall counters
        overall_total_words += len(word_array)
        overall_unique_words.update(word_array)

        # Append the current count and unique count to result
        result.append([overall_total_words, len(overall_unique_words)])

    return result

if __name__ == '__main__':
    input_file = 'data/proccessData1.3.pkl'
    output_file = 'dataGenaration/result/heaplaw1.3b.pkl'

    result = process_data(input_file)

    # Save the result array to a file
    with open(output_file, 'wb') as f:
        pickle.dump(result, f)

    print(f"Result saved to {output_file}")


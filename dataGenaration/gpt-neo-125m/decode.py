import pickle
from transformers import GPT2Tokenizer

def decode_generated_text(model_name, start_idx, end_idx, input_folder, output_file):
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    all_decoded_texts = []

    for i in range(start_idx, end_idx + 1):
        input_file = f"{input_folder}/gpt-neo-125m-{i}.pkl"
        print(f"Processing {input_file}...")

        # Load the generated text (as token IDs)
        try:
            with open(input_file, 'rb') as f:
                generated_text_ids = pickle.load(f)

            # Decode the text
            decoded_texts = [tokenizer.decode(text_id, skip_special_tokens=True) for text_id in generated_text_ids]
            all_decoded_texts.extend(decoded_texts)
        except FileNotFoundError:
            print(f"File not found: {input_file}")
        except Exception as e:
            print(f"An error occurred while processing {input_file}: {str(e)}")

    # Save all decoded text to a file
    with open(output_file, 'wb') as f:
        pickle.dump(all_decoded_texts, f)

    print(f"Decoded texts saved to {output_file}")

if __name__ == '__main__':
    model_name = 'EleutherAI/gpt-neo-125M'
    start_idx = 2
    end_idx = 20
    input_folder = 'dataGenaration/gpt-neo-125m'
    output_file = 'dataGenaration/result/result-gptNeo125m.pkl'
    decode_generated_text(model_name, start_idx, end_idx, input_folder, output_file)


from transformers import GPT2Tokenizer
import pickle

def create_prompts(data, prompt_length=5, tokenizer=None):
    prompts = []
    for item in data:
        if tokenizer is None:
            raise ValueError("Tokenizer must be provided")
        
        tokenized_item = tokenizer(item, add_special_tokens=False)
        tokenized_length = len(tokenized_item['input_ids'])
        
        if tokenized_length >= prompt_length:
            prompt = item[:prompt_length]
        else:
            prompt = item
        
        prompts.append((prompt, tokenized_length))
    return prompts

def main():
    data_folder = '/data'
    processData_file = f'{data_folder}/processData.pickle'
    promptSelection_file = f'{data_folder}/promptSelection.pickle'
    model_name = 'EleutherAI/gpt-neo-125m'
    
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token
    
    # Step 1: Read Data
    with open(processData_file, 'rb') as f:
        processed_data = pickle.load(f)

    # Select only the first 2 items for quick testing

    # Step 2: Create Prompts and Store Tokenized Length
    prompts = create_prompts(processed_data, 10, tokenizer)

    # Step 3: Save Prompt Data to File
    with open(promptSelection_file, 'wb') as f:
        pickle.dump(prompts, f)

    print(f"Prompt data has been saved to '{promptSelection_file}'")


if __name__ == "__main__":
    main()


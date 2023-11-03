
# Number of scripts you want to create
num_scripts=20
step=25000

for i in $(seq 1 $num_scripts); do
    start_point=$(( ($i-1) * $step ))
    end_point=$(( $i * $step ))
    file_name="gpt-neo-125m-$i.py"
    output_pickle_file="gpt-neo-125m-$i.pkl"

    # Generate the Python script
    cat > $file_name <<EOF
import torch
import pickle
from torch.utils.data import Dataset, DataLoader
from transformers import GPTNeoForCausalLM, GPT2Tokenizer

class VarrianDataset(Dataset):
    def __init__(self, input_ids, lengths):
        self.input_ids = input_ids
        self.lengths = lengths

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return self.input_ids[idx], self.lengths[idx]

class LLMsGeneration:
    def __init__(self, model, tokenizer, device, start_point, end_point):
        self.model = model
        self.tokenizer = tokenizer
        self.device = device
        self.startPoint = start_point
        self.endPoint = end_point
        self.rawDoc = None

    def loadArray(self, prompt):
        with open(prompt, 'rb') as f:
            data = pickle.load(f)[self.startPoint:self.endPoint]

        prompts, lengths = zip(*data)
        prompts = [" ".join(prompt) for prompt in prompts]

        all_input_ids = self.tokenizer(prompts, return_tensors="pt", truncation=True, padding="max_length", max_length=2048).input_ids
        all_input_ids = all_input_ids.to(self.device)

        dataset = VarrianDataset(all_input_ids, lengths)
        dataloader = DataLoader(dataset, batch_size=32, shuffle=False)

        outputs = []
        max_position_embeddings = self.model.config.max_position_embeddings
        
        for batch_input_ids, batch_lengths in dataloader:
            if batch_input_ids.shape[1] > max_position_embeddings:
                raise ValueError(f"Input IDs length ({batch_input_ids.shape[1]}) exceeds model's max position embeddings ({max_position_embeddings}).")

            max_desired_length = max(batch_lengths).item()
            total_length = batch_input_ids.shape[1] + max_desired_length

            if total_length > max_position_embeddings:
                print(f"Warning: Desired total length ({total_length}) exceeds model's max position embeddings ({max_position_embeddings}). Truncating to {max_position_embeddings}.")
                total_length = max_position_embeddings

            generated = self.model.generate(batch_input_ids,
                                            max_length=total_length,
                                            pad_token_id=self.tokenizer.pad_token_id)

            outputs.extend(generated.cpu().numpy())

        self.rawDoc = outputs

    def decode(self, data):
        return self.tokenizer.decode(data)


if __name__ == '__main__':
    # Set up start and end points, model, tokenizer, and device
    start_point = $start_point
    end_point = $end_point
    output_pickle_file = '$output_pickle_file'
    model_name = 'EleutherAI/gpt-neo-125m'
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Initialize model and tokenizer
    model = GPTNeoForCausalLM.from_pretrained(model_name).to(device)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    # Set padding token
    tokenizer.pad_token = tokenizer.eos_token

    # Initialize LLMsGeneration instance
    llms_generation = LLMsGeneration(model, tokenizer, device, start_point, end_point)
    
    # Load array and generate text
    llms_generation.loadArray('data/promptSelection.pickle')
    
    # Save the generated text
    with open(output_pickle_file, 'wb') as file:
        pickle.dump(llms_generation.rawDoc, file)

EOF

done

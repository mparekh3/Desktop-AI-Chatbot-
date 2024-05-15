from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained model tokenizer (vocabulary)
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Load pre-trained model
model = GPT2LMHeadModel.from_pretrained('gpt2')

def generate_response(user_input):
    """ Generate text given a user's input using the GPT-2 model. """
    # Encode input and add end of string token
    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    
    # Generate a response
    output_ids = model.generate(input_ids, max_length=100, num_return_sequences=1)
    
    # Decode the response
    response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    
    return response

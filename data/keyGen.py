import random
import string
import json

def generate_sequence(existing_sequences, chunk_size=16):

    """
    This function will Generate a unique sequence with as lenght: chunksize

    usage:
        chunk_size: (int=16) length of sequence
    
    returns:
        sequence
    """

    while True:
        sequence = ''.join(random.choice(string.ascii_letters) for _ in range(chunk_size))
        if sequence not in existing_sequences:
            existing_sequences.add(sequence)
            return sequence

def generate_data(characters):

    """
    This function will make our json data

    returns:
        json data
    """
        
    sequences = set()
    data = {}
    for char in characters:
        sequence = generate_sequence(sequences)
        data[char] = sequence
    
    return data

character_sets = { # json keys
    "seed": "".join(random.choice(string.digits) for _ in range(16)),  # Unique 16-digit seed
    "uppercase": string.ascii_uppercase,
    "lowercase": string.ascii_lowercase,
    "numbers": string.digits,
    "special": "!@#$%^&*()_+-=[]{};:'\"<>,./?|\\ "
}

json_data = {key: generate_data(value) if key != "seed" else value for key, value in character_sets.items()}

output_file_path = "./key.json"
with open(output_file_path, "w") as json_file: # write our json key file.
    json.dump(json_data, json_file, indent=4)

print(f"Random sequences generated and saved to '{output_file_path}'.")

import random
import string
import json

def generate_sequence(existing_sequences, chunk_size=16):
    while True:
        sequence = ''.join(random.choice(string.ascii_letters) for _ in range(chunk_size))
        if sequence not in existing_sequences:
            existing_sequences.add(sequence)
            return sequence

def generate_data(characters):
    sequences = set()
    data = {}
    for char in characters:
        sequence = generate_sequence(sequences)
        data[char] = sequence
    return data

character_sets = {
    "uppercase": string.ascii_uppercase,
    "lowercase": string.ascii_lowercase,
    "numbers": string.digits,
    "special": "!@#$%^&*()_+-=[]{};:'\"<>,./?|\\ "
}

json_data = {key: generate_data(value) for key, value in character_sets.items()}

output_file_path = "./key.json"
with open(output_file_path, "w") as json_file:
    json.dump(json_data, json_file, indent=4)

print(f"Random sequences generated and saved to '{output_file_path}'.")

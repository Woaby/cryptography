import data.utils as tool
import json

with open("key.json", "r") as json_file:
    data = json.load(json_file)

with open("output.txt", "r") as txt:
    content = txt.read()

def decrypt_chunk(chunk, mapping):
    for key, value in mapping.items():
        if chunk == value:
            return key
    return ""

def decrypt_content(content, data):
    decrypted_lines = []

    for line in content.split('\n'):
        decrypted_line = ""
        chunk_size = len(list(data['uppercase'].values())[0])
        chunks = [line[i:i + chunk_size] for i in range(0, len(line), chunk_size)]

        for chunk in chunks:
            decrypted_line += decrypt_chunk(chunk, data['uppercase'])
            decrypted_line += decrypt_chunk(chunk, data['lowercase'])
            decrypted_line += decrypt_chunk(chunk, data['numbers'])
            decrypted_line += decrypt_chunk(chunk, data['special'])

        decrypted_lines.append(decrypted_line)

    return '\n'.join(decrypted_lines)

perm = tool.getperm(content)
content_list = list(content)
tool.unshuffle(content_list, perm)
shuffled_output = ''.join(content_list)

decrypted_content = decrypt_content(shuffled_output, data)

print(decrypted_content)

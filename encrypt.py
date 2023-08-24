import data.utils as tool
import json

def encrypt_text(input_name, output_name):
    with open("key.json", "r") as json_file:
        data = json.load(json_file)

    with open(input_name, "r") as txt:
        content = txt.read()

    outp = ''

    for char in content:
        if char.isupper() and char in data["uppercase"]:
            outp += data["uppercase"][char]
        elif char.islower() and char in data["lowercase"]:
            outp += data["lowercase"][char]
        elif char.isdigit() and char in data["numbers"]:
            outp += data["numbers"][char]
        elif char in data["special"]:
            outp += data["special"][char]
        else:
            outp += char

    outp_list = list(outp)
    tool.shuffle(outp_list)
    shuffled_output = ''.join(outp_list)

    with open(output_name, "w") as output:
        output.write(shuffled_output)

    print("Data written to", output_name)

encrypt_text(input_name="input.txt", output_name="output.txt")

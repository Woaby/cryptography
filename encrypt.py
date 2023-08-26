import data.utils as tool

def encrypt_content(input_name, output_name, key_name):

    """
    This function will encrypt the content of a given txt file,

    usage:
        input_name: (string) Path to the file u want to encrypt.
        ouput_name: (string) Path where you want to save the encrypted file too.
        key_name: (string) Path to key.
    """

    content = tool.readeblecontent(input_name)
    key = tool.getkey(key_name)

    outp = ''

    for char in content:
        if char.isupper() and char in key["uppercase"]:
            outp += key["uppercase"][char]
        elif char.islower() and char in key["lowercase"]:
            outp += key["lowercase"][char]
        elif char.isdigit() and char in key["numbers"]:
            outp += key["numbers"][char]
        elif char in key["special"]:
            outp += key["special"][char]
        else:
            outp += char

    outp_list = list(outp)
    tool.shuffle(outp_list, key)
    shuffled_output = ''.join(outp_list)

    with open(output_name, "w") as output:
        output.write(shuffled_output)

    print("Data written to", output_name)

encrypt_content(input_name="input.txt", output_name="output.txt", key_name="key.json")

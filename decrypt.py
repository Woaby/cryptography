import data.utils as tool

def decrypt_content(input_name, output_name, key_name):

    """
    This function will decrypt the content of a given txt file,

    usage:
        input_name: (string) Path to the file u want to encrypt.
        ouput_name: (string) Path where you want to save the encrypted file too.
        key_name: (string) Path to key.
    """

    content = tool.readeblecontent(input_name)
    key = tool.getkey(key_name)

    perm = tool.getperm(content, key)
    content_list = list(content)
    tool.unshuffle(content_list, perm)
    shuffled_output = ''.join(content_list)

    decrypted_lines = []

    for line in shuffled_output.split('\n'):
        decrypted_line = ""
        chunk_size = len(list(key['uppercase'].values())[0])
        chunks = [line[i:i + chunk_size] for i in range(0, len(line), chunk_size)]

        for chunk in chunks:
            decrypted_line += tool.decrypt_chunk(chunk, key['uppercase'])
            decrypted_line += tool.decrypt_chunk(chunk, key['lowercase'])
            decrypted_line += tool.decrypt_chunk(chunk, key['numbers'])
            decrypted_line += tool.decrypt_chunk(chunk, key['special'])

        decrypted_lines.append(decrypted_line)

    with open(output_name, "w") as output:
        output.write('\n'.join(decrypted_lines))

decrypt_content(input_name="output.txt", output_name="input.txt", key_name="key.json")

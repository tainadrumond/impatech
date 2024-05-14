def encoder(text: str):
    a_CODE = 97
    z_CODE = 122
    encoded_text = ''
    for c in text:
        c_code = ord(c)
        parsed_char = c
        if c_code > a_CODE and c_code <= z_CODE: # checa se é uma letra minúscula entre b e z
            parsed_char = chr(c_code-1) # obtém a letra anterior
        elif c_code == a_CODE:
            parsed_char = 'z' # se a letra é 'a', atribui a letra 'z'
        encoded_text += parsed_char
    return encoded_text

print(encoder('Ola! Que tal ir ao IMPA Tech?'))
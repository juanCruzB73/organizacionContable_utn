import sys

def cesar_cipher(file_path):
    try:
        with open(file_path,'r',encoding='utf-8')as file:
            content=file.read()
        ascii_chars = ''.join(chr(i) for i in range(256))

        password=12
        deciphered_text=''

        for char in content:
            if(char in ascii_chars):
                index=ascii_chars.find(char)
                index_to_encrypt=(index-password)%256
                deciphered_text+=ascii_chars[index_to_encrypt]
            else:
                deciphered_text+=char
        with open(final_file,'w',encoding='utf-8')as file:
            file.write(deciphered_text)
        print(f"Successfully deciphered {file_path}.")

    except FileNotFoundError:
        print(f"Error: {file_path} not found.")

if __name__  == "__main__":
    if len(sys.argv)!=2:
        print("Modo de uso: python3 cecas_chifer.py <<archivo_a_convertir >>")
    else:
        final_file=input('nombre que tendra el archivo desencriptado: ')
        file_path=sys.argv[1]
        cesar_cipher(file_path)


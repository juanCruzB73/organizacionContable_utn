import sys
#ascii_chars = ''.join(chr(i) for i in range(256))
alphabet='abcdefghijklmnopqrstuvwxyz'
def cesar_cipher(file_path,password):    
    try:
        with open(file_path,'r',encoding='utf-8')as file:
            content=file.read() 
        deciphered_text=''
        for char in content:
            if(char in alphabet):
                index=alphabet.find(char)
                index_to_encrypt=(index-password)%25
                deciphered_text+=alphabet[index_to_encrypt]
            else:
                deciphered_text+=char
        print(password,") ",deciphered_text)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")

if __name__  == "__main__":
    if len(sys.argv)!=2:
        print("Modo de uso: python3 cecas_chifer.py <<archivo_a_convertir >>")
    else:
        file_path=sys.argv[1]
        for i in range(27):
            cesar_cipher(file_path,i)

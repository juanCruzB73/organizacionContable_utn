import sys
ascii_chars = ''.join(chr(i) for i in range(256))

def cesar_cipher(file_path,password):    
    try:
        with open(file_path,'r',encoding='utf-8')as file:
            content=file.read() 
        deciphered_text=password,")",''
        for char in content:
            if(char in ascii_chars):
                index=ascii_chars.find(char)
                index_to_encrypt=(index-password)%256
                deciphered_text+=ascii_chars[index_to_encrypt]
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
        for i in range(15):
            cesar_cipher(file_path,i)

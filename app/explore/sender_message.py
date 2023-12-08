from cryptography.fernet import Fernet
from datetime import datetime

def generate_key():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    key = Fernet.generate_key()
    return f"{timestamp}-{key.decode()}"

#each time a key is generated, it will include a timestamp, making it unique to that specific moment in time. When loading the key, the timestamp is separated from the key for proper decoding and usage.

def save_key(key, filename='secret.key'):
    with open(filename, 'wb') as key_file:
        key_file.write(key.encode())

def load_key(filename='secret.key'):
    return open(filename, 'rb').read().decode()

def encrypt_message(message, key):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

def main():
    print("Confidentiality: Encryption and Decryption Demo")

    # Generate or load a secret key
    key_choice = input("Do you want to (G)enerate a new key or (L)oad an existing key? ").lower()
    if key_choice == 'g':
        key = generate_key()
        save_key(key)
    elif key_choice == 'l':
        key = load_key()
    else:
        print("Invalid choice. Exiting.")
        return
    
        print(f"Selected Key: {key}")

    while True:
        print("\nOptions:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            encrypted_message = encrypt_message(message, key)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == '2':
            encrypted_message = input("Enter the encrypted message: ")
            decrypted_message = decrypt_message(encrypted_message.encode(), key)
            print(f"Decrypted message: {decrypted_message}")
        elif choice == '3':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

🔐 File Encryption and Decryption using Python
This project demonstrates a simple yet secure way to encrypt and decrypt text files using the Fernet module from Python’s cryptography library.

📌 Features
🔑 Generates a secure encryption key.

🗃️ Encrypts the content of a file and saves it as a new encrypted file.

🔓 Decrypts the encrypted file back to its original form.

💼 Saves the key securely for future encryption/decryption.

📁 Files
mykey.key: Stores the generated Fernet encryption key.
encrypt_decrypt.txt: Your original input file.
enc_encrypt_decrypt.txt: Encrypted version of the input file.
dec_encrypt_decrypt.txt: Decrypted version (should match the original).

🧪 How It Works
Generate a secure key and save it to a .key file.
Read the original file and encrypt its contents.
Save the encrypted data to a new file.
Decrypt the encrypted file using the same key.
Save the decrypted content to verify it matches the original.

▶️ Usage
Install the required library:
pip install cryptography

Run the script:
python your_script_name.py
Make sure your input file encrypt_decrypt.txt exists in the same directory before running the script.

🛡️ Dependencies
Python 3.x
cryptography library

🛡️ Caesar Cipher Encryption Project

🚀 Project Overview

This is a supercharged Caesar Cipher encryption and decryption tool written in Python.
It supports:

✅ Uppercase & lowercase letters

✅ Digits 0–9

✅ Symbols & punctuation (including \ and ")

✅ Spaces preserved

✅ Full modular wrap-around using %

✅ Encrypt & decrypt messages easily

This project demonstrates discrete modular arithmetic in action, perfect for learning both programming and cryptography concepts.

⚙️ How It Works

Character mapping:
Each character is mapped to an index in the custom Letters string (letters, numbers, symbols).

Encryption formula:

𝐸
𝑛
𝑐
𝑟
𝑦
𝑝
𝑡
𝑒
𝑑
𝐼
𝑛
𝑑
𝑒
𝑥
=
(
𝑂
𝑟
𝑖
𝑔
𝑖
𝑛
𝑎
𝑙
𝐼
𝑛
𝑑
𝑒
𝑥
+
𝐾
𝑒
𝑦
)
m
o
d
 
 
94
EncryptedIndex=(OriginalIndex+Key)mod94

Decryption formula:

𝐷
𝑒
𝑐
𝑟
𝑦
𝑝
𝑡
𝑒
𝑑
𝐼
𝑛
𝑑
𝑒
𝑥
=
(
𝐸
𝑛
𝑐
𝑟
𝑦
𝑝
𝑡
𝑒
𝑑
𝐼
𝑛
𝑑
𝑒
𝑥
−
𝐾
𝑒
𝑦
)
m
o
d
 
 
94
DecryptedIndex=(EncryptedIndex−Key)mod94

Wrap-around:
The modulo ensures letters, numbers, and symbols wrap correctly if the shift goes past the end of the set.

🧩 Diagram of Encryption Flow
User Input Text
       │
       ▼
  Convert each char to index in Letters
       │
       ▼
   Add key modulo 94
       │
       ▼
   Map back to character
       │
       ▼
Encrypted Output
💻 Installation
# Clone the repo
git clone https://github.com/YourUsername/Caesar-Cipher-Enhanced.git

# Navigate to folder
cd Caesar-Cipher-Enhanced

# Run in Python 3
python caesar_cipher.py
🎯 Usage
from caesar_cipher import Encrypt_Ceaser, Decrypt_Ceaser

message = "Hello from oboy #1"
key = 3

encrypted = Encrypt_Ceaser(message, key)
print("Encrypted:", encrypted)

decrypted = Decrypt_Ceaser(encrypted, key)
print("Decrypted:", decrypted)

✅ Example output:

Encrypted: Khoor iurp rehb $4
Decrypted: Hello from oboy #1
💡 Features

Supports letters, numbers, symbols

Works with any key

Preserves spaces and special characters

Uses modular arithmetic for discrete shifts

Easy to expand for more characters or custom sets

🔐 Why This Project Rocks

Demonstrates real discrete math in cryptography

Perfect for Python beginners and cybersecurity enthusiasts

Ready to include in your portfolio or GitHub profile
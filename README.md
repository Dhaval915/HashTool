![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)

# 🔐 HashTool

A lightweight **Python-based command-line cybersecurity tool** for generating cryptographic hashes, identifying common hash types, and validating plaintext against hashes.

Designed for cybersecurity students, beginners, and anyone interested in learning cryptographic hashing concepts.

---

## ✨ Features

### 🔹 Generate Hashes

Generate cryptographic hashes for any plaintext using:

- MD5
- SHA-1
- SHA-224
- SHA-256
- SHA-384
- SHA-512

---

### 🔹 Identify Possible Hash Types

Identify possible hash types using:

- Hash length analysis
- Known hash prefixes (bcrypt & Argon2)
- Hexadecimal format validation

Supported hash types:

- MD5
- SHA-1
- SHA-224
- SHA-256
- SHA-384
- SHA-512
- NTLM *(Possible)*
- LM *(Possible)*
- MD4 *(Possible)*
- bcrypt
- Argon2

---

### 🔹 Validate Plaintext Against Hash

Verify whether a plaintext matches a supplied hash.

The tool:

- Generates hashes for the entered plaintext
- Compares them against the supplied hash
- Displays the matching algorithm (if found)

---

### 🔹 Input Validation

- Detects empty input
- Validates hexadecimal hashes
- Supports bcrypt and Argon2 prefixes
- Handles invalid input gracefully

---

### 🔹 Graceful Exit

Supports clean program termination using:

- `Ctrl + C` (KeyboardInterrupt)
- `Ctrl + D` (Linux/macOS)
- `Ctrl + Z` then `Enter` (Windows)

---

## 📸 Preview

```text
==================================================
            HASH GENERATOR & IDENTIFIER
==================================================

[1] Generate Hash
[2] Identify Hash Type
[3] Validate Plaintext Against Hash
[4] Exit

Select :
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Dhaval915/HashTool.git
```

Go to the project directory:

```bash
cd HashTool
```

Run the program:

```bash
python hash.py
```

---

## 🖥️ Examples

### Generate Hash

```text
Enter Plaintext Value: hello

========== GENERATED HASHES ==========

MD5      : 5d41402abc4b2a76b9719d911017c592
SHA-1    : aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
SHA-224  : ea09ae9cc6768c50...
SHA-256  : 2cf24dba5fb0a30e...
SHA-384  : 59e1748777448c69...
SHA-512  : 9b71d224bd62f378...
```

---

### Identify Hash Type

```text
Enter Hash Value:
5d41402abc4b2a76b9719d911017c592

============ HASH INFORMATION ============

Hash Length   : 32
Possible Type : MD5 / NTLM / LM / MD4
```

---

### Validate Hash

```text
Enter Plaintext Value: hello

Enter Hash Value:
5d41402abc4b2a76b9719d911017c592

Status         : Match Found
Algorithm      : MD5
```

---

## 📚 Supported Hash Types

| Algorithm | Identification Method |
|-----------|-----------------------|
| MD5 | Length (32) |
| SHA-1 | Length (40) |
| SHA-224 | Length (56) |
| SHA-256 | Length (64) |
| SHA-384 | Length (96) |
| SHA-512 | Length (128) |
| NTLM | Possible (32) |
| LM | Possible (32) |
| MD4 | Possible (32) |
| bcrypt | Prefix (`$2a$`, `$2b$`, `$2y$`) |
| Argon2 | Prefix (`$argon2`) |

---

## ⚠️ Limitations

Hash validation compares a supplied plaintext against hashes generated using the supported algorithms. It does **not** perform password cracking, reverse hashing, or brute-force attacks.

---

## 📢 Disclaimer

This project is intended for **educational purposes** and to demonstrate cryptographic hashing, hash identification, and Python programming concepts. It is **not** intended for password cracking, bypassing authentication, or any unauthorized activity.

---

## 🛠️ Built With

- Python 3
- Python Standard Library
  - hashlib
  - string

---

## 🎯 Learning Objectives

This project demonstrates:

- Python functions
- Python dictionaries
- Input validation
- Exception handling
- Command-line application development
- Cryptographic hashing fundamentals
- Common hashing algorithms
- Password hashing formats
- Hash identification techniques
- Plaintext hash validation

---

## 📁 Project Structure

```
HashTool/
│
├── hash.py
├── README.md
└── LICENSE
```

---

## 🤝 Contributing

Contributions, suggestions, bug reports, and improvements are welcome.

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Dhaval Suthar**

- GitHub: https://github.com/Dhaval915
- LinkedIn: https://linkedin.com/in/thedhaval

---

⭐ **If you found this project useful, consider giving it a star!**

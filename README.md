# 🔐 Hash-Tool

A lightweight Python-based command-line tool to **generate cryptographic hashes** and **identify common hash types**. This project is designed for cybersecurity students, beginners, and anyone interested in learning about hashing algorithms.

---

## ✨ Features

### 🔹 Hash Generator
Generate hashes for a given plaintext using:

- MD5
- SHA-1
- SHA-224
- SHA-256
- SHA-384
- SHA-512

### 🔹 Hash Identifier
Identify possible hash types based on:

- Hash length
- Hash prefix (bcrypt & Argon2)
- Hexadecimal validation

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

## 📸 Preview

```text
========================================
      HASH GENERATOR & IDENTIFIER
========================================

1. Generate Hash
2. Identify Hash Type
3. Exit
Select :
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Dhaval915/Hash-Tool.git
```

Go to the project directory:

```bash
cd Hash-Tool
```

Run the program:

```bash
python hash.py
```

---

## 🖥️ Example

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

### Identify Hash

```text
Enter Hash Value:
5d41402abc4b2a76b9719d911017c592

============ HASH INFORMATION ============

Hash Length        : 32
Possible Hash Type : MD5 / NTLM / LM / MD4
```

---

## 📚 Hash Types

| Algorithm | Length |
|-----------|--------|
| MD5 | 32 |
| SHA-1 | 40 |
| SHA-224 | 56 |
| SHA-256 | 64 |
| SHA-384 | 96 |
| SHA-512 | 128 |
| bcrypt | Prefix: `$2a$`, `$2b$`, `$2y$` |
| Argon2 | Prefix: `$argon2` |

---

## ⚠️ Note

Hash identification is based on:

- Hash length
- Known prefixes
- Input format

Some algorithms (such as **MD5**, **NTLM**, **LM**, and **MD4**) produce hashes of the same length, so the exact algorithm cannot always be determined from the hash value alone.

---

## 🛠️ Built With

- Python 3
- hashlib
- string

---

## 🎯 Learning Objectives

This project helps you understand:

- Cryptographic hashing
- Common hashing algorithms
- Password hashing formats
- Hash identification techniques
- Python programming fundamentals

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed by **Dhaval Suthar**

⭐ If you found this project useful, consider giving it a star!

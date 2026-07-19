import hashlib
import string
import os

WIDTH = 50
TITLE = "HASH GENERATOR & IDENTIFIER"

print()
print("=" * WIDTH)
print(TITLE.center(WIDTH))
print("=" * WIDTH)

HASH_ALGORITHMS = {
    "MD5": hashlib.md5,
    "SHA-1": hashlib.sha1,
    "SHA-224": hashlib.sha224,
    "SHA-256": hashlib.sha256,
    "SHA-384": hashlib.sha384,
    "SHA-512": hashlib.sha512
}
HASH_TYPES = {
    32: "MD5 / NTLM / LM / MD4",
    40: "SHA-1",
    56: "SHA-224",
    64: "SHA-256",
    96: "SHA-384",
    128: "SHA-512"
}

def again(msg):
    while True:
        check = input(msg).strip().lower()

        if check == "y":
            return True

        elif check == "n":
            return False

        else:
            print("Please enter y or n.")

# section 1 --> generate the hash from user input
def generate():
    while True:
        plaintext = input("\nEnter Plaintext Value (or type 'exit'): ").strip()
        if not plaintext:
            print("Please enter a plaintext value.")
            print("Type 'exit' to return to the main menu.")
            continue
        if plaintext.lower() == "exit":
            return
        plaintext = plaintext.encode()
        hashes = {}

        for name, algo in HASH_ALGORITHMS.items():
            hashes[name] = algo(plaintext).hexdigest()

        print("\n========== GENERATED HASHES ==========")

        for name, value in hashes.items():
            print(f"{name:<8}: {value}")

        if not again("Generate another hash? (y/n): "):
            return

# Section 2 --> Identify the possible hash type
def identify():
    while True:
        hash_value = input("\nEnter Hash Value (or type 'exit'): ").strip()
        if not hash_value:
            print("Please enter a hash value.")
            print("Type 'exit' to return to the main menu.")
            continue
        if hash_value.lower() == "exit":
            return

        if not hash_value.startswith(("$2a$", "$2b$", "$2y$", "$argon2")):
            if not all(c in string.hexdigits for c in hash_value):
                print("Invalid hash format.")
                print("Only hexadecimal, bcrypt, or Argon2 hashes are supported.")
                print("Type 'exit' to return to the main menu.")
                continue

        # bcrypt hashes start with "$2a$", "$2b$", or "$2y$"
        # Used for secure password hashing (slow, salted, resistant to brute-force attacks)
        if hash_value.startswith(("$2a$", "$2b$", "$2y$")):
            print("\nPossible Hash Type : bcrypt")

        # Argon2 hashes start with "$argon2"
        # Modern password hashing algorithm (uses memory, time, and parallelism for strong security)
        elif hash_value.startswith("$argon2"):
            print("\nPossible Hash Type : Argon2")

        else:
            length = len(hash_value)

            if length in HASH_TYPES:
                print("\n============ HASH INFORMATION ============")
                print(f"Hash Length        : {length}")
                print(f"Possible Type      : {HASH_TYPES[length]}")
            else:
                print("Unknown or unsupported hash format.")

        if not again("Check another hash? (y/n): "):
            break

# Section 3 --> Validate plaintext against a hash
def validate():
    while True:
        plaintext = input("\nEnter Plaintext Value (or type 'exit'): ").strip()

        if not plaintext:
            print("Please enter a plaintext value.")
            print("Type 'exit' to return to the main menu.")
            continue

        if plaintext.lower() == "exit":
            break

        input_hash = input("Enter Hash Value (or type 'exit'): ").strip()

        if not input_hash:
            print("Please enter a hash value.")
            print("Type 'exit' to return to the main menu.")
            continue
        elif input_hash.lower() == "exit":
            return

        plaintext = plaintext.encode()
        hashes = {}
        for name, algo in HASH_ALGORITHMS.items():
            hashes[name] = algo(plaintext).hexdigest()

        # found = False
        for name, value in hashes.items():
            if value.lower() == input_hash.lower():
                print("\nStatus         : Match Found")
                print(f"Algorithm      : {name}")
                # print("\nMatch Found")
                # print("Hash Algorithm :", name)
                # found = True
                break

        else:
            print("\nHash does not match the plaintext.")

        if not again("Validate another hash? (y/n): "):
            break
            # if Md5 == hash_byuser or SHA1 == hash_byuser or SHA224 == hash_byuser or SHA256 == hash_byuser or SHA384 == hash_byuser or SHA512 ==hash_byuser:
            #     print("")
            
# Section 4 --> Calculate file hashes for integrity verification
def file_check():
    while True:
        path = input("\nEnter File Path (or type 'exit'): ").strip()

        if not path:
            print("Please enter a file path.")
            print("Type 'exit' to return to the main menu.")
            continue

        if path.lower() == "exit":
            return

        if not os.path.isfile(path):
            print("File not found. Please check the file path and try again.")
            continue

        with open(path, "rb") as file:
            data = file.read()  #reads every byte from the file.
            # - Suppose the file contains  -->  Hello World
            # - Internally it becomes bytes  -->  b'Hello World'

            print("\n========== FILE HASHES ==========")

            for name, algo in HASH_ALGORITHMS.items():
                print(f"{name:<8}: {algo(data).hexdigest()}")
                # algo(data) --> hashlib.md5(data)  -->  hashlib.md5(b"Hello World")   --->  .hexdigest() --->  b10a8db164e0754105b7a99be72e3fe5

            # sha256 = hashlib.sha256(data).hexdigest()
            # print("SHA-256 :", sha256)
        if not again("Check another file? (y/n): "):
            break

try:
    while True:
        sel = input(
            "\n[1] Generate Hash"
            "\n[2] Identify Hash Type"
            "\n[3] Validate Plaintext Against Hash"
            "\n[4] Check File"
            "\n[5] Exit"
            "\nSelect : "
        ).strip()

        if sel == "1":
            generate()
        elif sel == "2":
            identify()
        elif sel == "3":
            validate()
        elif sel == "4":
            file_check()
        elif sel == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid Selection")
# User interrupts the program --> Ctrl+C in linux/win
# EOFError input() reaches the end of input (no more data) Ctrl+Z, then Enter | Ctrl+D
except (KeyboardInterrupt, EOFError):
    print("\nThank you for using HashTool!")
    print("Goodbye!")
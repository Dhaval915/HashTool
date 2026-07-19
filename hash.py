import hashlib
import string

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

def generate():
        while True:
            plaintext = input("\nEnter Plaintext Value: ").strip()
            if not plaintext:
                print("Please enter a plaintext value.\n- Write exit to exit.")
                continue
            if plaintext.lower() == "exit":
                return None
            plaintext = plaintext.encode()
            hashes = {}

            for name, algo in HASH_ALGORITHMS.items():
                hashes[name] = algo(plaintext).hexdigest()

            print("\n========== GENERATED HASHES ==========")

            for name, value in hashes.items():
                print(f"{name:<8}: {value}")

            if not again("Generate another hash? (y/n): "):
                return

def identify():
    while True:
        hash_value = input("\nEnter Hash value: ").strip()
        if not hash_value:
            print("Please enter a hash value.\n Write exit to exit.")
            continue
        if hash_value.lower() == "exit":
            return

        if not hash_value.startswith(("$2a$", "$2b$", "$2y$", "$argon2")):
            if not all(c in string.hexdigits for c in hash_value):
                print("Invalid hash format.\nOnly hexadecimal hashes or bcrypt/Argon2 hashes are supported.\nWrite exit to exit.")
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

def validate():
    while True:
        plaintext = input("\nEnter Plaintext Value: ").strip()

        if not plaintext:
            print("Please enter a plaintext value.\n- Write exit to exit.")
            continue

        if plaintext.lower() == "exit":
            break

        input_hash = input("Enter HASH Value: ").strip()

        if not input_hash:
            print("Please enter a hash value.\n- Write exit to exit.")
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

        if not again("Check another hash? (y/n): "):
            break
            # if Md5 == hash_byuser or SHA1 == hash_byuser or SHA224 == hash_byuser or SHA256 == hash_byuser or SHA384 == hash_byuser or SHA512 ==hash_byuser:
            #     print("")


try:
    while True:
        sel = input(
            "\n[1] Generate Hash"
            "\n[2] Identify Hash Type"
            "\n[3] Validate Plaintext Against Hash"
            "\n[4] Exit"
            "\nSelect : "
        ).strip()

        if sel == "1":
            generate()
        elif sel == "2":
            identify()
        elif sel == "3":
            validate()
        elif sel == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid Selection")
# User interrupts the program --> Ctrl+C in linux/win
# EOFError input() reaches the end of input (no more data) Ctrl+Z, then Enter | Ctrl+D
except (KeyboardInterrupt, EOFError):
    print("\n\nGoodbye!")
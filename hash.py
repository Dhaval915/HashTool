import hashlib
import string

print("""
========================================
      HASH GENERATOR & IDENTIFIER
========================================
""")
while True:

    sel = input("\n1. Generate Hash\n2. Identify Hash Type\n3. Exit\nSelect : ").strip()
    exit_hash = False
    if sel == "1":
        while True:
            take = input("\nEnter Plaintext Value: ").strip()
            if take == "":
                print("Please enter a plaintext value.\n- Write exit to exit.")
                continue
            if take.lower() == "exit":
                break
            take = take.encode()
            print("\n========== GENERATED HASHES ==========")
            print("MD5     :", hashlib.md5(take).hexdigest())
            print("SHA-1   :", hashlib.sha1(take).hexdigest())
            print("SHA-224 :", hashlib.sha224(take).hexdigest())
            print("SHA-256 :", hashlib.sha256(take).hexdigest())
            print("SHA-384 :", hashlib.sha384(take).hexdigest())
            print("SHA-512 :", hashlib.sha512(take).hexdigest())

            while True:
                check = input("Generate another hash? (y/n): ").strip().lower()

                if check == "y":
                    break

                elif check == "n":
                    exit_hash = True
                    break

                else:
                    print("Please enter y or n.")

            if exit_hash:
                break

    elif sel == "2":
        exit_hash = False
        while True:
            hash_value = input("\nEnter Hash value: ").strip()
            if hash_value == "":
                print("Please enter a hash value.\n Write exit to exit.")
                continue
            if hash_value.lower() == "exit":
                break

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

                hash_types  = {
                    32: "MD5 / NTLM / LM / MD4",
                    40: "SHA-1",
                    56: "SHA-224",
                    64: "SHA-256",
                    96: "SHA-384",
                    128: "SHA-512"
                }

                if length in hash_types:
                    print("============ HASH INFORMATION ============")
                    print("Hash Length          : ", length)
                    print("Possible Hash Type   : ", hash_types[length])
                else:
                    print("Unknown Hash")

            while True:
                check = input("\nCheck another hash? (y/n): ").strip().lower()

                if check == "y":
                    break

                elif check == "n":
                    exit_hash = True
                    break

                else:
                    print("Please enter y or n.")

            if exit_hash:
                break
    elif sel == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Selection")
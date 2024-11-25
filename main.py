import hashlib

def converted_text_to_sha1(text):
    digest = hashlib.sha1(text.encode()).hexdigest()
    return digest

def main():
    user_sha1 = input("Enter the SHA1 to crack: ")
    cleaned_user_sha1 = user_sha1.strip().lower()

    # Open the file and iterate over each password
    with open('passwords.txt', 'r') as f:
        for line in f:
            password = line.strip()
            converted_sha1 = converted_text_to_sha1(password)

            if cleaned_user_sha1 == converted_sha1:
                print(f"Password Found: {password}")
                return

    print("Could not find the password.")

if __name__ == '__main__':
    main()

import hashlib
def convert(text):
    digest = hashlib.sha1(
        text.encode()
    ).hexdigest()
    return digest
def main():
    user_sha1 = input("Enter the SHA1 to Crack: ")
    cleaned_user_sha1 = user_sha1.strip().lower()

    with open('password.txt') as f:
        for line in f:
            password = line.strip()
            converted = convert(password)

            if cleaned_user_sha1 == converted:
                print(f"Password: {password}")
                return
        
    print("Could not find a password match")
if __name__ == '__main__':

    main()

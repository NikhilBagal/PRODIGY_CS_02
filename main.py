def get_Input():
    print("Do you want to encrypt ot decrypt image: /n")
    operation = input("E/D: ")
    if operation.upper() == "E":
        path = input("Please enter the Image path: ")
        key = int(input("Please enter the Key: "))
        encryption(path, key)
    elif operation.upper() == "D":
        path = input("Please enter the Image path: ")
        key = int(input("Please enter the Key: "))
        decryption(path, key)
    else:
        print("Oops something went wrong Try again")

def encryption(path, key):
    fin = open(path, 'rb')
    image = fin.read()
    fin.close()
    image = bytearray(image)

    for index, values in enumerate(image):
        image[index] = values ^ key

    fin = open(path, 'wb')

    fin.write(image)
    fin.close()
    print("Encryption Done...")

def decryption(path, key):
    fin = open(path, 'rb')

    image = fin.read()
    fin.close()

    image = bytearray(image)

    for index, values in enumerate(image):
        image[index] = values ^ key

    fin = open(path, 'wb')
    fin.write(image)
    fin.close()
    print("Decryption Done...")

get_Input()
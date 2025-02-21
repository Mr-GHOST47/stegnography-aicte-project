import cv2

def decrypt_image(image_path):
    """Decrypts a hidden message from an image."""
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found.")
        return
    
    try:
        with open("password.txt", "r") as f:
            stored_password = f.read().strip()
    except FileNotFoundError:
        print("Error: Password file not found.")
        return

    password = input("Enter passcode for decryption: ")
    if password != stored_password:
        print("YOU ARE NOT AUTHORIZED")
        return
    
    n, m, z = 0, 0, 0  
    decrypted_message = ""

    while True:
        char_value = int(img[n, m, z])  
        if char_value == 0:  
            break

        decrypted_char = chr(char_value)
        if decrypted_message.endswith("###"):
            break  # Stop at delimiter

        decrypted_message += decrypted_char
        
        z = (z + 1) % 3  
        if z == 0:
            m += 1
            if m == img.shape[1]:  
                m = 0
                n += 1

    decrypted_message = decrypted_message.replace("###", "")  
    print("Decrypted Message:", decrypted_message)


if __name__ == "__main__":
    image_path = input("Enter encrypted image path: ")
    decrypt_image(image_path)

import cv2
import os

def encrypt_image(image_path, message, password, output_path="encryptedImage.png"):
    """Encrypts a message into an image using ASCII values."""
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found.")
        return
    
    message += "###"  

    height, width, _ = img.shape
    n, m, z = 0, 0, 0  

    for char in message:
        if n < height and m < width:
            img[n, m, z] = ord(char)  
            z = (z + 1) % 3  
            if z == 0:
                m += 1
                if m == width:
                    m = 0
                    n += 1
        else:
            print("Error: Message is too long for this image.")
            return

    cv2.imwrite(output_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 0])  
    os.system(f"start {output_path}")  # Open encrypted image (Windows)
    print(f"Message encrypted successfully into {output_path}")
    
    # Store password
    with open("password.txt", "w") as f:
        f.write(password)


if __name__ == "__main__":
    image_path = input("Enter image path: ")
    message = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    
    encrypt_image(image_path, message, password)

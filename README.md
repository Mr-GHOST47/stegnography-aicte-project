# stegnography-aicte-project
# Steganography with OpenCV

This project implements **steganography**, the technique of hiding secret messages inside images, using **Python** and **OpenCV**.

## 📌 Features

- **Encrypt messages** into an image by modifying pixel values.
- **Decrypt messages** from an image with a password.
- Uses **PNG format** for accuracy (JPEG is avoided due to compression issues).

## 🛠️ Technologies Used

- **Python** → Main programming language
- **OpenCV (**``**)** → Image processing
- **NumPy** → Handling pixel values
- **File Handling (**``**)** → Password storage & file operations

---

## 🚀 Installation

### 1️⃣ **Clone the Repository**

```bash
git clone https://github.com/your-username/steganography-opencv.git
cd steganography-opencv
```

### 2️⃣ **Install Dependencies**

Make sure you have Python installed, then run:

```bash
pip install opencv-python
```

---

## 🔒 Encryption (Hiding the Message)

### Run `encrypt.py` to hide a secret message in an image:

```bash
python encrypt.py
```

**Example Usage:**

- Enter the image path (e.g., `image.png`).
- Input your secret message.
- Set a password.
- The encrypted image (`encryptedImage.png`) will be generated.

---

## 🔓 Decryption (Revealing the Message)

### Run `decrypt.py` to extract the hidden message:

```bash
python decrypt.py
```

**Example Usage:**

- Enter the path to the encrypted image.
- Enter the correct password.
- The hidden message will be displayed.

---

## 📝 Notes

- **Use PNG format** for accuracy (JPEG may alter pixels due to compression).
- Ensure the image has **enough pixels** to store the message.
- The decryption will fail if the wrong password is entered.

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 🤝 Contributing

Feel free to submit issues or pull requests to improve the project!

### **💡 Created by Dheeraj Sharma**


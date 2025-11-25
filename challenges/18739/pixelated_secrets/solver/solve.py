import re
import numpy as np
from PIL import Image


DOUBLE_STEG_IMAGE = "/content/drive/MyDrive/Colab Notebooks/CTF_Challenge_Dev/ctf_challenge_image(13).jpg"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n" #magic byte string
OUTPUT_PNG = "extracted_second_layer.png"
OUTPUT_TEXT = "recovered_hidden.txt"


# checks for jpg by reading magic byte header of file
def validate_jpeg(path):
    with open(path, "rb") as f:
        header = f.read(2)

# finds the png image that is appended at the bottom of challenge image
def extract_appended_png(path):
    with open(path, "rb") as f:
        data = f.read()

    # looks for the magic bytes
    idx = data.find(PNG_MAGIC)
    if idx == -1:
        raise ValueError("PNG magic bytes not found!")
    png_bytes = data[idx:]

    with open(OUTPUT_PNG, "wb") as f:
        f.write(png_bytes)
    return OUTPUT_PNG

# from the png image, it extracts the lsb from the pixels 
def extract_lsb(png_path):
    img = Image.open(png_path).convert("RGB")
    arr = np.array(img)
    flat = arr.flatten()

    # Read first 32 bits = payload length
    length_bits = flat[:32] & 1
    length = int("".join(str(b) for b in length_bits), 2)


    # Extract payload bits
    payload_bits = flat[32:32 + length * 8] & 1

    # Convert bits to bytes
    out = bytearray()
    for i in range(0, len(payload_bits), 8):
        byte = 0
        for bit in payload_bits[i:i+8]:
            byte = (byte << 1) | int(bit)
        out.append(byte)

    # Save text file
    with open(OUTPUT_TEXT, "wb") as f:
        f.write(out)

    # reads the contexts of the text file
    try:
        print(out[:200].decode(errors="replace"))
    except:
        print(out[:200])

validate_jpeg(DOUBLE_STEG_IMAGE)

extracted_png = extract_appended_png(DOUBLE_STEG_IMAGE)

extract_lsb(extracted_png)


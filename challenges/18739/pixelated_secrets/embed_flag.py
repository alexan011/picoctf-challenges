import os
import numpy as np
from PIL import Image

# 1st level of steg by using lsb steg for text file in inner image
def embed_lsb(cover_path, text_path, out_path):
    img = Image.open(cover_path).convert("RGB")
    arr = np.array(img)
    flat = arr.flatten()

    payload = open(text_path, "rb").read()
    payload_len = len(payload)

    length_bits = [int(b) for b in f"{payload_len:032b}"]

    payload_bits = []
    for byte in payload:
        payload_bits.extend([int(b) for b in f"{byte:08b}"])

    bitstream = length_bits + payload_bits

    for i, bit in enumerate(bitstream):
        flat[i] = (flat[i] & 0b11111110) | bit

    stego_arr = flat.reshape(arr.shape)
    Image.fromarray(stego_arr).save(out_path)

# does 2nd level steg which is appending lsb steg image to cover/outer image
def append_image(base_path, hidden_path, out_path):
    MARKER = b"\n-----Ah-ha you are on to something-----\n"

    with open(base_path, "rb") as f:
        main_bytes = f.read()

    with open(hidden_path, "rb") as f:
        hidden_bytes = f.read()

    combined = main_bytes + MARKER + hidden_bytes

    with open(out_path, "wb") as f:
        f.write(combined)


def main():
    cover = "/challenge/dreamcore.jpg" # before lsb steg
    text = "/challenge/working/hidden_with_flag.txt" 
    outer = "/challenge/challenge_image.png"           # outer image which is what the users will see (not stegged)
    stego_png = "/challenge/working/stego.png"  #intermed lsb steg image-1st level
    final_img = "/challenge/working/ctf_challenge_image.jpg" #image the players will see that is stegged

    embed_lsb(cover, text, stego_png)
    append_image(outer, stego_png, final_img)

if __name__ == "__main__":
    main()

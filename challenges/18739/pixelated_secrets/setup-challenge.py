import os
import json

def main():
    flag = os.environ.get("FLAG", "i_l0v3_st3g0!")

    rand_val = flag.replace("flag{", "").replace("}", "") 
    flag = f"i_l0v3_st3g!_{rand_val}"

    os.makedirs("/challenge/working", exist_ok=True)

    base_path = "/challenge/hidden.txt"
    out_path = "/challenge/working/hidden_with_flag.txt"


    with open(base_path, "r") as f:
        base = f.read()

    with open(out_path, "w") as f:
        f.write(base + "\nFLAG: " + flag)

    os.system("python3 /challenge/embed_flag.py")

    os.system(
        "tar czvf /challenge/artifacts.tar.gz -C /challenge/working ctf_challenge_image.jpg"
    )

    with open("/challenge/metadata.json", "w") as f:
        f.write(json.dumps({"flag": flag}))

if __name__ == "__main__":
    main()

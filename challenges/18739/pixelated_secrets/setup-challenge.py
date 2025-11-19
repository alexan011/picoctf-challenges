import os
import json

def main():
    # During docker build, FLAG may not be set
    flag_env = os.environ.get("FLAG", "picoCTF{placeholder_flag_for_build}")

    # Write the flag to /challenge/flag
    with open("/challenge/flag", "w") as f:
        f.write(flag_env)

    # Write metadata.json
    metadata = {
        "flag": flag_env
    }

    with open("/challenge/metadata.json", "w") as f:
        f.write(json.dumps(metadata))

if __name__ == "__main__":
    main()


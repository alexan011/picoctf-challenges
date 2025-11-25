FROM python:3.11-slim

ARG FLAG="picoCTF{I_l0v3_st3g0!}"
ENV FLAG=$FLAG

RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install pillow numpy

RUN mkdir -p /challenge /challenge/working
WORKDIR /challenge


COPY dreamcore.jpg /challenge/
COPY challenge_image.png /challenge/
COPY hidden.txt /challenge/


COPY embed_flag.py /challenge/
COPY setup-challenge.py /challenge/

# creates steg image
RUN python3 /challenge/setup-challenge.py

# embedded ctf image with the double steg for players to download
RUN tar czvf /challenge/artifacts.tar.gz -C /challenge/working ctf_challenge_image.jpg

CMD ["tail", "-f", "/dev/null"]

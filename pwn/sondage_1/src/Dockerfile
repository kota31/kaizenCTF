FROM ubuntu:latest

# update the machine and install gcc
RUN apt update && apt upgrade -y && apt install -y gcc gcc-multilib socat 

#RUN addgroup -S kaizen && adduser -S kaizen -G kaizen

#USER root
WORKDIR "/tmp"

# Chall compilation
COPY sondage /tmp/pwn1

# RUN chall
CMD socat TCP-LISTEN:5555,bind=0.0.0.0,fork,reuseaddr SYSTEM:'/tmp/pwn1'
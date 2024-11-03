#FROM ubuntu:latest
FROM ubuntu@sha256:8a37d68f4f73ebf3d4efafbcf66379bf3728902a8038616808f04e34a9ab63ee

# update the machine and install gcc
RUN apt update && apt upgrade -y && apt install -y gcc gcc-multilib socat 


# add user kaizen
RUN groupadd kaizen && useradd -g kaizen kaizen

WORKDIR "/tmp"

COPY sondage /tmp/pwn2

# add flag
RUN echo "KZS{Le_Pwn_Cest_Pas_Si_Facile_:P}" > flag.txt

USER kaizen

EXPOSE 5556

# RUN chall
CMD socat TCP-LISTEN:5556,bind=0.0.0.0,fork,reuseaddr SYSTEM:'/tmp/pwn2'
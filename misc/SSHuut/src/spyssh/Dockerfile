FROM debian:latest
RUN apt-get update && apt install openssh-server sudo -y && apt install nano -y
RUN apt-get install strace -y

# creation utilisateur pour le challenge
#RUN groupadd -g 1234 challenger
RUN useradd -M -s /bin/bash kaizen
RUN echo 'kaizen ALL=(ALL) /usr/bin/strace' >> /etc/sudoers
RUN echo 'kaizen:K41Z3N' | chpasswd

# creation compte monkey pour le flag
RUN useradd -rm -d /home/john -s /bin/bash -g root -G sudo -u 777 john                    
RUN echo 'john:KZS{y0U_4r3_3v1L_:0}' | chpasswd

# running ssh
RUN service ssh start
EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]

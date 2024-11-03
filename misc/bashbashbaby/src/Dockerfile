# Image avec JAVA installé par défaut
FROM openjdk:24-slim-bullseye
WORKDIR "/tmp"

# Installer les paquets nécessaires
RUN apt-get update && apt-get install -y openssh-server && apt-get install sudo

# Plus court pour écrire la commande
RUN cp /usr/local/openjdk-24/bin/java /bin/java

# Créer un utilisateur "kaizen" => pas home comme ça pas de poisoning dans le bashrc possible 
RUN useradd -M -s /bin/bash kaizen && echo "kaizen:K41Z3N" | chpasswd

# Création des comptes  kaizen-cracked et kaizen-cracked-master
RUN useradd -m -s /bin/bash kaizen-cracked && echo "kaizen-cracked:b60f17ff-b075-4eed-8fa4-ddd84f778998" | chpasswd
RUN useradd -m -s /bin/bash kaizen-cracked-master && echo "kaizen-cracked-master:7301543d-18be-44f7-a0d0-b32d8f60ff8a" | chpasswd

# Création du flag (own par kaizen-cracked-master mais droit lecture pour le groupe kaizen-cracked)
RUN echo "KZS{2e910bcd10123bc886f4185dbd5ae66d}" > /tmp/flag.txt && chown kaizen-cracked-master:kaizen-cracked /tmp/flag.txt && chmod 440 /tmp/flag.txt

# Importer la conf sudoers
COPY files/sudoers /etc/sudoers

# Copier le code java + compilation + nettoyage
COPY files/SecureFind.java /tmp/SecureFind.java
RUN /usr/local/openjdk-24/bin/javac SecureFind.java && \
    /usr/local/openjdk-24/bin/jar cvfe SecureFind.jar SecureFind SecureFind.class && \
    rm -f SecureFind.java SecureFind.class


# Trick pour éviter d'avoir un historique infini pour kaizen-cracked
RUN echo 'export HISTCONTROL=ignorespace' > /home/kaizen-cracked/.bashrc

# Ajouter l'historique bash pour root
COPY files/bash_history /home/kaizen-cracked/.bash_history

# Pour que le serveur ssh tourne
RUN mkdir /var/run/sshd
EXPOSE 22

# Lancer le service SSH
CMD ["/usr/sbin/sshd", "-D"]

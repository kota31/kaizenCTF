# Sondage 2

## Objectif du challenge

Le but de ce challenge est de contourner les protections NX et ASLR via la technique ret2libc.

## Compilation

```sh
gcc pwn2.c -o pwn2 -no-pie -fno-stack-protector -m32
```

## Résolution

* Step 1 :
Le premier buffer overflow consiste à remplacer une valeur présente sur la stack afin de pouvoir atteindre la fonction leak().
Cette dernière va pouvoir nous donner l'addresse actuelle de la libC et ainsi rendre inutile ASLR.

* Step 2 :
La stack étant NX on peut utiliser ret2libc pour exécuter la fonction system depuis la libc. Pour cela il va être nécessaire de connaitre les bons offets de la libc (elle sera donnée en pièce jointe pour cela).

* Step 3 :
Il faut ensuite automatiser le tout avec pwntool par exemple (voir exploit.py)




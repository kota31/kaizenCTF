FROM node:slim

RUN useradd -M -s /bin/bash kaizen

WORKDIR /express-challenge

COPY server/ .

RUN npm install

USER kaizen

ENV FLAG=KZS{1_LOVE_w3B_H4ck1nG!}

CMD ["node","/express-challenge/server.js"]

EXPOSE 5001
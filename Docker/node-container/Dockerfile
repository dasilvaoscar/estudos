FROM node

ENV PORT=8080

WORKDIR /app
COPY package.json .

RUN npm install --production

COPY . .

EXPOSE 8080

CMD ["node", "index.js"]
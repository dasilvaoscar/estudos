FROM node:20-alpine

WORKDIR /app

COPY node-service/package.json ./
RUN npm install --omit=dev

COPY node-service/server.js ./
COPY proto/ ./proto/

EXPOSE 3000
CMD ["node", "server.js"]

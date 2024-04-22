FROM denoland/deno:alpine

EXPOSE 8000

WORKDIR /app

USER deno

COPY server.ts .

COPY . .
RUN deno cache server.ts

CMD ["run", "-A", "server.ts"]
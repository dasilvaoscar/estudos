FROM golang:1.23-bookworm AS build

RUN apt-get update && apt-get install -y protobuf-compiler && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.35.2 && \
    go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.5.1
ENV PATH="/go/bin:${PATH}"

COPY go-service/go.mod ./
COPY proto/ ./proto/
RUN protoc --go_out=. --go_opt=module=grpc-poc \
    --go-grpc_out=. --go-grpc_opt=module=grpc-poc \
    proto/greeter.proto

COPY go-service/main.go ./
RUN go mod tidy
RUN CGO_ENABLED=0 go build -o /server .

FROM gcr.io/distroless/static-debian12
COPY --from=build /server /server
EXPOSE 50051
ENTRYPOINT ["/server"]

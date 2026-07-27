package main

import (
	"context"
	"log"
	"net"
	"os"

	pb "grpc-poc/proto/greeter"

	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"
)

type server struct {
	pb.UnimplementedGreeterServer
}

func (s *server) SayHello(ctx context.Context, req *pb.HelloRequest) (*pb.HelloReply, error) {
	log.Printf("Recebido SayHello para: %q", req.GetName())
	return &pb.HelloReply{
		Message:  "Olá, " + req.GetName() + "!",
		ServedBy: "go-service (gRPC server)",
	}, nil
}

func main() {
	port := os.Getenv("GRPC_PORT")
	if port == "" {
		port = "50051"
	}

	lis, err := net.Listen("tcp", ":"+port)
	if err != nil {
		log.Fatalf("falha ao escutar: %v", err)
	}

	s := grpc.NewServer()
	pb.RegisterGreeterServer(s, &server{})
	reflection.Register(s)

	log.Printf("Servidor gRPC ouvindo em :%s", port)
	if err := s.Serve(lis); err != nil {
		log.Fatalf("falha ao servir: %v", err)
	}
}

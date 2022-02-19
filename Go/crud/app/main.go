package main

import "net/http"

func JsonResponse(response string) []byte {
	return []byte(response)
}

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write(JsonResponse(`{"message": "hello world"}`))
	})
	http.ListenAndServe(":8080", nil)
}

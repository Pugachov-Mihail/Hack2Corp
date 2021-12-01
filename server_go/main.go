package main

import (
	"log"
	"net/http"
)

func home(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/" {
		http.NotFound(w, r)
		return
	} else {
		w.Write([]byte("<h1><a href='about/'>Привет мир</a></h1>"))
	}
}

func about(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/about/" {
		http.NotFound(w, r)
		return
	} else {
		w.Write([]byte("<h1>Привет о нас</h1>"))
	}
}

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/", home)
	mux.HandleFunc("/about/", about)
	log.Println("HEllo")
	err := http.ListenAndServe(":4000", mux)
	log.Fatal(err)
}

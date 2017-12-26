package main

import (
	"errors"
	"fmt"
	"net/http"
	"strconv"
)

func main() {
	http.HandleFunc("/add", Add)
	http.HandleFunc("/subtract", Subtract)
	http.HandleFunc("/multiply", Multiply)
	http.HandleFunc("/divide", Divide)
	fmt.Println("listening...")
	err := http.ListenAndServe(":3002", nil)
	if err != nil {
		panic(err)
	}
}

func Add(res http.ResponseWriter, req *http.Request) {
	a, b, err := ParseArgs(req)
	if err != nil {
		RespondError(res, err.Error())
		return
	}
	result := a + b;
	RespondResult(res, result)
}

func Subtract(res http.ResponseWriter, req *http.Request) {
	op1, op2, err := ParseArgs(req)
	if err != nil {
		RespondError(res, err.Error())
		return
	}
	result := op1 - op2;
	RespondResult(res, result)
}

func Multiply(res http.ResponseWriter, req *http.Request) {
	a, b, err := ParseArgs(req)
	if err != nil {
		RespondError(res, err.Error())
		return
	}
	result := a * b;
	RespondResult(res, result)
}

func Divide(res http.ResponseWriter, req *http.Request) {
	a, b, err := ParseArgs(req)
	if err != nil {
		RespondError(res, err.Error())
		return
	}
	result := a / b;
	RespondResult(res, result)
}

func ParseArgs (req *http.Request) (float64, float64, error) {
	op1, err := strconv.ParseFloat(req.FormValue("op1"), 64)
	if err != nil {
		return 0, 0, errors.New("bad first argument: " + req.FormValue("op1"))
	}
	op2, err := strconv.ParseFloat(req.FormValue("op2"), 64)
	if err != nil {
		return 0, 0, errors.New("bad second argument: " + req.FormValue("op2"))
	}
	return op1, op2, nil
}

func RespondError (res http.ResponseWriter, message string) {
	res.Header().Set("Access-Control-Allow-Origin", "*")
	res.Header().Set("Content-Type", "text/plain")
	res.WriteHeader(http.StatusBadRequest)
	fmt.Fprintln(res, message)
}

func RespondResult (res http.ResponseWriter, result float64) {
	res.Header().Set("Access-Control-Allow-Origin", "*")
	res.Header().Set("Content-Type", "text/plain")
	res.WriteHeader(http.StatusOK)
	fmt.Fprintln(res, result)
}

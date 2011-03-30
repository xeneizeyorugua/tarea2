#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Imprime los n primeros números de la serie de Fibonacci 
# el cual se recibe como parámetro

def fibonacci():
	n = raw_input("Ingrese n: ")
	print "Se imprimen a continuación los " + n + " primeros numeros de la serie de Fibonacci"
	ant = 1
	sig = 1
	print ant
	print sig
	for i in range(int(n)-2):
		fibo = sig + ant 
		ant = sig
		sig = fibo
		print fibo
		

fibonacci()

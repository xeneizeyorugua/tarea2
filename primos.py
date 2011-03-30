#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Devuelve los primos desde 1 hasta n

def es_primo(n):
	primo = True
	cont = 2
	while (primo and (n <> cont)):
		if (n % cont ==0):
			primo = False
		else:
			cont+=1
	
	return primo
# Solicito valor para n
m = raw_input("Ingrese un valor para n: ")
print "Los siguientes valores son primos menores que " + m
for j in range(2,int(m)):
	if es_primo(j): 
		print str(j)


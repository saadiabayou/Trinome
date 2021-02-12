# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 14:13:09 2020

@author: Saadia Bayou
"""



from Trinome import *

# *** Tests classe Trinome *** 


# Definition de 3 cas - valeurs discriminant delta -  

# Instanciation 

t1=Trinome(1,4,3) # discriminant delta positif - 2 solutions 
t2=Trinome(1,0,0) # discriminant delta égal à zéro - une solution 
t3=Trinome(1,2,3) # discriminant delta négatif - pas de solution réelle



T=[t1,t2,t3]

# Boucle d'instanciation

for t in T :
	print ("\nLes coefficients du trinome sont: \na=",t.a,"\nb=",t.b,"\nc=",t.c)
	print("\nLe trinome s'écrit : ",t)
	print("\nLa valeur du discriminant vaut : \ndelta =", t.delta())

	try:
		print("\nLa résolution du trinome est : \nsolution(s):", t.resolv())
	except ZeroDivisionError: 
		print("\nLe coefficient a est égal à zéro pas de solution possible")

    
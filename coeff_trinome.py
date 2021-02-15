# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 14:13:09 2020

@author: Saadia Bayou
"""



from Trinome import *

# *** trinome_1.py *** 

""" Ce programme permet de saisir les coefficients du trinome en ligne de commande """

print ("Entrer les coefficients du trinome : ")

a=float(input(" a = "))
b=float(input(" b = "))
c=float(input(" c = "))


# Instanciation 
t=Trinome(a,b,c)

# Notations pointées
   
print ("\nLes coefficients du trinome sont: \na=",t.a,"\nb=",t.b,"\nc=",t.c)
print("\nLe trinome s'écrit : ",t)
print("\nLa valeur du discriminant vaut : \ndelta =", t.delta())
try:
    print("\nLa résolution du trinome est : \nsolution(s):", t.resolv())
except ZeroDivisionError: 
    print("\nLe coefficient a est égal à zéro , cas dégénéré")



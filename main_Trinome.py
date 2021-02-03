# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 14:13:09 2020

@author: Saadia Bayou
"""



from Trinome import *

# *** Tests classe Trinome *** 



t1=Trinome(1,4,3) # discriminant positif - 2 solutions 
t2=Trinome(1,0,0) # discriminant égal à zéro - une solution 
t3=Trinome(1,2,3) # discriminant négatif 

    
print ("\nLes coefficients du trinome sont: \na=",t1.a,"\nb=",t1.b,"\nc=",t1.c)
print("\nLe trinome s'écrit : ",t1)
print("\nLa valeur du discriminant vaut : \ndelta =", t1.delta())
try:
    print("\nLa résolution du trinome est : \nsolution(s):", t1.resolv())
except ZeroDivisionError: 
    print("\nLe coefficient a est égal à zéro pas de solution possible")


print ("\nLes coefficients du trinome sont: \na=",t2.a,"\nb=",t2.b,"\nc=",t2.c)
print("\nLe trinome s'écrit : ",t2)
print("\nLa valeur du discriminant vaut : \ndelta =", t2.delta())
try:
    print("\nLa résolution du trinome est : \nsolution(s):", t2.resolv())
except ZeroDivisionError: 
    print("\nLe coefficient a est égal à zéro pas de solution possible")
        
        
print ("\nLes coefficients du trinome sont: \na=",t3.a,"\nb=",t3.b,"\nc=",t3.c)
print("\nLe trinome s'écrit : ",t3)
print("\nLa valeur du discriminant vaut : \ndelta =", t3.delta())
try:
    print("\nLa résolution du trinome est : \nsolution(s):", t3.resolv())
except ZeroDivisionError: 
    print("\nLe coefficient a est égal à zéro pas de solution possible")       
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 14:14:15 2020

@author: Saadia Bayou
"""
# Classe Trinome

from math import sqrt 

class Trinome (object):
    
    """ Definir une classe trinome t(x) :
        Afficher le trinome,
        Calculer son determinant,
        Resoudre le trinome : determiner la valeur de x pour t(x)=0
        """
    def __init__(self,coeff1,coeff2,coeff3):
        """ Constructeur : Construit un trinome à partir des coefficients : 
        coeff1, coeff2, coeff3 """
        self.a=coeff1
        self.b=coeff2
        self.c=coeff3
   
    def __str__(self):
        """ Affichage trinome """ 
        return "t(x) = "+ str(self.a)+"x²+" + str(self.b) + "x + " + str(self.c) + " \n on cherche à résoudre : {0.a}x² + {0.b}x + {0.c}".format(self) +" = 0"

    def delta (self):
        """ Calcul du discriminant delta """
        self.d=(((self.b)**2)-(4*self.a*self.c))/2
        return self.d 
    
    def resolv(self):
        """ Résolution du trinome selon le signe du discriminant """
        if self.d < 0:
          print( "Pas de solutions réelles")
        elif self.d ==0 :
            x0=-(self.b**2)/(2*self.a)
            print("Une solution unique x0 =-b²/2a :\n ")
            return "x0 = "+ str(x0) 
        else :
            (x1,x2)=((-self.b -sqrt(self.d)/(2*self.a)),(self.b -sqrt(self.d)/(2*self.a)))
            print("Deux solutions distinctes x1 et x2 :\n", "\nx1 =",x1,"\nx2 =" ,x2)
            return "x1="+str(x1),"x2 ="+ str(x2)

            


    



    
    
    
        
        
    

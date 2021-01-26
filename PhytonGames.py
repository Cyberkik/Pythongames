# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 15:41:46 2021

@author: cyber
"""

import random

mystere = random.randint(1,100)

print("Je vais imaginé un nombre entre 1 et 100")

print("A toi de le trouver")

reponse = 0

#print(type(reponse))
#print((mystere))

while mystere != reponse :
#    print(mystere)
    reponse = input('Trouve le nombre')
    reponse=int(reponse)
    if reponse < mystere :
        print("Plus grand")
    if reponse > mystere :
        print('Plus petit')
        
print("bravo")


      
        
    
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:00:23 2020

@author: aylinaydemir
"""
import random
 
def Menu():
    mode=int(input("Choisissez le mode de jeu souhaité : \n 1 : pour la Bataille Classique \n 2 : pour la Bataille découverte \n 3 : pour la Bataille à deux \n 4 : pour la Bataille d'addition \n"))
    if mode==1:
        print(Batailleclassique())
    elif mode==2:
        print(Batailledecouverte())
    elif mode==3:
        print(Batailleadeux())
    elif mode==4:
        print(Batailledaddition())
    return
 
T=[]
def distrib(T):   
    T=[]
    T=[i for i in range(2,15)]
    random.shuffle(T)
   
    T+=[i for i in range(2,15)]
    random.shuffle(T)
   
    T+=[i for i in range(2,15)]
    random.shuffle(T)
   
    T+=[i for i in range(2,15)]
    random.shuffle(T)
    

    jeu1=[]
    jeu2=[]
    for i in range(len(T)):
        if i%2==0:
            x=T.pop()
            jeu1.append(x)
        else:
            jeu2.append(T.pop())
    return (jeu1,jeu2)
 
    
def distrib2(T):   
    T=[]
    T=[i for i in range(1,10)]
    random.shuffle(T)
   
    T+=[i for i in range(1,10)]
    random.shuffle(T)
   
    T+=[i for i in range(1,10)]
    random.shuffle(T)
   
    T+=[i for i in range(1,10)]
    random.shuffle(T)
    

    jeu1=[]
    jeu2=[]
    for i in range(len(T)):
        if i%2==0:
            x=T.pop()
            jeu1.append(x)
        else:
            jeu2.append(T.pop())
    return (jeu1,jeu2)    


def Bataille1(jeu1,jeu2,cA,cB):
    x=jeu1.pop(0)
    y=jeu2.pop(0)
    print(x,"  ",y)
    if x>y:
        jeu1+=[cA,x,cB,y]
    elif y>x:
        jeu2+=[cB,y,cA,x]
    elif x==y:
        Bataille1(jeu1,jeu2,x,y)
    return
 
 
def Bataille2(jeu1,jeu2,cA,cB):
    x=jeu1.pop(0)
    y=jeu2.pop(0)
    cA2=jeu1.pop(0)
    cB2=jeu2.pop(0)
    print(cA2,"  ",cB2)
    print("#","   ","#")
    if cA2>cB2:
        jeu1+=[cA,x,cA2,cB,y,cB2]
    elif cB2>cA2:
        jeu2+=[cB,y,cB2,cA,x,cA2]
    elif cB2==cA2:
        Bataille2(jeu1,jeu2,cA2,cB2)
    return
   
    
def Bataille3(jeu1,jeu2,cA,cA2,cB,cB2):
    cA3=jeu1.pop(0)
    cB3=jeu2.pop(0)
    cA4=jeu1.pop(0)
    cB4=jeu2.pop(0)
    cA5=str(jeu1.pop(0))
    cB5=str(jeu2.pop(0))
    cA6=str(jeu1.pop(0))
    cB6=str(jeu2.pop(0))
    a=int(cA5+cA6)
    b=int(cB5+cB6)
    print("#","  ","#")
    print(a,"  ",b)
    if a>b:
        jeu1+=[cA,cA2,cA3,cA4,cA5,cA6]
        jeu1+=[cB,cB2,cB3,cB4,cB5,cB6]
    elif b>a:
        jeu2+=[cB,cB2,cB3,cB4,cB5,cB6]
        jeu2+=[cA,cA2,cA3,cA4,cA5,cA6]
    elif a==b:
        Bataille3(jeu1,jeu2,cA3,cA4,cB3,cB4)
    return
 
 
def Bataille4(jeu1,jeu2,cA,cA2,cB,cB2):   
    cA3=jeu1.pop(0)
    cB3=jeu2.pop(0)
    cA4=jeu1.pop(0)
    cB4=jeu2.pop(0)
    cA5=jeu1.pop(0)
    cB5=jeu2.pop(0)
    cA6=jeu1.pop(0)
    cB6=jeu2.pop(0)
    a=cA5+cA6
    b=cB5+cB6
    print("#","  ","#")
    print(a,"  ",b)
    if a>b:
        jeu1+=[cA,cA2,cA3,cA4,cA5,cA6]
        jeu1+=[cB,cB2,cB3,cB4,cB5,cB6]
    elif b>a:
        jeu2+=[cB,cB2,cB3,cB4,cB5,cB6]
        jeu2+=[cA,cA2,cA3,cA4,cA5,cA6]
    elif a==b:
        Bataille4(jeu1,jeu2,cA3,cA4,cB3,cB4)
    return
 
 
def Batailledecouverte():
    jeu1,jeu2=distrib(T)
    while len(jeu1)>0 and len(jeu2)>0:
        cA=jeu1.pop(0)
        cB=jeu2.pop(0)
        print(cA,"  ",cB)
        if cA>cB:
            jeu1.append(cA)
            jeu1.append(cB)
        elif cB>cA:
            jeu2.append(cB)
            jeu2.append(cA)
        elif cA==cB:
            if len(jeu1)<1:
                len(jeu1)==0
            elif len(jeu2)<1:
                len(jeu2)==0
            else :
                print("Il y a une Bataille")
                Bataille1(jeu1,jeu2,cA,cB)
    if len(jeu1)==0:
        print("Le vainqueur est le Joueur 2")
    elif len(jeu2)==0:
        print("Le vainqueur est le Joueur 1")
    return
   

def Batailleclassique():
    jeu1,jeu2=distrib(T)
    while len(jeu1)>0 and len(jeu2)>0:
        cA=jeu1.pop(0)
        cB=jeu2.pop(0)
        print(cA,"  ",cB)
        if cA>cB:
            jeu1.append(cA)
            jeu1.append(cB)
        elif cB>cA:
            jeu2.append(cB)
            jeu2.append(cA)
        elif cA==cB:
            if len(jeu1)<2:
                len(jeu1)==0
            elif len(jeu2)<2:
                len(jeu2)==0
            else :
                print("Il y a une Bataille")
                Bataille2(jeu1,jeu2,cA,cB)
    if len(jeu1)==0:
        print("Le vainqueur est le Joueur 2")
    elif len(jeu2)==0:
        print("Le vainqueur est le Joueur 1")
    return
   
    
def Batailleadeux():
    jeu1,jeu2=distrib2(T)
    while len(jeu1)>0 and len(jeu2)>0:
        cA=str(jeu1.pop(0))
        cA2=str(jeu1.pop(0))
        cB=str(jeu2.pop(0))
        cB2=str(jeu2.pop(0))
        x=int(cA+cA2)
        y=int(cB+cB2)
        print(x,"  ",y)
        if x>y:
            jeu1+=[cA,cA2]
            jeu1+=[cB,cB2]
        elif y>x:
            jeu2+=[cB,cB2]
            jeu2+=[cA,cA2]
        elif x==y:
            if len(jeu1)<4:
                len(jeu1)==0
            elif len(jeu2)<4:
                len(jeu2)==0
            else :
                print("Il y a une Bataille")
                Bataille3(jeu1,jeu2,cA,cA2,cB,cB2)
    if len(jeu1)==0:
        print("Le vainqueur est le Joueur 2")
    elif len(jeu2)==0:
        print("Le vainqueur est le Joueur 1")
    return
 
 
def Batailledaddition():
    
    jeu1,jeu2=distrib2(T)
    while len(jeu1)>0 and len(jeu2)>0:
        cA=jeu1.pop(0)
        cA2=jeu1.pop(0)
        cB=jeu2.pop(0)
        cB2=jeu2.pop(0)
        x=cA+cA2
        y=cB+cB2
        print(x,"  ",y)
        if x>y:
            jeu1+=[cA,cA2]
            jeu1+=[cB,cB2]
        elif y>x:
            jeu2+=[cB,cB2]
            jeu2+=[cA,cA2]
        elif x==y:
            if len(jeu1)<4:
                len(jeu1)==0
            elif len(jeu2)<4:
                len(jeu2)==0
            else :
                print("Il y a une Bataille")
                Bataille4(jeu1,jeu2,cA,cA2,cB,cB2)
    if len(jeu1)==0:
        print("Le vainqueur est le Joueur 2")
    elif len(jeu2)==0:
        print("Le vainqueur est le Joueur 1")
    return
Menu()
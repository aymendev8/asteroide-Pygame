import pygame
import random

class t_asteroide:
    def __init__(self,taille):
        self.taille = taille
        if taille == 1 : 
            self.image = pygame.image.load("Images/asteroide_grand.png") 
        if taille == 2 : 
            self.image = pygame.image.load("Images/asteroide.png")
        if taille == 3 : 
            self.image = pygame.image.load("Images/asteroide_petit.png")

        A=[i for i in range(0,800)]
        self.x = random.choice(A)
        B=[i for i in range(0,600)]
        self.y = random.choice(B)

        if self.x < 400:
            self.direction_x = 1
        else : 
            self.direction_x = -1

        if self.y < 300: 
            self.direction_y = 1
        else : 
            self.direction_y = -1 

        self.vitesse_en_x = self.direction_x * 2  
        self.vitesse_en_y = self.direction_x * 2  

        self.hauteur = self.image.get_height()
        self.largeur = self.image.get_width()
    
    def afficher_asteroide(self,ecran):
        ecran.blit(self.image,(self.x,self.y))
    
    def deplacer_asteroide(self):
        self.x += self.vitesse_en_x
        self.y += self.vitesse_en_y


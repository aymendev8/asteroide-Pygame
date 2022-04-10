import pygame
import math


class t_vaisseau:
    def __init__(self):
        self.image = pygame.image.load("Images/vaisseau.png")
        self.rect = self.image.get_rect()
        self.hauteur = self.image.get_height()
        self.largeur = self.image.get_width()
        self.x = 400
        self.y = 300
        self.angle = 0
        self.rotation = pygame.transform.rotate(self.image, self.angle)
        self.rotation_rect = self.rotation.get_rect()
        self.rotation_rect.center = (self.x, self.y)
        self.cosinus = math.cos(math.radians(self.angle + 90))
        self.sinus = math.sin(math.radians(self.angle + 90))
        self.tete_vaisseau = (self.x + self.cosinus * self.largeur//2, self.y - self.sinus * self.hauteur//2)

    def afficher_vaisseau(self, ecran):
        ecran.blit(self.rotation, self.rotation_rect)

    def tourner_gauche(self):
        self.angle += 5
        self.image = pygame.image.load("Images/vaisseau.png")
        self.rotation = pygame.transform.rotate(self.image, self.angle)
        self.rotation_rect = self.rotation.get_rect()
        self.rotation_rect.center = (self.x, self.y)
        self.cosinus = math.cos(math.radians(self.angle + 90))
        self.sinus = math.sin(math.radians(self.angle + 90))
        self.tete_vaisseau = (
            self.x + self.cosinus * self.largeur//2, self.y - self.sinus * self.hauteur//2)

    def tourner_droite(self):
        self.angle -= 5
        self.image = pygame.image.load("Images/vaisseau.png")
        self.rotation = pygame.transform.rotate(self.image, self.angle)
        self.rotation_rect = self.rotation.get_rect()
        self.rotation_rect.center = (self.x, self.y)
        self.cosinus = math.cos(math.radians(self.angle + 90))
        self.sinus = math.sin(math.radians(self.angle + 90))
        self.tete_vaisseau = (
            self.x + self.cosinus * self.largeur//2, self.y - self.sinus * self.hauteur//2)

    def accelerer(self):
        self.x += self.cosinus * 6
        self.y -= self.sinus * 6
        self.image = pygame.image.load("Images/vaisseau_boost.png")
        self.rotation = pygame.transform.rotate(self.image, self.angle)
        self.rotation_rect = self.rotation.get_rect()
        self.rotation_rect.center = (self.x, self.y)
        self.cosinus = math.cos(math.radians(self.angle + 90))
        self.sinus = math.sin(math.radians(self.angle + 90))
        self.tete_vaisseau = (self.x + self.cosinus * self.largeur //2, self.y - self.sinus * self.sinus * self.hauteur // 2)

    def replacer_vaisseau(self):
        if 0 >= self.x:
            self.x = 799
        if 0 >= self.y:
            self.y = 599

        if self.y >= 600:
            self.y = 0
        if self.x >= 800:
            self.x = 0

    def repositionner(self):
        self.x = 400
        self.y = 300    
    
    def changer_image(self):
        self.image = pygame.image.load("Images/vaisseau.png")
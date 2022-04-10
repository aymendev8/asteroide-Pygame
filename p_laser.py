import pygame

class t_laser:
    def __init__(self, vaisseau):
        self.x = vaisseau.tete_vaisseau[0]
        self.y = vaisseau.tete_vaisseau[1]
        self.vitesse_x = vaisseau.cosinus * 10
        self.vitesse_y = vaisseau.sinus * 10

    def afficher_laser(self, ecran):
        pygame.draw.rect(ecran, (240, 0, 32), [self.x, self.y, 8, 8])

    def deplacement_laser(self):
        self.x += self.vitesse_x
        self.y -= self.vitesse_y

    
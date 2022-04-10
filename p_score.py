import pygame
pygame.font.init()




class t_score:
    def __init__(self):
        self.vie = pygame.image.load("Images/vie.png")
        self.score_img = pygame.image.load("Images/score.png")
        self.game_over = pygame.image.load("Images/game_over.png")
        self.meilleur_score_img = pygame.image.load("Images/meilleur_score.png")
        self.nb_vie = 3
        self.score = 0
        self.meilleur_score = 0

    def afficher_vie(self, ecran,vaisseau):
        if self.nb_vie == 3:
            ecran.blit(self.vie,(660,20))
            ecran.blit(self.vie,(700,20))
            ecran.blit(self.vie,(740,20))

        if self.nb_vie == 2:
            ecran.blit(self.vie,(700,20))
            ecran.blit(self.vie,(740,20))

        if self.nb_vie == 1:
            ecran.blit(self.vie,(740,20))

    def afficher_score(self,ecran):
        police = pygame.font.SysFont("comicsans",23)
        texte = police.render(str(self.score),1,(255,255,255))
        ecran.blit(self.score_img,(0,0))
        ecran.blit(texte,(80,2))

    def afficher_game_over(self,ecran):
        ecran.blit(self.game_over,(303,246))
    
    def afficher_meilleur_score(self,ecran):
        police = pygame.font.SysFont("comicsans",23)
        texte = police.render(str(self.meilleur_score),1,(255,255,255))
        if self.meilleur_score > 0:
            ecran.blit(self.meilleur_score_img,(20,550))
            ecran.blit(texte,(160,550))
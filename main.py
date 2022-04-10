import time
import pygame
import p_vaisseau
import p_bouton
import p_laser
import p_score
import p_asteroide
import random


# Mes variables
mon_ecran_hauteur = 600
mon_ecran_largeur = 800
mon_horloge = pygame.time.Clock()
parti_en_cours = False
le_fond = pygame.image.load("Images/fond.png")
le_logo = pygame.image.load("Images/logo_asteroide.png")
le_bouton_play = p_bouton.t_bouton(pygame.image.load("Images/bouton_jouer.png"),303,246)
le_bouton_quitter = p_bouton.t_bouton(pygame.image.load("Images/bouton_quitter.png"),303,346)
mes_lasers = [] 
mes_asteroides = []
compteur_asteroide = 0
mon_vaisseau = p_vaisseau.t_vaisseau()
le_score = p_score.t_score()


# La fenetre du jeu
pygame.init()
mon_ecran = pygame.display.set_mode((mon_ecran_largeur, mon_ecran_hauteur))
pygame.display.set_caption("Astéroîde")

# La boucle du jeu
jeu = True
while jeu:
    mon_ecran.blit(le_fond, (0, 0))
    # fps
    mon_horloge.tick(60)
    compteur_asteroide += 2

      # Gestion des evenements
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            jeu = False
        if evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_SPACE:
                mes_lasers.append(p_laser.t_laser(mon_vaisseau))  
        pos = pygame.mouse.get_pos()
        if evt.type == pygame.MOUSEBUTTONDOWN:
            if le_bouton_play.est_cliquer(pos):
                parti_en_cours = True
                le_score.nb_vie = 3
            if le_bouton_quitter.est_cliquer(pos):
                parti_en_cours = False
                jeu = False

            
    if not parti_en_cours:

        mon_ecran.blit(le_logo, (150,60))
        le_bouton_play.dessiner_bouton(mon_ecran)
        le_bouton_quitter.dessiner_bouton(mon_ecran)
        mes_asteroides = []
        mes_lasers = []
        le_score.score = 0
        le_score.afficher_meilleur_score(mon_ecran)

    
    # parti démarrer
    if parti_en_cours:
        mon_vaisseau.afficher_vaisseau(mon_ecran)
        mon_vaisseau.replacer_vaisseau()
        le_score.afficher_vie(mon_ecran,mon_vaisseau)
        le_score.afficher_score(mon_ecran)

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_q]:
            mon_vaisseau.tourner_gauche()
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            mon_vaisseau.tourner_droite()
        if key[pygame.K_UP] or key[pygame.K_z]:
            mon_vaisseau.accelerer()

        for laser in mes_lasers:
            laser.deplacement_laser()
            if laser.x > mon_ecran_largeur + 10 or laser.y > mon_ecran_hauteur + 10 or laser.x <= -10 or laser.y <= -10 :
                mes_lasers.pop(mes_lasers.index(laser))

        for asteroide in mes_asteroides:
            asteroide.deplacer_asteroide()
            if asteroide.x > mon_ecran_largeur + 50 or asteroide.y > mon_ecran_hauteur + 50 or asteroide.x == -30 or asteroide.y == -30 :
                mes_asteroides.pop(mes_asteroides.index(asteroide))

        if compteur_asteroide % 50 == 0:
            taille = random.choice([1,2,2])
            mes_asteroides.append(p_asteroide.t_asteroide(taille))

        if le_score.nb_vie == 0:
            le_score.afficher_score(mon_ecran)
            if le_score.score > le_score.meilleur_score : 
                le_score.meilleur_score = le_score.score
            time.sleep(1)
            parti_en_cours = False

        
        for asteroide in mes_asteroides : 
            for laser in mes_lasers:
                if laser.x >= asteroide.x and laser.x <= asteroide.x + asteroide.largeur or laser.x + 8 >= asteroide.x and laser.x + 8 <= asteroide.x + asteroide.largeur:
                    if laser.y >= asteroide.y and laser.y <= asteroide.y + asteroide.hauteur or laser.y + 8 >= asteroide.y and laser.y + 8 <= asteroide.y + asteroide.hauteur:
                        if asteroide.taille == 1 : 

                            a = p_asteroide.t_asteroide(2)
                            b = p_asteroide.t_asteroide(2)
                            a.x, b.x = asteroide.x,asteroide.x
                            a.y, b.y = asteroide.y,asteroide.y
                            mes_asteroides.append(a)
                            mes_asteroides.append(b)
                            le_score.score += 40
                            le_score.afficher_score(mon_ecran)
                            mes_lasers.pop(mes_lasers.index(laser))
                            mes_asteroides.pop(mes_asteroides.index(asteroide))

                        if asteroide.taille == 2 :

                            a = p_asteroide.t_asteroide(3)
                            b = p_asteroide.t_asteroide(3)
                            a.x, b.x = asteroide.x,asteroide.x
                            a.y, b.y = asteroide.y,asteroide.y
                            mes_asteroides.append(a)
                            mes_asteroides.append(b)
                            le_score.score += 20
                            le_score.afficher_score(mon_ecran)
                            mes_lasers.pop(mes_lasers.index(laser))
                            mes_asteroides.pop(mes_asteroides.index(asteroide))

                        if asteroide.taille == 3:
                                le_score.score += 5
                                le_score.afficher_score(mon_ecran)
                                mes_lasers.pop(mes_lasers.index(laser))
                                mes_asteroides.pop(mes_asteroides.index(asteroide))
                        
                    
    for laser in mes_lasers:
        laser.afficher_laser(mon_ecran)
    for asteroide in mes_asteroides:
        asteroide.afficher_asteroide(mon_ecran)
        if mon_vaisseau.x >= asteroide.x and mon_vaisseau.x <= asteroide.x + asteroide.largeur:
            if mon_vaisseau.y >= asteroide.y and mon_vaisseau.y <= asteroide.y + asteroide.hauteur :
                mes_asteroides.pop(mes_asteroides.index(asteroide))  
                le_score.nb_vie -= 1    
                mon_vaisseau.x = 400
                mon_vaisseau.y = 300

    pygame.display.flip()
pygame.quit()

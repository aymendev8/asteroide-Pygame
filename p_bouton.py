class t_bouton():
    def __init__(self,image,x,y):
        self.image = image
        self.x = x
        self.y = y
        self.hauteur = self.image.get_height()
        self.largeur = self.image.get_width()

    def dessiner_bouton(self, ecran):
        ecran.blit(self.image,(self.x,self.y))

    def est_cliquer(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.largeur:
            if pos[1] > self.y and pos[1] < self.y + self.hauteur:
                return True
        return False
    

        
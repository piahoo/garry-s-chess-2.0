import pygame
import conf


class Pawn(pygame.sprite.Sprite):
    def __init__(self, x, y, color, size, square):
        pygame.sprite.Sprite.__init__(self)
        if color == "black":
            self.image = pygame.image.load("images/BP.png")
        else:
            self.image = pygame.image.load("images/WP.png")
        self.color = color
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.has_moved = False
        self.square = square

        def legal_moves():
            return True


class King(pygame.sprite.Sprite):
    def __init__(self, x, y, color, size, square):
        pygame.sprite.Sprite.__init__(self)
        if color == "black":
            self.image = pygame.image.load("images/BK.png")
        else:
            self.image = pygame.image.load("images/WK.png")
        self.color = color
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.square = square


class Queen(pygame.sprite.Sprite):
    def __init__(self, x, y, color, size, square):
        pygame.sprite.Sprite.__init__(self)
        if color == "black":
            self.image = pygame.image.load("images/BQ.png")
        else:
            self.image = pygame.image.load("images/WQ.png")
        self.color = color
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.square = square


class Rook(pygame.sprite.Sprite):
    def __init__(self, x, y, color, size, square):
        pygame.sprite.Sprite.__init__(self)
        if color == "black":
            self.image = pygame.image.load("images/BR.png")
        else:
            self.image = pygame.image.load("images/WR.png")
        self.color = color
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.square = square


class Knight(pygame.sprite.Sprite):
    def __init__(self, x, y, color, size, square):
        pygame.sprite.Sprite.__init__(self)
        if color == "black":
            self.image = pygame.image.load("images/BN.png")
        else:
            self.image = pygame.image.load("images/WN.png")
        self.color = color
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.square = square


class Bishop(pygame.sprite.Sprite):
    def __init__(self, x, y, color, size, square):
        pygame.sprite.Sprite.__init__(self)
        if color == "black":
            self.image = pygame.image.load("images/BB.png")
        else:
            self.image = pygame.image.load("images/WB.png")
        self.color = color
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.square = square

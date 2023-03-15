import pygame
class Ship():
    def __init__(self, ai_settings, screen):
        #Initialize the ship and set its starting position
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the ship image an get its rect.
        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Store a decimal value for rhe ship's center.
        self.center = float(self.rect.centerx)

        #Movement flag
        self.moving_right = False
        self.moving_left = False

        #Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def update(self):
        #Update the ship's position based on the movement flag
        #Update the ship's center value, not the rect.
        if self.moving_right:
            self.rect.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.rect.center -= self.ai_settings.ship_speed_factor

        #Update rect object from self.center.
        self.rect.centerx = self.center

    def blitime(self):
        #Draw the ship at its current location
        self.screen.blit(self.image, self.rect)
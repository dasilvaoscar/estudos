import sys, pygame



class MyGame(object):
  
  def __init__(self, image_path) -> None:
    super().__init__()
    pygame.init()
    self.size = self.width, self.height = 500, 500
    self.speed = [2, 2]
    self.black = 0, 0, 0
    self.screen = pygame.display.set_mode(self.size)
    self.ball = pygame.image.load(image_path)
    self.ballrect = self.ball.get_rect()
    
game = MyGame('intro_ball.gif')

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = game.ballrect.move(game.speed)
    if ballrect.left < 0 or ballrect.right > game.width:
        game.speed[0] = -game.speed[0]
    if ballrect.top < 0 or ballrect.bottom > game.height:
        game.speed[1] = -game.speed[1]

    game.screen.fill(game.black)
    game.screen.blit(game.ball, ballrect)
    pygame.display.flip()
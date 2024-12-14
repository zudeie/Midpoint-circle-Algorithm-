import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint Circle Drawing Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0,00, 00)

# Function to draw a circle using mid-point algorithm
def draw_circle(xc,yc,r):
        x=0
        y=r
        d= 1-r
        
        while(x<=y):
            screen.set_at((round(x+xc), round(y+yc)), WHITE) 
            screen.set_at((round(y+xc), round(x+yc)), WHITE) 
            screen.set_at((round(-y+xc), round(x+yc)), WHITE) 
            screen.set_at((round(-x+xc), round(y+yc)), WHITE) 
            screen.set_at((round(-x+xc), round(-y+yc)), WHITE) 
            screen.set_at((round(-y+xc), round(-x+yc)), WHITE) 
            screen.set_at((round(y+xc), round(-x+yc)), WHITE) 
            screen.set_at((round(x+xc), round(-y+yc)), WHITE) 
            
            x = x + 1
            if(d<0):
                 d = d+ 2*x+1
            else:
                y=y-1
                d=d+2*x-2*y+1
                
                
      
# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)
        
        draw_circle(100,100,90)
        
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
   
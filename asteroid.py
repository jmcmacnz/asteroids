from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self,x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(surface=screen,color='white', center=self.position, radius=self.radius, width=2)
        return
    
    def update(self, dt):
        self.position += self.velocity * dt
        return
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        print(f"angle = {angle}")
        new_dir_1 = self.velocity.rotate(angle)
        new_dir_2 = self.velocity.rotate(-1*angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_rad)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_rad)
        new_asteroid_1.velocity = new_dir_1*1.2
        new_asteroid_2.velocity = new_dir_2*1.2
        return

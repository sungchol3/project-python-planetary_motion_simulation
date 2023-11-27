import turtle
import time

# Constants
G = 100000 # Gravitational constant
# Create planets
class Planet(turtle.Turtle):
    def __init__(self, m, x, y, vx, vy, color="black"):
        self.tr = turtle.Turtle()
        self.tr.shape("circle")
        self.tr.color(color)
        self.m = m
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def goto(self, x, y):
        self.tr.up()
        self.x = x
        self.y = y
        self.tr.goto(x, y)
        self.tr.down()
    
    def acceleration(self, other):
        global G
        dx = other.x - self.x
        dy = other.y - self.y
        r = (dx**2 + dy**2)**0.5
        a = G*other.m / r**2
        ax = a * dx / r
        ay = a * dy / r
        return ax, ay
    
    def move(self, dt):
        print("pos: ", self.x, self.y, "vel: ", self.vx, self.vy)
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.tr.goto(self.x, self.y)
    
    def get_pos(self):
        return self.x, self.y

def moving_simulation(pl1, pl2, dt):
    ax1, ay1 = pl1.acceleration(pl2)
    ax2, ay2 = pl2.acceleration(pl1)
    pl1.vx += ax1 * dt
    pl1.vy += ay1 * dt
    pl2.vx += ax2 * dt
    pl2.vy += ay2 * dt
    pl1.move(dt)
    pl2.move(dt)
    
def distance(pl1, pl2):
    x1, y1 = pl1.get_pos()
    x2, y2 = pl2.get_pos()
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

if __name__ == "__main__":
    dt = 0.01 #time step
    #create planets
    pl1 = Planet(100, 0, 0, 0, 0, color="red")
    pl2 = Planet(100, 0, 0, 0, 0, color="blue")
    #set initial position
    pl1.goto(0, 100)
    pl2.goto(0, -100)
    while distance(pl1, pl2) > 10:
        moving_simulation(pl1, pl2, dt)
        time.sleep(dt)

input("Press any key to exit")
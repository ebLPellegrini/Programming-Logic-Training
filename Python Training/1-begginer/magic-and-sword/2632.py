from math import sqrt, pow

def main():
    total_Tests = int(input())
    for _ in range(total_Tests):
        first_input = input().split(" ")
        w, h, enemy_X0, enemy_Y0 = first_input
        w = int(w)
        h = int(h)
        enemy_X0 = int(enemy_X0)
        enemy_Y0 = int(enemy_Y0)
            
        enemy = Rectangle(enemy_X0, enemy_Y0, enemy_X0 + w, enemy_Y0 + h)
            
        second_input = input().split(" ")
        spell, level, center_X, center_Y = second_input
        level = int(level)
        center_X = int(center_X)
        center_Y = int(center_Y)
                            
        distance = distance_Nearest(center_X, center_Y, enemy.x0, enemy.y0, enemy.x1, enemy.y1)
                    
        if radius[spell][level] >= distance:
            print(damage[spell])
        else:
            print('0')
        
class Rectangle:
    def __init__(self, x0, y0 , x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        
damage = {
    "fire": 200,
    "water": 300,
    "earth": 400,
    "air": 100
}

radius = {
    "fire": {
        1: 20,
        2: 30,
        3: 50
    },
    "water": {
        1: 10,
        2: 25,
        3: 40
    },
    "earth": {
        1: 25,
        2: 55,
        3: 70
    },
    "air": {
        1: 18,
        2: 38,
        3: 60
    }
}
    
def distance_Nearest(x_Center, y_Center, x0, y0, xf,yf):
    x_Closest = max(x0, min(x_Center, xf))
    y_Closest = max(y0, min(y_Center, yf))
    
    return sqrt(pow(x_Center - x_Closest, 2) + pow(y_Center - y_Closest, 2))

main()      
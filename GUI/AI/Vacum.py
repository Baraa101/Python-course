import time
class Vacum:

    def __init__(self, canvas, window, size, xVelocity, color, locationA, locationB, vcState):
        self.canvas = canvas
        self.canWidth = canvas.winfo_width()
        self.center=(200-size)/2
        self.window = window
        self.image = canvas.create_rectangle(
            self.center,
            self.center,
            self.center+size,
            self.center+size,
            fill=color)
        self.xvelocity = xVelocity
        self.locatonA=locationA
        self.locatonB=locationB
        self.location = locationA
        self.vcState = vcState
    
    def moveRight(self):
        if(self.location == self.locatonA):
            self.location = self.locatonB
            for i in range(40):
                cords = self.canvas.coords(self.image)
                self.canvas.move(self.image, self.xvelocity, 0)
                self.window.update()
                time.sleep(0.01)
            
        
            
    def moveLeft(self):
        if (self.location == self.locatonB):
            self.location = self.locatonA
            for i in range(40):
                cords = self.canvas.coords(self.image)
                self.canvas.move(self.image, -self.xvelocity, 0)
                self.window.update()
                time.sleep(0.01)

    def suck(self):
        self.location.clean = True
        self.canvas.itemconfig(self.location.rect, fill='green')
        

    
    def precept(self):
        if (not self.location.clean):
            self.vcState.insert("end","Suck\n<><><><><><>\n")
            self.suck()
        elif (self.location.symbol=='A'):
            self.vcState.insert("end","Move Right\n<><><><><><>\n")
            self.moveRight()
        elif (self.location.symbol=='B'):
            self.vcState.insert("end","Move Left\n<><><><><><>\n")
            self.moveLeft()
        self.vcState.see("end")

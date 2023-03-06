class Ball:

    def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=color)
        self.xvelocity = xVelocity
        self.yvelocity = yVelocity
    
    def move(self):
        cords = self.canvas.coords(self.image)
        """ print(cords) """

        if(cords[2]>=(self.canvas.winfo_width()) or cords[0]<0):
            self.xvelocity = -self.xvelocity
        if(cords[3]>=(self.canvas.winfo_height()) or cords[1]<0):
            self.yvelocity = -self.yvelocity
        self.canvas.move(self.image,self.xvelocity,self.yvelocity)
class ball:
    def __init__(self,canvas,x,y,diameter,x_speed,y_speed,colour):
        self.canvas = canvas
        self.diameter = diameter
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=colour)

    def move(self):
        self.coordinate = self.canvas.coords(self.image) 
        # (x1, y1) = top-left corner of bounding box
        # (x2, y2) = bottom-right corner

        #                (x2)                                                  (x1)  
        if(self.coordinate[2] >= (self.canvas.winfo_width()) or self.coordinate[0] < 0):
            self.x_speed = -self.x_speed
        #                 (y2)                                                  (y1)
        if(self.coordinate[3] >= (self.canvas.winfo_height()) or self.coordinate[1] < 0):
            self.y_speed = -self.y_speed

        self.canvas.move(self.image,self.x_speed,self.y_speed)
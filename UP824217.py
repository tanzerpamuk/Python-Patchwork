#----------------------------------------------------------------------------------------------------------------------------------
#Coursework: Patch Samples
#Tanzer Pamuk
#UP824217
#----------------------------------------------------------------------------------------------------------------------------------









from graphics import *

#Before we start to draw, we are defining the sizes and the colours of our Patch

def getInputs():
#Indefinete loops till we get the right answer from user    
    while True:
        size = input("Which size do you prefer (5x5,7x7,9x9): ")
        if size in ["5x5", "7x7", "9x9"]:
            break
        else:
            print("Wrong size, give it another go")
            
    colourType = []            
    for i in range(3):
        while True:
            colour = input("What is your colour: ")
            if colour in ["red","blue", "green", "orange", "pink", "brown"]:
                colourType.append(colour)
                break
            else:
                print("Wrong Colour.!! Choose again")
                            
    return eval(size[0]), colourType #The inputs are ready to code in
    
#Drawing the stairs in a square
def rectangles(x, y, win, colour):
    for i in range(10):
        rect = Rectangle(Point(x + (i*10), y + 90-(i*10)), Point(x + 100, y + 100-(i*10)))
        rect.draw(win)
        rect.setFill(colour)
        rect.setOutline(colour)
        
#Drawing the boats neatly in a square:        
def boat(x, y, win, colour, colour2):
    
    body1 = Polygon(Point(x,y + 25), Point(x+25,y+25), Point(x+22,y+30), Point(x+3,y+30))
    body1.setFill(colour2)
    body1.draw(win)
    line1 = Line(Point(x+12.50,y+20), Point(x+12.50,y+25))
    line1.draw(win)
    sail1 = Polygon(Point(x+12.50,y), Point(x,y+20), Point(x+25,y+20))
    sail1.setFill(colour)
    sail1.draw(win)
    
    
def boats(x, y, win, colour):
    column = 1
    for m in range(3):
        for n in range(4):
            if column == 2:
                boat(x + n*25, y + m*35, win, "white", colour)
            else:
                 boat(x + n*25, y + m*35, win, colour, "white")
                
        
    
    
def drawPatchwork(x, y, size, colourType):
    win = GraphWin("PATCHWORK", size*100, size*100)
    win.setBackground("white")
    for vertical in range(size):
        for horizontal in range(size):
            if vertical == 0:
                if horizontal == 0:
                    rectangles(x + (100*horizontal), y + (100*vertical), win, colourType[0])
                else:
                    rectangles(x + (100*horizontal), y + (100*vertical), win, colourType[1])
            elif horizontal == (size -1):
                if vertical == (size - 1):
                    rectangles(x + (100*horizontal), y + (100*vertical), win, colourType[0])
                else:
                    rectangles(x + (100*horizontal), y + (100*vertical), win, colourType[1])
            elif horizontal == vertical:
                rectangles(x + (100*horizontal), y + (100*vertical), win, colourType[0])
            else:
                if vertical - horizontal < 0:
                    boats(x + (100*horizontal), y + (100*vertical), win, colourType[1])
                else:
                    boats(x + (100*horizontal), y + (100*vertical), win, colourType[2])    
    
    
# Our main funtion to make "PATCHWORK" drawn
def main():
    size, colourType = getInputs()
    drawPatchwork(0,0, size, colourType)
    

main()        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
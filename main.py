from tkinter import *


root = Tk()
root.title("Color picker")
root.geometry('560x340')

def slide(value):
    r = redValue.get()
    g = greenValue.get()
    b = blueValue.get()
    rgb = (r, g, b)
    hexacode = "#%02x%02x%02x" % rgb
    colorFrame['bg'] = hexacode
    
    
redValue = IntVar()
greenValue = IntVar()
blueValue = IntVar()

#   Create color display frame

colorFrame = Label(root, bg = "black", width=40, height = 15)
colorFrame.place(x = 10, y = 10)

#   Making color scales
#   Red
redSlider = Scale(root, variable = redValue,fg = "red", from_=0, to=255,length = 200, cursor = "dot", highlightbackground = "red",orient = "horizontal", sliderlength=20, label="Red", command = slide)
redSlider.place(x = 330, y= 20)

#   Green
greenSlider = Scale(root, variable = greenValue, from_=0, to=255,length = 200, cursor = "dot", highlightbackground = "green",fg = "green", orient = "horizontal", sliderlength=20, label="Red", command = slide)
greenSlider.place(x = 330, y= 120)

#   Red
blueSlider = Scale(root, variable = blueValue, fg = "blue", from_=0, to=255,length = 200, cursor = "dot", highlightbackground = "blue",orient = "horizontal", sliderlength=20, label="Red", command = slide)
blueSlider.place(x = 330, y= 220)

#   Disable maximize
root.resizable(False, False)

root.mainloop()
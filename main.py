from textwrap import wrap
from tkinter import *


root = Tk()
root.title("Color picker")
root.geometry('560x300')

def slide(value):
    r = redValue.get()
    g = greenValue.get()
    b = blueValue.get()
    rgb = (r, g, b)
    #   Convert (r, g, b) into hex code
    hexcode = "#%02x%02x%02x" % rgb
    
    #   Apply changes to color of frame
    colorFrame['bg'] = hexcode
    
    #   Apply changes to hexcode textbox
    hexDisplay.delete(1.0, END)    
    hexDisplay.insert(END, hexcode)
    
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
greenSlider = Scale(root, variable = greenValue, from_=0, to=255,length = 200, cursor = "dot", highlightbackground = "green",fg = "green", orient = "horizontal", sliderlength=20, label="Green", command = slide)
greenSlider.place(x = 330, y= 120)

#   Blue
blueSlider = Scale(root, variable = blueValue, fg = "blue", from_=0, to=255,length = 200, cursor = "dot", highlightbackground = "blue",orient = "horizontal", sliderlength=20, label="Blue", command = slide)
blueSlider.place(x = 330, y= 220)

#   Hex Code
hexLabel = Label(root, text = "Hex Code : ")
hexLabel.place(x=10, y = 270)

#   Hex Code text box
hexDisplay = Text(root, height = 1, width = 10, wrap = WORD)
hexDisplay.place(x = 80, y = 270)
hexDisplay.insert(END, "#000000")
#   Disable maximize
root.resizable(False, False)

root.mainloop()
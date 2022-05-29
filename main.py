#   Color Picker
#   Picks hex code for different rgb values
#   May 29, 2022

from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Color picker")
root.geometry('560x300')
root.iconbitmap('images/colorPickerIcon.ico')

#   Disable maximize
root.resizable(False, False)


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
    
    
def copySuccess():
    messagebox.showinfo("Copy Success", "Copied Successfully!!")    #   Show success message box
    clip = Tk()                                                     #   Create small window
    clip.withdraw()                                                 #   Withdraw value
    clip.clipboard_clear()                                          #   Clear clipboard in Tk clipboard
    clip.clipboard_append(hexDisplay.get(1.0, END))                 #   Get hexcode copied to clipboard
    clip.destroy()                                                  #   Destroy this and all descendent widgets
    
    #   Now you can paste it anywhere


# Holds integer data where we can set integer data and can retrieve it as well using getter and setter methods.
redValue = IntVar()
greenValue = IntVar()
blueValue = IntVar()

#   Create color display frame

colorFrame = Label(root, bg = "black", width=40, height = 15)
colorFrame.place(x = 10, y = 10)

#   Making color scales(sliders)

#   Red
redSlider = Scale(root, variable = redValue,fg = "red", from_=0, to=255,length = 200, cursor = "dot", highlightbackground = "red",orient = "horizontal", sliderlength=20, label="Red", command = slide)
redSlider.place(x = 330, y= 20)

#   Green
greenSlider = Scale(root, variable = greenValue, from_=0, to=255,length = 200, cursor = "dot", highlightbackground = "green",fg = "green", orient = "horizontal", sliderlength=20, label="Green", command = slide)
greenSlider.place(x = 330, y= 120)

#   Blue
blueSlider = Scale(root, variable = blueValue, fg = "blue", from_=0, to=255,length = 200, cursor = "dot", highlightbackground = "blue",orient = "horizontal", sliderlength=20, label="Blue", command = slide)
blueSlider.place(x = 330, y= 220)

#   Hex  Label
hexLabel = Label(root, text = "Hex Code : ")
hexLabel.place(x=10, y = 270)

#   Hex Code Text box
hexDisplay = Text(root, height = 1, width = 10, wrap = WORD)
hexDisplay.place(x = 80, y = 270)
hexDisplay.insert(END, "#000000")

#   Copy Button
copyButton = Button(root, text = "Copy", command = copySuccess)
copyButton.place(x = 200, y = 270)


root.mainloop()
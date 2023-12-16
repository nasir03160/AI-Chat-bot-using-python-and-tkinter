from tkinter import*
from PIL import Image,ImageTk
import action

from speech_to_text import speech_to_text
#Creating a object 
root = Tk()
root.title("Burney") #change title 
root.geometry("550x675") #size
root.resizable(False, False) #fix the size
root.config(bg='pink') #colour 


def ask():
    user_val = speech_to_text()  # Get user input using speech recognition
    bot_val = action.Action(user_val)
    text.insert(END, 'User ---> ' + user_val + "\n")
    if bot_val is not None:
        text.insert(END, "Bot ---> " + str(bot_val) + '\n')
    if bot_val == "Okay, shutting down":
        root.destroy()


       
#del func
def delete():
    text.delete('1.0', "end")
    
#send func
def send():
    send= entry.get()
    bot=action.Action(send)
    text.insert(END, "user--->" +str(send)+'\n')
    
    if bot != NONE:
        text.insert(END,"BOT ---->"+str(bot)+'\n')
        
    if bot =="Okay, shutting down":
     root.destroy()

#main frame
frame= LabelFrame(root, padx=100, pady=7, borderwidth=3 , relief="raised")
frame.config(bg='grey')
frame.grid(row =0, column=1 ,padx=75, pady= 10)
#text label
text_label=Label(frame, text="Bruney AI", font=("comic Sans ms",14 , 'bold'), bd=3)
text_label.grid(row=0, column=0, padx=20, pady=10)

#install pillow as tkinter only allows gif modules not pics 

#image 
image_path = r'E:\OneDrive\Desktop\os projecr\ai.jpg'
image = ImageTk.PhotoImage(Image.open(image_path))
#image position
image_label= Label(frame, image=image)
image_label.grid(row=1,column= 0,pady=20)

#adding text widget
text= Text(root , font =('courier 10 bold'), bg='grey')
text.grid(row= 2, column= 0)
text.place(x= 100 , y= 375, width=375, height=100)

#Entry widget

entry= Entry(root, justify=CENTER)
entry.place(x=100, y=500,width= 350, height=30)

#button 1
button1=Button(root, text="Ask",bg='grey',pady=60,padx=40,borderwidth=3,relief=SOLID, command=ask)
button1.place(x=70,y=575)


#button 2
button2=Button(root, text="delete",bg='grey',pady=60,padx=40,borderwidth=3,relief=SOLID, command=delete)
button2.place(x=400,y=575)

#button 3
button3=Button(root, text="send",bg='grey',pady=60,padx=40,borderwidth=3,relief=SOLID, command=send)
button3.place(x=225,y=575)

root.mainloop() #basic frame of UI



'''import sys
import warnings

__version__ = sys.version[:sys.version.index(' ')]

_DEPRECATION_MESSAGE = ("The distutils package is deprecated and slated for "
                        "removal in Python 3.12. Use setuptools or check "
                        "PEP 632 for potential alternatives")
warnings.warn(_DEPRECATION_MESSAGE,
              DeprecationWarning, 2)'''

from kivymd.app import MDApp

from kivymd.uix.label import MDLabel

class DiceApp(MDApp):
    def build(self):
        return MDLabel
    (
            import random

             from tkinter import *
             root=Tk()
            root.geometry("700x450")

              l1=Label(root,font=("times",200))

    
               def roll():

                 number=['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
                 l1.config(text=f'{random.choice(number)}')
                l1.pack()


             b1=Button(root,text="Lets rolll",command=roll)
             b1.place(x=325,y=0)

             root.mainloop()
     )
        if__name__=='__main__':
            DiceApp().run()
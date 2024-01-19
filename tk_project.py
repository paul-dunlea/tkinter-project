from tkinter import * 
import tkinter as tk
class Options:
    def __init__(self):
        self._root=Tk()
        self._root.title("paint app")
        self._root.geometry("900x600")
        self._root.config(bg="skyblue")
        self._left_frame=Frame(self._root,width=200,height=580,bg="grey")
        self._left_frame.grid(row=0,column=0,padx=10,pady=10)

        self._right_frame=Frame(self._root,width=700,height=600,bg="white")
        self._right_frame.grid(row=0,column=1)


        self._lab1=Label(self._left_frame,text="colours")
        self._lab1.grid(row=0,column=0)

        self._red=Button(self._left_frame,text="red",command=lambda:self.setcolour("red"))
        self._red.grid(row=1,column=0)
        self._blue=Button(self._left_frame,text="blue",command=lambda:self.setcolour("blue"))
        self._blue.grid(row=2,column=0)
        self._yellow=Button(self._left_frame,text="yellow",command=lambda:self.setcolour("yellow"))
        self._yellow.grid(row=3,column=0)
        self._green=Button(self._left_frame,text="green",command=lambda:self.setcolour("green"))
        self._green.grid(row=4,column=0)

        self._lab2=Label(self._left_frame,text="shapes ")
        self._lab2.grid(row=0,column=2)

        self._line=Button(self._left_frame,text="line",command=lambda:self.setshape("line"))
        self._line.grid(row=1,column=2)
        self._oval=Button(self._left_frame,text="oval",command=lambda:self.setshape("oval"))
        self._oval.grid(row=2,column=2)
        self._rectangle=Button(self._left_frame,text="rectangle",command=lambda:self.setshape("rectangle"))
        self._rectangle.grid(row=3,column=2)
        self._left_frame.grid_propagate(False)
    def setcolour(self,event):
        self._colourset=event
    def setshape(self,event):
        self._shapeset=event

    

class Paint(Options):
    def __init__(self):
        super().__init__()
        self._mycanvas=tk.Canvas(self._right_frame,width=700,height=600)
        self._mycanvas.bind("<Button 1>",self.mouseclick)
        self._clickcount=0
        self._mycanvas.pack()



    def mouseclick(self,event):
        try:
            self._clickcount+=1
            if self._clickcount==2:
                x1=self._firstclick[0]
                y1=self._firstclick[1]

                if self._shapeset=="oval":
                    self._mycanvas.create_oval(x1, y1, event.x,event.y, fill=self._colourset)
                if self._shapeset=="rectangle":
                    self._mycanvas.create_rectangle(x1,y1,event.x,event.y,fill=self._colourset)
                if self._shapeset=="line":
                    self._mycanvas.create_line(x1,y1,event.x,event.y,fill=self._colourset)
                self._clickcount=0
            else:
                self._firstclick=(event.x,event.y)
        except AttributeError as ae:
            if "shapeset" in str(ae):
                print("Error: pick a shape")
            elif "colourset" in str(ae):
                print("Error: pick a colour")
            self._clickcount=0
    def run(self):
        self._root.mainloop()


    
if __name__=="__main__":
    app=Paint()
    app.run()
from tkinter import *
from tkinter import ttk

cor1 = "#3c3c3c"
cor2 = "#38576b"
cor3 = "#008"

btnColor = "#e4c3c2"
btnBorder = "#3ff"

janela =Tk()
janela.title("Calculadora")
janela.geometry("185x280")
janela.config(bg=cor1)


## frames 
frame_tela = Frame(janela, width=185, height=60, bg=cor2)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=185, height=220)
frame_corpo.grid(row=1, column=0)

## crinado label
app_label = Label(frame_tela, text="123234", width=19, height=3)
app_label.place(x=0, y=0)


#botoes
b1 = Button(frame_corpo, text="C", width=11, height=2, bg=btnColor)
b1.place(x=0, y=0)
b2 = Button(frame_corpo, text="%", width=5, height=2, bg=btnColor)
b2.place(x=90, y=0)
b3 = Button(frame_corpo, text="/", width=5, height=2, bg=btnColor)
b3.place(x=139, y=0)

b4 = Button(frame_corpo, text="7", width=5, height=2, bg=btnColor)
b4.place(x=0, y=45)
b5 = Button(frame_corpo, text="8", width=5, height=2, bg=btnColor)
b5.place(x=46, y=45)
b6 = Button(frame_corpo, text="9", width=5, height=2, bg=btnColor)
b6.place(x=92, y=45)
b7 = Button(frame_corpo, text="*", width=5, height=2, bg=btnColor)
b7.place(x=139, y=45)

b8 = Button(frame_corpo, text="4", width=5, height=2, bg=btnColor)
b8.place(x=0, y=90)
b9 = Button(frame_corpo, text="5", width=5, height=2, bg=btnColor)
b9.place(x=46, y=90)
b10 = Button(frame_corpo, text="6", width=5, height=2, bg=btnColor)
b10.place(x=92, y=90)
b11 = Button(frame_corpo, text="-", width=5, height=2, bg=btnColor)
b11.place(x=139, y=90)

b12 = Button(frame_corpo, text="1", width=5, height=2, bg=btnColor)
b12.place(x=0, y=135)
b13 = Button(frame_corpo, text="2", width=5, height=2, bg=btnColor)
b13.place(x=46, y=135)
b14 = Button(frame_corpo, text="3", width=5, height=2, bg=btnColor)
b14.place(x=92, y=135)
b15 = Button(frame_corpo, text="+", width=5, height=2, bg=btnColor)
b15.place(x=139, y=135)

b16 = Button(frame_corpo, text="0", width=11, height=2, bg=btnColor)
b16.place(x=0, y=180)
b17 = Button(frame_corpo, text=".", width=5, height=2, bg=btnColor)
b17.place(x=92, y=180)
b18 = Button(frame_corpo, text="=", width=5, height=2, bg=btnColor)
b18.place(x=139, y=180)



janela.mainloop()

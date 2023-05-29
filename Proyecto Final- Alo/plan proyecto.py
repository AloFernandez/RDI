from tkinter import *
from tkinter import messagebox
ventana=Tk()

#------------------------------------------
w = 380
h = 350
ws = ventana.winfo_screenheight()
hs = ventana.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

ventana.geometry('%dx%d+%d+%d' %(w,h,x,y))

#------------------------------------------
"""
def mayor():
	if n1.get()== "":
		messagebox.showinfo("Faltan datos ","ingrese nª1")
		entry_n1.focus()
		return
	n_1=n1.get()
	if n_1.isdigit()== False:
		messagebox.showerror("Error","Tipo de dato invalido"
		entry_n1.focus()
		n1.set("")
		return

"""

lbl_n1=Label(ventana,text="Ingrese su nombre ")
lbl_n1.pack()
lbl_n1.place(x=50,y=60)

lbl_n1=Label(ventana,text="Ingrese apellido")
lbl_n1.pack()
lbl_n1.place(x=70,y=90)



entry_n1 =Entry(ventana)
entry_n1.pack()
entry_n1.place(x=170,y=60)


entry_n2 =Entry(ventana)
entry_n2.pack()
entry_n2.place(x=170,y=90)


btn_calcular=Button(ventana,text="Ingrese su fecha importante")
btn_calcular.pack()
btn_calcular.place(x=50,y=120)

btn_calcular=Button(ventana,text="Ingresar")
btn_calcular.pack()
btn_calcular.place(x=220,y=120)










ventana.mainloop()    

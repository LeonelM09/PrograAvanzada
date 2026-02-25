import tkinter as tk
from tkinter import messagebox

def ventanas():
        if var.get()==1:
            messagebox.showinfo("Ventana de información","Aca puedes escribrir info al usuario")
        elif var.get()==2:
            messagebox.showwarning("Ventana de advertencia","Esta es una advertencia")
        elif var.get()==3:
            messagebox.showerror("Ventana de error","Has cometido un error")
        elif var.get()==4:
            respuesta=messagebox.askyesno("Ventana de opcion","Te gusta esta clase")
            if respuesta:
                   messagebox.showinfo("Ventana de respuesta","Más te vale")
            else:
                      messagebox.showinfo("Ventana de respuesta","Por eso vas a reprobar")
        elif var.get()==5:
            respuesta=messagebox.askokcancel("Ventana de opcion","Das tu alma a esta clase?")
            if respuesta:
                   messagebox.showinfo("Ventana de respuesta","Por eso vas a sacar 10")
            else:
                      messagebox.showinfo("Ventana de respuesta","Por eso repruebas")
        else:
         messagebox.showinfo("Opcion elegida","No seleccionaste nada")


ven1=tk.Tk()
ven1.title("Uso de los diferentes messagebox")
ven1.geometry("500x600")
ven1.config(bg="lightgreen")
etiqueta1=tk.Label(ven1,text="Veremos el uso de las messagebox")
etiqueta1.pack()

var=tk.IntVar()
rad1=tk.Radiobutton(ven1,text="Mostrar iformación",variable=var,value=1)
rad1.pack(pady=20)
rad2=tk.Radiobutton(ven1,text="Advertencia",variable=var,value=2)
rad2.pack(pady=20)
rad3=tk.Radiobutton(ven1,text="Error",variable=var,value=3)
rad3.pack(pady=20)
rad4=tk.Radiobutton(ven1,text="Pregunta si o no",variable=var,value=4)
rad4.pack(pady=20)
rad5=tk.Radiobutton(ven1,text="Pregunta aceptar o cancelar",variable=var,value=5)
rad5.pack(pady=20)
boton1=tk.Button(ven1,text="Sacar ventana",command=ventanas)
boton1.pack(pady=30)

ven1.mainloop()
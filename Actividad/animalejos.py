import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

def opcion():
    seleccionar=var.get()
    if seleccionar==1:
         ventana_2()
    elif seleccionar==2:
         ventana_3()
    elif seleccionar==3:
         ventana_4()
    elif seleccionar==4:
         ventana_5()
    else:
         messagebox.showinfo("Opcion elegida","No seleccionaste nada")


def ventana_principal():
    global ven1
    global var
    ven1=tk.Tk()
    ven1.title("Ventana Principal")
    ven1.geometry("600x400")
    ven1.config(bg="pink")

    eti1=tk.Label(ven1,text="Esta es la ventana principal")
    eti1.grid(row=1,column=0,padx=5,pady=5)

    imagen=Image.open("C:/Users/DELL/Desktop/Actividad/animales-collage-lifeder-min.jpg")
    imagen=imagen.resize((400,200))
    imagen_tk=ImageTk.PhotoImage(imagen)
    label_imagen=tk.Label(ven1,image=imagen_tk)
    label_imagen.grid(row=1,column=0,padx=5,pady=5)

    var=tk.IntVar()
    rad1=tk.Radiobutton(ven1,text="Elefante",variable=var,value=1)
    rad1.grid(row=2,column=0,padx=5,pady=5)
    rad2=tk.Radiobutton(ven1,text="Jirafe",variable=var,value=2)
    rad2.grid(row=3,column=0,padx=5,pady=5)
    rad3=tk.Radiobutton(ven1,text="Castor",variable=var,value=3)
    rad3.grid(row=4,column=0,padx=5,pady=5)
    rad4=tk.Radiobutton(ven1,text="León",variable=var,value=4)
    rad4.grid(row=5,column=0,padx=5,pady=5)

    boton1=tk.Button(ven1,text="Ver info", command=opcion)
    boton1.grid(pady=20)


    ven1.mainloop()

def destruir_ventanas(ventana_actual):
    ventana_actual.destroy()
    ventana_principal()

def ventana_2():
    ven1.destroy()
    ven2=tk.Tk()
    ven2.title("Ventana secundaria")
    ven2.geometry("600x400")
    ven2.config(bg="lightblue")

    imagen=Image.open("C:/Users/DELL/Desktop/Actividad/elephant-laptop-q3nfxlsda8kdywfp.jpg")
    imagen=imagen.resize((400,200))
    imagen_tk=ImageTk.PhotoImage(imagen)
    label_imagen=tk.Label(ven1,image=imagen_tk)
    label_imagen.grid(row=1,column=0,padx=5,pady=5)

    eti2=tk.Label(ven2,text="Esta es la ventana2")
    eti2.grid()

    boton2=tk.Button(ven2,text="Ventana principal", command=lambda: destruir_ventanas(ven2))
    boton2.grid(pady=20)


    ven2.mainloop()

def ventana_3():
    ven1.destroy()
    ven3=tk.Tk()
    ven3.title("Ventana secundaria")
    ven3.geometry("600x400")
    ven3.config(bg="lightblue")

    eti3=tk.Label(ven3,text="Esta es la ventana3")
    eti3.pack()

    boton3=tk.Button(ven3,text="Ventana principal", command=lambda: destruir_ventanas(ven3))
    boton3.pack(pady=20)


    ven3.mainloop()

def ventana_4():
    ven1.destroy()
    ven4=tk.Tk()
    ven4.title("Ventana secundaria")
    ven4.geometry("600x400")
    ven4.config(bg="lightblue")

    eti4=tk.Label(ven4,text="Esta es la ventana4")
    eti4.pack()

    boton4=tk.Button(ven4,text="Ventana principal", command=lambda: destruir_ventanas(ven4))
    boton4.pack(pady=20)


    ven4.mainloop()

def ventana_5():
    ven1.destroy()
    ven5=tk.Tk()
    ven5.title("Ventana secundaria")
    ven5.geometry("600x400")
    ven5.config(bg="lightblue")

    eti5=tk.Label(ven5,text="Esta es la ventana2")
    eti5.pack()

    boton5=tk.Button(ven5,text="Ventana principal", command=lambda: destruir_ventanas(ven5))
    boton5.pack(pady=20)


    ven5.mainloop()

ventana_principal()
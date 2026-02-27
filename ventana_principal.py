import tkinter as tk
def ventana_principal():
    global ven1
    ven1=tk.Tk()
    ven1.title("Ventana Principal")
    ven1.geometry("600x400")
    ven1.config(bg="aqua")

    eti1=tk.Label(ven1,text="Esta es la ventana principal")
    eti1.pack()

    boton1=tk.Button(ven1,text="Ventana 2",command=ventana_2)
    boton1.pack(pady=20)
    boton2=tk.Button(ven1,text="Ventana 3",command=ventana_3)
    boton2.pack(pady=20)
    boton3=tk.Button(ven1,text="Ventana 4",command=ventana_4)
    boton3.pack(pady=20)
    boton4=tk.Button(ven1,text="Ventana 5",command=ventana_5)
    boton4.pack(pady=20)
    
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

    eti2=tk.Label(ven2,text="Esta es la ventana2")
    eti2.pack()

    boton2=tk.Button(ven2,text="Ventana principal", command=lambda: destruir_ventanas(ven2))
    boton2.pack(pady=20)


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
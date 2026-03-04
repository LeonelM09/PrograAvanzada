import tkinter as tk
from PIL import Image, ImageTk 
from tkinter import messagebox

def ventana_principal():
    global ven1
    ven1=tk.Tk()
    ven1.title("Esta es mi ventana principal")
    ven1.geometry("800x400")
    ven1.config(bg="lightblue")

    eti1=tk.Label(ven1,text="Reino Animal",bg="lightblue",font=("Arial",23,"bold"))
    eti1.pack()
    frame1= tk.Frame(ven1)
    frame1.pack(fill=tk.X, padx=10, pady=10)
    imagen = Image.open("C:/Users/Salon202/Downloads/ñ/ventanas/animales-collage-lifeder-min.jpg")
    imagen = imagen.resize((400, 200))  # Redimensionar si es necesario
    imagen_tk = ImageTk.PhotoImage(imagen) 
    label_imagen = tk.Label(frame1, image=imagen_tk)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)
    frame2=tk.Frame(frame1)
    frame2.grid(row=0, column=1, padx=5, pady=5)
    var=tk.IntVar()
    ele=tk.Radiobutton(frame2,text="Elefante",variable=var,value=1)
    ele.pack()
    jirafa=tk.Radiobutton(frame2,text="Jirafa",variable=var,value=2)
    jirafa.pack()
    castor=tk.Radiobutton(frame2,text="Castor",variable=var,value=3)
    castor.pack()
    leon=tk.Radiobutton(frame2,text="León",variable=var,value=4)
    leon.pack()

    def informacion():
        seleccion=var.get()
        if seleccion==1:
            ventana_elefante()
        elif seleccion==2:
            ventana_jirafa()
        elif seleccion==3:
            ventana_castor()
        elif seleccion==4:
            ventana_león()
        else:
             messagebox.showinfo("Opcion elegida","No seleccionaste nada")

    boton1=tk.Button(ven1,text="Ver info",command=informacion)
    boton1.pack()

    ven1.mainloop()

def regresar_a_primera(ventana_actual):
    ventana_actual.destroy()  # Cerrar la segunda ventana
    ventana_principal()  # Volver a abrir la ventana principal

def ventana_elefante():
    global ven2
    ven1.destroy()
    ven2=tk.Tk()
    ven2.title("Información del elefante")
    ven2.geometry("800x400")
    ven2.config(bg="gray")

    eti2=tk.Label(ven2,text="Elefante",bg="gray",font=("Algerian",24,"bold"))
    eti2.pack(pady=10)
    frame3=tk.Frame()
    frame3.pack(pady=20)
    imagen2= Image.open("C:/Users/Salon202/Downloads/ñ/ventanas/elephant-laptop-q3nfxlsda8kdywfp.jpg")
    imagen2=imagen2.resize((400,200))
    imagen_tk2=ImageTk.PhotoImage(imagen2)
    label_imagen=tk.Label(frame3,image=imagen_tk2)
    label_imagen.grid(row=0,column=0,padx=5,pady=5)
    etiqueta2=tk.Label(frame3,text="""Los elefantes pueden escuchar con los pies. " 
    "Resulta que tienen unos receptores especiales en las plantas de sus patas que les permiten detectar vibraciones sísmicas en la tierra."
    " Gracias a esto, pueden comunicarse entre sus manadas a distancias de hasta 16 kilómetros, enviando mensajes de alerta si hay peligro o avisando dónde hay agua."
    "¡Todo a través de pisotones de baja frecuencia que viajan por el suelo y suben por sus patas hasta sus oídos!""",wraplength=200,justify="left")
    etiqueta2.grid(row=0,column=1,padx=5,pady=5)

    boton2=tk.Button(ven2,text="ir a ventana principal",command=lambda: regresar_a_primera(ven2) )
    boton2.pack(pady=30)

    ven2.mainloop()

def ventana_jirafa():
    global ven3
    ven1.destroy()
    ven3=tk.Tk()
    ven3.title("Información de la jirafa")
    ven3.geometry("800x400")
    ven3.config(bg="gray")
    eti3=tk.Label(ven3,text="Jirafa",bg="gray",font=("Algerian",24,"bold"))
    eti3.pack(pady=10)
    frame3=tk.Frame()
    frame3.pack(pady=20)
    imagen2= Image.open("C:/Users/Salon202/Downloads/ñ/ventanas/animals-wildlife-nature-giraffes-wallpaper-preview.jpg")
    imagen2=imagen2.resize((400,200))
    imagen_tk2=ImageTk.PhotoImage(imagen2)
    label_imagen=tk.Label(frame3,image=imagen_tk2)
    label_imagen.grid(row=0,column=0,padx=5,pady=5)
    etiqueta3 = tk.Label(frame3, text="""La jirafa tiene un "bloqueador solar" integrado.
    Tienen la lengua de color azul oscuro, casi morado, y puede medir ¡hasta 50 centímetros!
    La evolución les dio este color para proteger su lengua de quemaduras solares, ya que pasan la mayor parte del día con la lengua de fuera arrancando hojas en lo alto de los árboles bajo el intenso sol de la sabana.""", wraplength=200, justify="left")
    etiqueta3.grid(row=0, column=1, padx=5, pady=5)

    boton3=tk.Button(ven3,text="ir a ventana principal",command=lambda: regresar_a_primera(ven3) )
    boton3.pack(pady=30)

    ven3.mainloop()

def ventana_castor():
    global ven4
    ven1.destroy()
    ven4=tk.Tk()
    ven4.title("Información del castor")
    ven4.geometry("800x400")
    ven4.config(bg="gray")
    eti4=tk.Label(ven4,text="Castor",bg="gray",font=("Algerian",24,"bold"))
    eti4.pack(pady=10)
    frame3=tk.Frame()
    frame3.pack(pady=20)
    imagen2= Image.open("C:/Users/Salon202/Downloads/ñ/ventanas/istockphoto-531662275-612x612.jpg")
    imagen2=imagen2.resize((400,200))
    imagen_tk2=ImageTk.PhotoImage(imagen2)
    label_imagen=tk.Label(frame3,image=imagen_tk2)
    label_imagen.grid(row=0,column=0,padx=5,pady=5)
    etiqueta4 = tk.Label(frame3, text="""El castor tiene unos "goggles" naturales.
    Tienen un segundo par de párpados que son totalmente transparentes. Cuando se sumergen en el agua, cierran estos párpados especiales.
    Esto les permite proteger sus ojos de las ramas y los escombros mientras construyen sus presas, ¡pero sin perder la capacidad de ver perfectamente bajo el agua!""", wraplength=200, justify="left")
    etiqueta4.grid(row=0, column=1, padx=5, pady=5)

    boton4=tk.Button(ven4,text="ir a ventana principal",command=lambda: regresar_a_primera(ven4) )
    boton4.pack(pady=30)

    ven4.mainloop()

def ventana_león():
    global ven5
    ven1.destroy()
    ven5=tk.Tk()
    ven5.title("Información del león")
    ven5.geometry("800x400")
    ven5.config(bg="gray")
    eti5=tk.Label(ven5,text="León",bg="gray",font=("Algerian",24,"bold"))
    eti5.pack(pady=10)
    frame3=tk.Frame()
    frame3.pack(pady=20)
    imagen2= Image.open("C:/Users/Salon202/Downloads/ñ/ventanas/Sultan_the_Barbary_Lion.jpg")
    imagen2=imagen2.resize((400,200))
    imagen_tk2=ImageTk.PhotoImage(imagen2)
    label_imagen=tk.Label(frame3,image=imagen_tk2)
    label_imagen.grid(row=0,column=0,padx=5,pady=5)
    
    etiqueta5 = tk.Label(frame3, text="""El león es el rey de las siestas.
    Aunque tienen fama de ser feroces y activos cazadores, la realidad es que son súper dormilones.
    Para conservar energía debido al intenso calor de su hábitat, los leones pueden llegar a dormir y descansar entre 16 y 20 horas al día. Eso sí, cuando despiertan y rugen, su sonido es tan potente que puede escucharse a kilómetros.""", wraplength=200, justify="left")
    etiqueta5.grid(row=0, column=1, padx=5, pady=5)

    boton5=tk.Button(ven5,text="ir a ventana principal",command=lambda: regresar_a_primera(ven5) )
    boton5.pack(pady=30)

    ven5.mainloop()

ventana_principal()
import tkinter as tk
from PIL import Image, ImageTk

def boton_clic():
    print("Hiciste click")

def actualizar_etiqueta():
    nuevo_texto=entrada.get()
    etiqueta.config(text=nuevo_texto)

ven1=tk.Tk()
ven1.title("Jorgitoelgnomo")
ven1.geometry("500x500")

boton=tk.Button(ven1,text="Haz clic aquí", command=boton_clic,
                font=("Comic Sans",30))
boton.pack(pady=20)

entrada=tk.Entry(ven1,width=60)
entrada.pack(pady=10)

boton1=tk.Button(ven1,text="Actualizar",command=actualizar_etiqueta)
boton1.pack()

etiqueta=tk.Label(ven1,text="Texto inicial", font=("Arial",12))
etiqueta.pack(pady=10)

imagen=Image.open("3timebomb.png")
imagen=imagen.resize((400,200))
imagen_tk=ImageTk.PhotoImage(imagen)
label_imagen=tk.Label(ven1,image=imagen_tk)
label_imagen.pack(pady=20)

#etiqueta=tk.Label(ven1,text="Hola, Grupo de programación Básica",
#    font=("Arial",14,"bold"),fg="black",bg="yellow",padx=20,pady=10)
#etiqueta1=tk.Label(ven1,text="Soy Leonel",
#    font=("Arial",14,"bold"),fg="black",bg="green",padx=20,pady=10)
#etiqueta2=tk.Label(ven1,text="Estudio la ing. en ciencias de la computación",
#    font=("Arial",14,"bold"),fg="black",bg="yellow",padx=20,pady=10)
#etiqueta3=tk.Label(ven1,text="Y me gustan las tlayudas",
#    font=("Arial",14,"bold"),fg="black",bg="yellow",padx=20,pady=10)
#etiqueta.pack()
#etiqueta1.pack()
#etiqueta2.pack()
#etiqueta3.pack()

ven1.mainloop()


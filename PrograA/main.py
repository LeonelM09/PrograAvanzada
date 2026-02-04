from humanidad import*

humano1=Humano("Diana",17,"Femenino")
print(humano1.nombre)
print(humano1.edad)
print(humano1.genero) #atributos no necesitan terminar en paraentesis 
humano1.caract() #metodos terminan en parentesis 
humano1.saludo()

programador1=Programador("Gilberto",20,"Masculino")
print(programador1.nombre)
print(programador1.edad)
print(programador1.genero)
programador1.caract()
programador1.saludo()
programador1.saludo2()

ingeniero1=Ingeniero("Letzel",18,"Masculino","Ciencias de la computación")
print(ingeniero1.nombre)
print(ingeniero1.edad)
print(ingeniero1.genero)
ingeniero1.caract()
ingeniero1.saludo()

#lic1=Licenciado
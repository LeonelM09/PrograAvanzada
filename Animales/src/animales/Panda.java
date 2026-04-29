package animales;

public class Panda {
   String Nombre;
    String Color;
    int patas;
    
    public Panda(String name, String color, int legs){
        this.Nombre=name;
        this.Color=color;
        this.patas=legs;
    }
    public void Sonidopanda(){
            System.out.println("El panda hace ...");
    }
    public void Descripcionpanda(){
        System.out.println("El panda se llama: "+Nombre+ " es color "+Color+" y tiene "+patas+" patas");
        
    }

} 


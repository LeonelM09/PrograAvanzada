package animales;

public class MainAnimales {
    public static void main(String[] args){
        Perro perro1=new Perro("Kino","negro",3);
        perro1.Sonidoperro();
        perro1.Descripcionperro();
        
        Gato gato1=new Gato("Tigris","atigrado",2);
        gato1.Sonidogato();
        gato1.Descripciongato();
        
        Panda panda1=new Panda("Shifu","nigga",4);
        panda1.Sonidopanda();
        panda1.Descripcionpanda();
    }
    
}

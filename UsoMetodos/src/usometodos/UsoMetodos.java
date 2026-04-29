package usometodos;
public class UsoMetodos {
    public static void Saludo(){
        System.out.println("Hola ejecutaste saludo");    
    }
    public static double calcularDistancia(double a, double b){
        double dist = Math.abs(a-b);
        return dist;
    }        
    public static void main(String[] args) {
        Saludo();
        Saludo();
        Saludo();
        double berna= calcularDistancia(3.5,9.987);
        System.out.println("El valor de la distancia: "+berna);
    }
    
}

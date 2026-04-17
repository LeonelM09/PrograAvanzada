package aplicacion3;
import java.util.Scanner;


public class Aplicacion3 {
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner lector=new Scanner(System.in);
        System.out.println("Dame tu altura");
        double altura=lector.nextDouble();
        lector.nextLine();
        System.out.println("Dame tu nombre");
        String nombre=lector.nextLine();
        System.out.println("Dame tu edad");
        int edad=lector.nextInt();
        lector.close();
        System.out.println("Tu nombre es: "+nombre+ " Tu altura es: "+altura+" Tu edad es: "+edad);
        if (edad >=18){
            System.out.println("Tu eres mayor de edad");
        }
        else{
            System.out.println("Tu eres menor de edad");
        }
        
    }
    
}

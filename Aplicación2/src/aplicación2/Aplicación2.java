package aplicación2;
import java.util.Scanner;

public class Aplicación2 {

    public static void main(String[] args) {
        // TODO code application logic here
        /*
        double base = 9.6;
        double altura = 5.6;
        
        double area = (base*altura)/2;
        System.out.println("El triangulo don bas:"+base+" y altura:"+altura+" Tiene area de:" +area);
        System.out.printf("El triangulo con base %.2f y altura %.2f tiene area de: %.2f \n",base,altura,area);
         */
        
        System.out.println("--- Area de Triangulo ---");
        
        Scanner lector=new Scanner(System.in);
        System.out.print("Dame una base: ");
        double base=lector.nextDouble();
        System.out.print("Dame una altura: ");
        double altura=lector.nextDouble();
        System.out.println("");
        double area = (base*altura)/2;
        System.out.printf("El triangulo con base %.2f y altura %.2f tiene area de: %.2f \n",base,altura,area);
        
        
                
       
    }
    
}

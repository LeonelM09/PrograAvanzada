package clase24;
import java.util.Scanner;

public class Clase24 {

    public static void main(String[] args) {
         Scanner scanner = new Scanner(System.in);
         System.out.println("--- Calculadora de Impuestos Bracket ---");
            System.out.print("Ingrese su salario anual: ");
            double salario = scanner.nextDouble();


     
            if (salario <= 10000 ) {
                System.out.printf("La cantidad de %.2f no paga impuestos \n", salario);
            } else if (salario > 10000 || salario <= 30000) {
                double impuesto=salario*0.15;
                System.out.printf("Debe de pagar %.2f pesos \n", impuesto);
            } else {
                double impu=salario*0.3;
                System.out.printf("La cantidad de impuestos a pagar s: %.2f \n", impu);
            }

            scanner.close();
     
    }
    
}

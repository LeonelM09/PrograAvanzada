package clase23;
import java.util.Scanner;

public class Clase23 {

    public static void main(String[] args) {
        /*
        Scanner dana=new Scanner(System.in);
        System.out.print("Dame la opcion que quieras: ");
        int opcion_menu = dana.nextInt();
        switch (opcion_menu) {
            case 1:
            System.out.println("Iniciando ETL...");
             break; // IMPORTANTE: EL break le dice a Java que se salga del switch, sino ejecutará todo lo de abajo
            case 2:
             System.out.println("Filtrando base de datos...");
            break;
            case 3:
            System.out.println("Exportando a CSV...");
            break;
            default:
             // default es el equivalente a "else", es el caso de seguridad.
            System.out.println("Error 404: Opción no válida en el sistema.");
        }
      */
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("--- SENSOR DE ALERTA AMBIENTAL ---");
        System.out.print("Ingrese la temperatura del sistema (double): ");
        double nivelTemp = scanner.nextDouble();
        
        System.out.print("Ingrese presión del cilindro (int): ");
        int presion = scanner.nextInt();
        
        // Evaluamos doble factor de riesgo
        if (nivelTemp > 80.0 && presion > 100) {
            System.out.println("¡ALERTA ROJA! Riesgo inminente de explosión térmica.");
        } else if (nivelTemp > 80.0 || presion > 100) {
            System.out.println("Aviso: Un valor excedió el límite de control. Por favor, revise de inmediato.");
        } else {
            System.out.println("Sistema en condiciones operativas óptimas. Riesgo calculado bajo.");
        }
        
        scanner.close();
    }
    
}

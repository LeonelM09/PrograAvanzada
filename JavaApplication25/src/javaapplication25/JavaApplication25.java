
package javaapplication25;

public class JavaApplication25 {
    public static void main(String[] args) {
     /*   
    int contador = 1; // Inicializamos un iterador

    while (contador <= 5) {
        System.out.println("Iteración número: " + contador);
        contador++; // contador++ es equivalente a decir: contador = contador + 1;
        
        }
     */  
     /*
    for (int i = 0; i < 10; i++) {
    System.out.println("Procesando epoch n.º " + i);
    // 'i' será primero 0 y se ejecutará. 0 < 10, i aumenta a 1. Y así sucesivamente.
    
    }
    // El ciclo se detiene cuando el iterador es 5.
*/
     for (int i = 0; i<10; i++){
         System.out.println("Estamos en la iteración: " + i);
     }
     
    int[] puntuaciones_sat={1200,1500,1050,1340,950};
     
    double[] probabilidadVentas = new double[4];
     
    probabilidadVentas[0]=0.52;
    probabilidadVentas[1]=0.70;
    
        System.out.println("El valor en la posicion 2 de la lista puntuaciones_sa es: "+puntuaciones_sat[1]);
     
    }
    
}

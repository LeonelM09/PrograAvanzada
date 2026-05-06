package modelo.a;

public class Main {
    public static void main(String[] args) {
        
        ModeloA modelo1 = new ModeloA("Regresion Logistica", 0.50);
        ModeloA modelo2 = new ModeloA("Arbol de Decisiones", 0.65);
        
        System.out.println("--- ESTADO INICIAL ---");
        modelo1.mostrarDesempenio();
        modelo2.mostrarDesempenio();
        
        System.out.println("\n --- Ejecutando comportamientos ---");
        modelo1.entrenarModelo();
        
        System.out.println("\n--- Estado FINAL ---");
        modelo1.mostrarDesempenio();
        modelo2.mostrarDesempenio();
    }
    
}

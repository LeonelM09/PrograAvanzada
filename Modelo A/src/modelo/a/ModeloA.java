package modelo.a;

public class ModeloA {
    
    String nombreAlgoritmo;
    double precision;
    boolean estaEntrenado;
    
    public ModeloA(String npNombre, double npPrecisionInicial){
        this.nombreAlgoritmo = npNombre;
        this.precision =  npPrecisionInicial;
        this.estaEntrenado = false;
        
    }
    
    public void entrenarModelo(){
        System.out.println("Iniciando fase de entrenamiento para " +this.nombreAlgoritmo+ "...");
        precision = precision + 0.15;
        estaEntrenado = true;
        System.out.println("Entrenamiento completado exitosamente.");
    }
    
    public void mostrarDesempenio(){
        System.out.println("--- Reporte del Modelo ---");
        System.out.println("Algortimo: " + nombreAlgoritmo);
        System.out.println("Precison actual: " + precision);
        System.out.println("Estado de entrenamiento: " + estaEntrenado);
        
    }              
}

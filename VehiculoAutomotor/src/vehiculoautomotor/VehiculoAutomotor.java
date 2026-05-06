package vehiculoautomotor;

public class VehiculoAutomotor {
    protected double combustibleLitros;
    protected boolean encendido;

    // Constructor de la clase padre
    public VehiculoAutomotor(double litros) {
        this.combustibleLitros = litros;
        this.encendido = false;
    }

    // Método genérico
    public void arranconGen() {
        System.out.println("Arrancaste el coche.");
    }
}

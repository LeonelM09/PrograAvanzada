package vehiculoautomotor;

public class AutoTesla extends VehiculoAutomotor {
    // Atributo privado propio de la clase hija
    private double bateriaElectronica;

    // Constructor de la clase hija
    public AutoTesla(double litros, double bateriaElectronica) {
        // Llamada al constructor de la clase padre (VehiculoAutomotor)
        super(litros);
        // Inicialización del atributo propio
        this.bateriaElectronica = bateriaElectronica;
    }

    // Sobrescritura del método del padre
    @Override
    public void arranconGen() {
        System.out.println("El sistema de Autopilot dirige este arranque usando batería");
    }
}

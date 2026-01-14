class Car {
    public Car() {
        System.out.println("Class Car");
    }

    public void vehicleType() {
        System.out.println("Vehicle type: Car");
    }
}

class Maruti extends Car {
    public Maruti() {
        System.out.println("Class Maruti");
    }

    public void brand() {
        System.out.println("Brand is Maruti");
    }

    public void speed() {
        System.out.println("Max Speed: 90kmph");
    }
}

class Maruti800 extends Maruti {
    public Maruti800() {
        System.out.println("Class Maruti800");
    }

    public void speed() {
        System.out.println("Max Speed: 190kmph");
    }
}

class Cars {
    public static void main(String[] args) {
        Maruti800 maruti800 = new Maruti800();
        maruti800.vehicleType();
        maruti800.brand();
        maruti800.speed();
    }
}

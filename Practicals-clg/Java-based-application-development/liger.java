abstract class Animal{
    public abstract void sound();
}
class lion extends Animal{
    public void sound(){
        System.out.println("Sujal Santosh 18");
        System.out.println("lion rowrs!");
    }
}
class tiger extends Animal{
    public void sound(){
        System.out.println("Tiger growls");
    }
}
public class liger{
    public static void main(String[] args){
        Animal lion = new lion();
        lion.sound();
        Animal tiger = new tiger();
        tiger.sound();
    }
}
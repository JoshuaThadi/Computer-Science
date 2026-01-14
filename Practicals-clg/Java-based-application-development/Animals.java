abstract class animal{
    public abstract void sound();
}
class lion extends animal{
    public void sound(){
        System.out.print("Lion Roars !");
    }
}
class tiger extends animal{
    public void sound(){
        System.out.print("Tiger Growls !");
    }
}
public class Animals{
    public static void main(String[] args){
        animal lion = new lion();
        lion.sound();
        animal tiger = new tiger();
        tiger.sound();
    }
}
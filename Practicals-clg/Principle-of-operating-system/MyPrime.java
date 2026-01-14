// Practical No.2
/* WAP to work with a single thread */

// https://ctxt.io/2/AAB4QliPFA


class Prime implements Runnable {
    long c;
    Prime() {
        super();
        c = 0;
    }
    public void run() {
        for (long i = 2; i <= 100; i++) {  // Start from 2, as 1 is not considered prime
            boolean isPrime = true;
            for (long j = 2; j < i; j++) {  // Corrected condition to j < i
                if (i % j == 0) {
                    isPrime = false;
                    break;  // Exit loop if not prime
                }
            }
            if (isPrime) {  // Moved outside of the inner loop
                c++;
                System.out.println("\t\t" + c + " the Prime no. = " + i);
            }
        }
    }
}
public class MyPrime {
    public static void main(String[] args) {
        Thread ct = Thread.currentThread();
        System.out.println("\nMain Thread name: " + ct.getName());
        Prime p = new Prime();
        Thread prime = new Thread(p, "Prime");
        prime.start();
        System.out.println("\nThread " + prime.getName() + " started.");
    }
}
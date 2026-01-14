// Practical No.1
/* WAP to give a solution to the producer - consumer problem using message passing */

import java.util.Vector;

public class prac1_b {
    public static void main(String[] args) {
        Producer producer = new Producer();
        producer.start();
        new ConsumerThread(producer).start();
    }
}

class Producer extends Thread {
    static final int MAXQUEUE = 5;
    private final Vector<String> messages = new Vector<>();

    public void run() {
        try {
            while (true) {
                putMessage();
                sleep(1000);  // reduced sleep time to 1 second for testing purposes
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public synchronized void putMessage() throws InterruptedException {
        while (messages.size() >= MAXQUEUE) {
            wait();
        }
        messages.addElement(new java.util.Date().toString());
        notify();
    }

    public synchronized String getMessage() throws InterruptedException {
        while (messages.isEmpty()) {
            wait();
        }
        String message = messages.firstElement();
        messages.removeElement(message);
        notify();
        return message;
    }
}

class ConsumerThread extends Thread {
    private final Producer producer;

    ConsumerThread(Producer p) {
        producer = p;
    }

    public void run() {
        try {
            while (true) {
                String message = producer.getMessage();
                System.out.println("Got message: " + message);
                sleep(1000);  // reduced sleep time to 1 second for testing purposes
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

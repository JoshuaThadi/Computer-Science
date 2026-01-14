import javax.swing.*;

public class SimpleMenuExample {
    public static void main(String[] args) {

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);

        JMenuBar menuBar = new JMenuBar();

        JMenu menu1 = new JMenu("Menu 1");
        JMenuItem item_1 = new JMenuItem("Item 1-1");
        JMenuItem item_2 = new JMenuItem("Item 1-2");

        menu1.add(item_1);
        menu1.add(item_2);

        JMenu menu2 = new JMenu("Menu 2");
        JMenuItem item1_1 = new JMenuItem("Item 2-1");
        JMenuItem item1_2 = new JMenuItem("Item 2-2");

        menu2.add(item1_1);
        menu2.add(item1_2);

        menuBar.add(menu1);
        menuBar.add(menu2);

        frame.setJMenuBar(menuBar);
        frame.setVisible(true);
    }
}
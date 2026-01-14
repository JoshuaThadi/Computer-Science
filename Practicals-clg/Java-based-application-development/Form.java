import javax.swing.*;

public class Form {
    public static void main(String[] args) {
        JFrame f = new JFrame("Form Example");
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JLabel lb = new JLabel("Form Example");
        lb.setBounds(50, 50, 100, 50);
        f.add(lb);

        JLabel lb1 = new JLabel("Name : ");
        lb1.setBounds(100, 100, 100, 30);
        JTextField tf = new JTextField("Enter Name : ");
        tf.setBounds(200, 100, 150, 30);
        f.add(lb1);
        f.add(tf);

        JLabel lb2 = new JLabel("Password : ");
        lb2.setBounds(100, 150, 100, 30);
        JPasswordField pf = new JPasswordField();
        pf.setBounds(200, 150, 150, 30);
        f.add(lb2);
        f.add(pf);

        JLabel lb3 = new JLabel("Fruits : ");
        lb3.setBounds(100, 200, 100, 30);
        JCheckBox cb1 = new JCheckBox("Apple");
        cb1.setBounds(200, 200, 100, 30);
        JCheckBox cb2 = new JCheckBox("Banana");
        cb2.setBounds(200, 250, 100, 30);
        JCheckBox cb3 = new JCheckBox("Orange");
        cb3.setBounds(200, 300, 100, 30);
        f.add(lb3);
        f.add(cb1);
        f.add(cb2);
        f.add(cb3);

        JLabel lb4 = new JLabel("Gender : ");
        lb4.setBounds(100, 350, 100, 30);
        JRadioButton r1 = new JRadioButton("Male");
        r1.setBounds(200, 350, 100, 30);
        JRadioButton r2 = new JRadioButton("Female");
        r2.setBounds(200, 400, 100, 30);
        ButtonGroup bg = new ButtonGroup();
        bg.add(r1);
        bg.add(r2);
        f.add(lb4);
        f.add(r1);
        f.add(r2);

        JButton bt = new JButton("Submit");
        bt.setBounds(150, 450, 100, 30);
        f.add(bt);

        f.setLayout(null);
        f.setSize(400, 600);
        f.setVisible(true);
    }
}


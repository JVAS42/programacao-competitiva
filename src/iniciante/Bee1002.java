package iniciante;

import java.util.Scanner;

public class Bee1002 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double n = 3.14159;
        double raio = input.nextDouble();
        double area = n*(raio*raio);

        System.out.println(String.format("A=%.4f", area));

    }
}
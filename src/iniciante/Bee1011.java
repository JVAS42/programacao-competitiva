package iniciante;

import java.util.Scanner;

public class Bee1011 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double pi = 3.14159;
        double raio = input.nextDouble();
        double volume = (4 * pi * (raio*raio*raio))/3;

        System.out.println(String.format("VOLUME = %.3f", volume));

    }
}
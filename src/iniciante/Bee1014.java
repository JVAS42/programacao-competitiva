package iniciante;

import java.util.Scanner;

public class Bee1014 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int X = input.nextInt();
        float Y = input.nextFloat();
        float consumo = X/Y;

        System.out.println(String.format("%.3f km/l", consumo));
    }
}
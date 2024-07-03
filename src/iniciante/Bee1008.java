package iniciante;

import java.util.Scanner;

public class Bee1008 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int funcionarios = input.nextInt();
        int valorHora = input.nextInt();
        float horaTrabalhada = input.nextFloat();

        System.out.println(String.format("NUMBER = %d\nSALARY = U$ %.2f", funcionarios, (horaTrabalhada*valorHora)));
    }
}
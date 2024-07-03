package iniciante;

import java.util.Scanner;

public class Bee1018 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        int quantidadeNotas;
        int divisores[] = {100, 50, 20, 10, 5, 2, 1};

        System.out.println(n);
        for (int i = 0; i < 7; i++) {
            quantidadeNotas = (n/divisores[i]);
            n %= divisores[i];
            System.out.println(String.format("%d nota(s) de R$ %d,00", quantidadeNotas, divisores[i]));
        }

    }
}
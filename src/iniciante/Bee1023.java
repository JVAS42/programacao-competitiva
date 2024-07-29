package iniciante;

import java.util.Scanner;

public class Bee1023 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int quantidadeMoradores, consumoMoradores;
        int quantidadeMoradoresTotal = 0;
        int consumoTotal = 0;

        int n = input.nextInt();
        while (n != 0) {
            for (int i = 0; i < n; i++) {
                String[] residencia = input.nextLine().split(" ");
                quantidadeMoradores = Integer.parseInt(residencia[0]);
                consumoMoradores = Integer.parseInt(residencia[1]);
                System.out.println(quantidadeMoradores);
                System.out.println(consumoMoradores);
            }
            n = input.nextInt();
        }
    }
}

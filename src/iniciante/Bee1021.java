package iniciante;

import java.util.Scanner;

public class Bee1021 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        float valor = input.nextFloat();
        int quantidade;
        float notas[] = {100.00F, 50.00F, 20.00F, 10.00F, 5.00F, 2.00F};
        float moedas[] = {1.00F, 0.50F, 0.25F, 0.10F, 0.05F, 0.01F};

        System.out.println("NOTAS:");
        for (int i = 0; i < notas.length; i++) {
            quantidade = (int) (valor/notas[i]);
            valor = valor%notas[i];
            System.out.println(String.format("%d nota(s) de R$ %.2f", quantidade, notas[i]));
        }

        System.out.println("MOEDAS:");
        for (int i = 0; i < moedas.length; i++) {
            quantidade = (int) (valor/moedas[i]);
            valor = valor%moedas[i];
            System.out.println(String.format("%d moeda(s) de R$ %.2f", quantidade, moedas[i]));
        }
    }
}

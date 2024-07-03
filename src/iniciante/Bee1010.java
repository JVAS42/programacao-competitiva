package iniciante;

import java.util.Scanner;

public class Bee1010 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int codigoPeca;
        int quantPeca;
        float valorPeca;
        float valorTotal = 0;

        for (int i = 0; i < 2; i++) {
            codigoPeca = input.nextInt();
            quantPeca = input.nextInt();
            valorPeca = input.nextFloat();

            valorTotal = valorTotal+quantPeca*valorPeca;
        }
        System.out.println(String.format("VALOR A PAGAR: R$ %.2f", valorTotal));
    }
}
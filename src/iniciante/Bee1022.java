package iniciante;

import java.util.Scanner;

public class Bee1022 {

    /*
    Soma: (N1*D2 + N2*D1) / (D1*D2)
    Subtração: (N1*D2 - N2*D1) / (D1*D2)
    Multiplicação: (N1*N2) / (D1*D2)
    Divisão: (N1/D1) / (N2/D2), ou seja (N1*D2)/(N2*D1)
     */

    public static String soma (int n1, int n2, int d1, int d2) {
        int numerador = (n1*d2)+(n2*d1);
        int denominador = d1*d2;

        if (numerador%2 == 0 & denominador%2 == 0) {
        }

        return numerador + "/" + denominador;
    }

    public static int subtracao (int numero) {
        return 0;
    }

    public static int multiplicacao (int numero) {
        return 0;
    }

    public static int divisao (int numero) {
        return 0;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n1, n2, d1, d2;
        String operacaoMatematica;

        int n = input.nextInt();
        input.nextLine();

        for (int i = 0; i < n; i++) {
            String[] operacao = input.nextLine().split(" ");
            n1 = Integer.parseInt(operacao[0]);
            d1 = Integer.parseInt(operacao[2]);

            n2 = Integer.parseInt(operacao[4]);
            d2 = Integer.parseInt(operacao[6]);

            operacaoMatematica = operacao[3];

            switch (operacaoMatematica) {
                case "+":
                    System.out.println(String.format("%d/%d", (n1*d2+n2*d1), (d1*d2)));
                    break;
                case "-":
                    System.out.println(String.format("%d/%d", (n1*d2-n2*d1), (d1*d2)));
                    break;
                case "*":
                    System.out.println(String.format("%d/%d", (n1*n2), (d1*d2)));
                    break;
                case "/":
                    System.out.println(String.format("%d/%d", (n1*d2), (n2*d1)));
                    break;
            }
        }
    }
}

package iniciante;

import java.util.Scanner;

public class Bee1022 {

    public static int mdc(int a, int b) {
        a = Math.abs(a);
        b = Math.abs(b);
        if (b == 0) {
            return a;
        }
        return mdc(b, a % b);
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n1, n2, d1, d2;
        int numerador, denominador;
        String operacaoMatematica;

        int n = input.nextInt();
        input.nextLine();
        System.out.println();
        for (int i = 0; i < n; i++) {
            String[] operacao = input.nextLine().split(" ");
            n1 = Integer.parseInt(operacao[0]);
            d1 = Integer.parseInt(operacao[2]);

            n2 = Integer.parseInt(operacao[4]);
            d2 = Integer.parseInt(operacao[6]);

            operacaoMatematica = operacao[3];

            switch (operacaoMatematica) {
                case "+":
                    numerador = (n1*d2)+(n2*d1);
                    denominador = d1*d2;
                    if (numerador%2 == 0 && denominador%2 == 0) {
                        int numeradoSimplificado = numerador;
                        int denominadorSimplificado = denominador;
                        int divisorComum = mdc(numeradoSimplificado, denominadorSimplificado);
                        numeradoSimplificado /= divisorComum;
                        denominadorSimplificado /= divisorComum;
                        System.out.println(numerador+"/"+denominador+ " = "+numeradoSimplificado+"/"+denominadorSimplificado);
                    } else {
                        System.out.println(numerador+"/"+denominador);
                    }
                    break;
                case "-":
                    numerador = ((n1*d2)-(n2*d1));
                    denominador = d1*d2;
                    if (numerador%2 == 0 && denominador%2 == 0) {
                        int numeradoSimplificado = numerador;
                        int denominadorSimplificado = denominador;
                        int divisorComum = mdc(numeradoSimplificado, denominadorSimplificado);
                        numeradoSimplificado /= divisorComum;
                        denominadorSimplificado /= divisorComum;
                        System.out.println(numerador+"/"+denominador+ " = "+numeradoSimplificado+"/"+denominadorSimplificado);
                    } else {
                        System.out.println(numerador+"/"+denominador);
                    }
                    break;
                case "*":
                    numerador = n1*n2;
                    denominador = d1*d2;
                    if (numerador%2 == 0 && denominador%2 == 0) {
                        int numeradoSimplificado = numerador;
                        int denominadorSimplificado = denominador;
                        int divisorComum = mdc(numeradoSimplificado, denominadorSimplificado);
                        numeradoSimplificado /= divisorComum;
                        denominadorSimplificado /= divisorComum;
                        System.out.println(numerador+"/"+denominador+ " = "+numeradoSimplificado+"/"+denominadorSimplificado);
                    } else {
                        System.out.println(numerador+"/"+denominador);
                    }
                    break;
                case "/":
                    numerador = n1*d2;
                    denominador = n2*d1;
                    if (numerador%2 == 0 && denominador%2 == 0) {
                        int numeradoSimplificado = numerador;
                        int denominadorSimplificado = denominador;
                        int divisorComum = mdc(numeradoSimplificado, denominadorSimplificado);
                        numeradoSimplificado /= divisorComum;
                        denominadorSimplificado /= divisorComum;
                        System.out.println(numerador+"/"+denominador+ " = "+numeradoSimplificado+"/"+denominadorSimplificado);
                    } else {
                        System.out.println(numerador+"/"+denominador);
                    }
                    break;
            }
        }
    }
}

package iniciante;

import java.util.Scanner;

public class Bee1009 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String nome = input.nextLine();
        double salario = input.nextDouble();
        double valorVendas = input.nextDouble();

        double comissao = salario+(valorVendas*0.15);

        System.out.println(String.format("TOTAL = R$ %.2f", comissao));
    }
}
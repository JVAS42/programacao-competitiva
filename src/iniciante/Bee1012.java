package iniciante;

import java.util.Scanner;

public class Bee1012 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double A = input.nextDouble();
        double B = input.nextDouble();
        double C = input.nextDouble();
        double pi = 3.14159;

        double triangulo = (A*C)/2;
        double circulo = pi*(C*C);
        double trapezio = (A+B)*C/2;
        double quadrado = B*B;
        double retangulo = A*B;

        System.out.println(String.format(
                "TRIANGULO: %.3f"
                        +"\nCIRCULO: %.3f"
                        +"\nTRAPEZIO: %.3f"
                        +"\nQUADRADO: %.3f"
                        +"\nRETANGULO: %.3f",
                triangulo, circulo, trapezio, quadrado, retangulo
        ));
    }
}
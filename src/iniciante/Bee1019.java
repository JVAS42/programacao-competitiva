package iniciante;

import java.util.Scanner;
import java.time.Duration;

public class Bee1019 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int valorEmSegundos = input.nextInt();
        int tempoEmSegundos [] = {3600, 60};
        int quantidadeHoras, quantidadeMinutos;

        quantidadeHoras = valorEmSegundos/tempoEmSegundos[0];
        valorEmSegundos %= tempoEmSegundos[0];

        quantidadeMinutos = valorEmSegundos/tempoEmSegundos[1];
        valorEmSegundos %= tempoEmSegundos[1];

        System.out.println(String.format("%01d:%01d:%01d", quantidadeHoras, quantidadeMinutos, valorEmSegundos));
    }
}

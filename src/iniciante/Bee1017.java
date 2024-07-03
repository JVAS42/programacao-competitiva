package iniciante;

import java.util.Scanner;

public class Bee1017 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int mediaCarro = 12;
        float tempoGasto = input.nextFloat();
        float velocidadeMedia = input.nextFloat();

        float quantidadeLitros = (tempoGasto*velocidadeMedia)/mediaCarro;

        System.out.println(String.format("%.3f", quantidadeLitros));
    }
}
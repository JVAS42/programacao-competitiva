package iniciante;

import java.util.Scanner;

public class Bee1020 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int idadeEmDias = input.nextInt();
        int resultado;
        int vetorQuantEmDias [] = {365, 30};

        for (int i = 0; i <= 1; i++) {
            resultado = idadeEmDias/vetorQuantEmDias[i];
            idadeEmDias %= vetorQuantEmDias[i];
            if (i == 0) {
                System.out.println(resultado + " ano(s)");
            } else {
                System.out.println(resultado + " mes(es)");
            }
        }
        System.out.println(idadeEmDias + " dia(s)");
    }
}

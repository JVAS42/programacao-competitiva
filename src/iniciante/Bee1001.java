package iniciante;

import java.io.IOException;
import java.util.Scanner;

public class Bee1001 {

    public static void main(String[] args) throws IOException {
        int A;
        int B;


        Scanner input = new Scanner(System.in);

        A = input.nextInt();
        B = input.nextInt();

        int X = A + B;

        System.out.println("X = " + X);
    }

}
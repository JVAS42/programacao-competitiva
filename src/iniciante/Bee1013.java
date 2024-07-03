package iniciante;

import java.util.Scanner;
import java.lang.Math;

public class Bee1013 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int A = input.nextInt();
        int B = input.nextInt();
        int C = input.nextInt();

        int testaMaior = (A+B+Math.abs(A-B))/2;
        if (testaMaior == A) {
            testaMaior = (A+C+Math.abs(A-C))/2;
            if (testaMaior == A) {
                System.out.println(A+" eh o maior");
            } else {
                System.out.println(C+" eh o maior");
            }
        } else {
            testaMaior = (B+C+Math.abs(B-C))/2;
            if (testaMaior == B) {
                System.out.println(B+" eh o maior");
            } else {
                System.out.println(C+" eh o maior");
            }
        }

    }
}
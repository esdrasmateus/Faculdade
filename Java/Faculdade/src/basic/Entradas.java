package basic;

import java.util.Scanner;

public class Entradas {

    public static void main(String[] args) {

        Scanner leitor = new Scanner(System.in);

        int inteiro = leitor.nextInt();
        double real = leitor.nextDouble();
        boolean logico = leitor.nextBoolean();
        String cadeia = leitor.nextLine();

        System.out.println("O seu inteiro é: " + inteiro);
        System.out.println("O seu real é: " + real);
        System.out.println("O seu lógico é: " + logico);
        System.out.println("A sua palavra é: " + cadeia);

    }
}

package br.com.esdrasmateus.aulasjava;

import java.util.Scanner;

public class S03Tabuada {

    public static void main(String[] args){

        Scanner s = new Scanner(System.in);

        System.out.print("Digite um número inteiro positivo (Negativo para sair): ");

        int x = s.nextInt();

        while (x > 0){

            for (int cont = 1; cont <= 10; cont++){
                
                System.out.println( x + " X " + cont + " = " + (x * cont) + "\n" );
            }
        System.out.print("Digite outro número inteiro positivo (Negativo para sair): ");

        x = s.nextInt();

        }

        System.out.println("Você saiu");
    }
}

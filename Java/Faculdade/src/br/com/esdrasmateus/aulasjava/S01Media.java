package br.com.esdrasmateus.aulasjava;

import java.util.Scanner;

public class S01Media {

    public static void main(String[] args) {

        Scanner valor = new Scanner(System.in);

        System.out.print("Digite a sua primeira nota: ");

        float nota1 = valor.nextFloat();

        System.out.print("Digite a sua segunda nota: ");

        float nota2 = valor.nextFloat();

        System.out.print("Digite a sua terceira nota: ");

        float nota3 = valor.nextFloat();

        System.out.print("Digite a sua última nota: ");

        float nota4 = valor.nextFloat();

        float media = (nota1 + nota2 + nota3 + nota4) / 4;

        System.out.println("Sua média é: " + media);

    }
    
}

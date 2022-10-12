package br.com.esdrasmateus.aulasjava;

import java.util.Scanner;

public class S01PedeNumeroeSoma {

    public static void main(String[] args){

        Scanner leitor = new Scanner(System.in);

        System.out.print("Digite um número inteiro: ");

        int numero1 = leitor.nextInt();

        System.out.print("Digite um segundo número inteiro: ");

        int numero2 = leitor.nextInt();

        int numero3 = numero1 + numero2;

        System.out.print("A soma dos números é : " + numero3);
    }
}


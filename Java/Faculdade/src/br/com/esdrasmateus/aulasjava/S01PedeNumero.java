package br.com.esdrasmateus.aulasjava;

import java.util.Scanner;

public class S01PedeNumero {

    public static void main(String[] args){

        Scanner leitor = new Scanner(System.in);

        System.out.print("Digite um número: ");

        int numero = leitor.nextInt();

        System.out.println("O número digitado é: " + numero);
    }
    
}
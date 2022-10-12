package br.com.esdrasmateus.aulasjava;

import java.util.Scanner;

public class S02LerMaiorMenor {

    public static void main(String[] args){

        Scanner variaveis = new Scanner(System.in);

        System.out.print("Digite a primeira variável: ");

        float variavel1 = variaveis.nextFloat();

        System.out.print("Digite a segunda variável: ");

        float variavel2 = variaveis.nextFloat();

        System.out.print("Digite a terceira variável: ");

        float variavel3 = variaveis.nextFloat();

        if (variavel1 > variavel2 && variavel1 > variavel3){
            System.out.println("A maior variável é: " + variavel1);
        }else if (variavel2 > variavel3 && variavel2 > variavel1){
            System.out.println("A maior variável é: " + variavel2);
        }else if (variavel3 > variavel2 && variavel3 > variavel1){
            System.out.println("A maior variável é: " + variavel3);
        }

        if (variavel1 < variavel2 && variavel1 < variavel3){
            System.out.println("A menor variável é: " + variavel1);
        }else if (variavel2 < variavel3 && variavel2 < variavel1){
            System.out.println("A menor variável é: " + variavel2);
        }else if (variavel3 < variavel2 && variavel3 < variavel1){
            System.out.println("A menor variável é: " + variavel3);
        }
    }
    
}

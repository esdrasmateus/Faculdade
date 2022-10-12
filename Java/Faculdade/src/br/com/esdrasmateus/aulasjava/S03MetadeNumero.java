package br.com.esdrasmateus.aulasjava;

import java.util.Scanner;

public class S03MetadeNumero {
    public static void main(String[] args){

        Scanner s = new Scanner(System.in);

        System.out.print("Digite um número (negativo para sair): ");

        float x = s.nextFloat();

        while (x > 0) {

            System.out.println("A metade do número é: " + (x / 2));
            
            System.out.print("Digite outro número (negativo para sair): ");
            x = s.nextFloat();
        
        }
        System.out.println("Você saiu");
    }
    
}

package br.com.esdrasmateus.aulasjava;

import java.util.Scanner;
import java.util.ArrayList;

public class S03Impares {

    public static void main(String[] args){

        Scanner s = new Scanner(System.in);
        
        ArrayList<Integer> lista = new ArrayList();

        System.out.println("Digite um número inteiro: ");

        for (int x = 0; x < 10; x++) {
            int numero = s.nextInt();

            if (numero % 2 != 0){

                lista.add(numero);
            }
        }
        
        System.out.print("Os números ímpares são: " + lista);
    }
    
}

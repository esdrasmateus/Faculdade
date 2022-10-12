package br.com.esdrasmateus.aulasjava;

import java.util.Scanner;

public class S04ArrayInverso {

    public static void main(String[] args){

        int array[] = new int[10];

        Scanner s = new Scanner(System.in);

        for (int i = 0; i < array.length; i++) {
            
            System.out.println("Digite um número real: ");
            array[i] = s.nextInt();
        }
        for (int i = array.length - 1; i >= 0; i--) {
            System.out.println("Os números em ordem inversa são: " + array[i]);    
        }
    }
    
}

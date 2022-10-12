package br.com.esdrasmateus.aulasjava;

import java.util.Scanner;

public class S04ArrayAltura {

    public static void main(String[] args){

        double array[] = new double[5];

        Scanner s = new Scanner(System.in);

        for (int i = 0; i < array.length; i++) {
            
            System.out.println("Digite a sua altura: ");
            array[i] = s.nextDouble();
        }
        for (int i = array.length - 1; i >= 0; i--) {
            System.out.println("As alturas em ordem inversa são: " + array[i]);    
        }
    }
    
}

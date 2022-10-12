package br.com.esdrasmateus.aulasjava;

import java.util.Scanner;

public class S02Triangulo {

    public static void main(String[] args){

        Scanner s = new Scanner(System.in);

        System.out.print("Digite o primeiro lado do triângulo: ");

        float lado1 = s.nextFloat();

        System.out.print("Digite o segundo lado do triângulo: ");

        float lado2 = s.nextFloat();

        System.out.print("Digite o terceiro lado do triângulo: ");

        float lado3 = s.nextFloat();

        if (lado1 + lado2 < lado3 || lado2 + lado3 < lado1 || lado3 + lado1 < lado2 ){
            System.out.println("Triângulo inválido");
            System.exit(0);
        }else if (lado1 == lado2 && lado1 == lado3){
            System.out.println("Os três lados formam um triângulo, e ele é equilátero");
            System.exit(0);
        }else if (lado1 == lado2 || lado1 == lado3 || lado2 == lado3){
            System.out.println("Os três lados formam um triângulo, e ele é isósceles");
        }else if (lado1 != lado2 && lado1 != lado3 && lado2 != lado3){
            System.out.println("Os três lados formam um triângulo, e ele é escaleno");
        }
    }   
}

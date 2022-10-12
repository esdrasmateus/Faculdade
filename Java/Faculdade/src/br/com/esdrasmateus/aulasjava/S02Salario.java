package br.com.esdrasmateus.aulasjava;

import java.util.Scanner;

public class S02Salario {

    public static void main(String[] args){

        Scanner s = new Scanner(System.in);

        System.out.print("Informe o seu salário: ");
        double salario = s.nextDouble();
        double total, percentual;

        if (salario <= 280){
            percentual = (salario * 0.20);
            total = salario + percentual;
            System.out.print("O salário antes do reajuste era de: ");
            System.out.printf("%.2f", salario);
            System.out.print(". O percentual de aumento aplicado foi de 20% e o valor do aumento foi de: ");
            System.out.printf("%.2f", percentual);
            System.out.print(". O novo salário é de: ");
            System.out.printf("%.2f", total);
        }else if (salario > 280 && salario < 700){
            percentual = (salario * 0.15);
            total = salario + percentual;
            System.out.print("O salário antes do reajuste era de: ");
            System.out.printf("%.2f", salario);
            System.out.print(". O percentual de aumento aplicado foi de 15% e o valor do aumento foi de: ");
            System.out.printf("%.2f", percentual);
            System.out.print(". O novo salário é de: ");
            System.out.printf("%.2f", total);
        }else if (salario >= 700 && salario < 1500){
            percentual = (salario * 0.10);
            total = salario + percentual;
            System.out.print("O salário antes do reajuste era de: ");
            System.out.printf("%.2f", salario);
            System.out.print(". O percentual de aumento aplicado foi de 10% e o valor do aumento foi de: ");
            System.out.printf("%.2f", percentual);
            System.out.print(". O novo salário é de: ");
            System.out.printf("%.2f", total);
        }else if (salario >= 1500){
            percentual = (salario * 0.5);
            total = salario + percentual;
            System.out.print("O salário antes do reajuste era de: ");
            System.out.printf("%.2f", salario);
            System.out.print(". O percentual de aumento aplicado foi de 5% e o valor do aumento foi de: ");
            System.out.printf("%.2f", percentual);
            System.out.print(". O novo salário é de: ");
            System.out.printf("%.2f", total);
        }
    }
}

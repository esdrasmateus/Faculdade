package br.com.esdrasmateus.aulasjava;

import java.util.Scanner;

public class VetoresLeo2 {

    public static void main (String[] args){

        int var1 = 0;

        double vetGanhos[] = new double[12], vetGastos[] = new double[12], vetLucros[] = new double[12], soma = 0, media = 0; 

        Scanner s = new Scanner(System.in);

        for (int i = 0; i < vetGanhos.length; i++){

            System.out.printf("Informe %2dº. valor de %d para os meses de ganhos: ", (i+1), vetGanhos.length);
            vetGanhos[i] = s.nextDouble(); 
        }

        for (int i = 0; i < vetGastos.length; i++){

            System.out.printf("Informe %2dº. valor de %d para os meses de gastos: ", (i+1), vetGastos.length);
            vetGastos[i] = s.nextDouble(); 
        }

        for (int i = 0; i < vetLucros.length; i++){

            double subtração = vetGanhos[i] - vetGastos[i];
            
            vetLucros[i] = subtração;
        }

        System.out.print("\nDigite 0 para terminar o programa, 1 para mostrar os meses de ganhos, 2 para os meses de gastos e 3 para os meses de lucros, \n4 para mostrar a soma dos ganhos, 5 para a soma dos gastos e 6 para a soma dos lucros: ");
        var1 = s.nextInt();

        while (var1 != 0){
            if (var1 == 1) {
                for (int i = 0; i < vetGanhos.length; i++) {
                    System.out.print("\nO valor do " + (i+1) + "º mês de ganhos é: " + vetGanhos[i]);
                }
            } if (var1 == 2) {
                for (int i = 0; i < vetGastos.length; i++) {
                    System.out.print("\nO valor do " + (i+1) + "º mês de gastos é: " + vetGastos[i]);
                }
            } if (var1 == 3) {
                for (int i = 0; i < vetLucros.length; i++) {
                    System.out.print("\nO valor do " + (i+1) + "º mês de lucros é: " + vetLucros[i]);
                }
            } if (var1 == 0) {
                System.exit(0);
            } if (var1 == 4) {
                for (double valor : vetGanhos) {
                    soma += valor;
                }
                System.out.println("O valor da soma para os ganhos é de: " + soma);
            } if (var1 == 5) {
                for (double valor : vetGastos) {
                    soma += valor;
                }
                System.out.println("O valor da soma para os gastos é de: " + soma);
            } if (var1 == 6) {
                for (double valor : vetLucros) {
                    soma += valor;
                }
                System.out.println("O valor da soma para os lucros é de: " + soma);
            }
            soma = 0;
            System.out.print("\nDigite 0 para terminar o programa, 1 para mostrar os meses de ganhos, 2 para os meses de gastos e 3 para os meses de lucros, \n4 para mostrar a soma dos ganhos, 5 para a soma dos gastos e 6 para a soma dos lucros: ");
            var1 = s.nextInt();
        }
    }
}
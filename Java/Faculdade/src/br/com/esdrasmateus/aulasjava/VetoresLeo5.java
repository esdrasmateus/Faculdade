package br.com.esdrasmateus.aulasjava;

import java.util.Scanner;

public class VetoresLeo5 {

    public static void main(String[] args){

        int vetA[] = new int[50], vetB[] = new int[50], var1 = 0, var2 = 0, indiceImpar = 0, indicePar = 0, temp1, temp2;
        
        Scanner s = new Scanner(System.in);

        System.out.print("Digite 1 para armazenar números, 2 para procurar números, 3 para exibir os números pares, \n4 para exibir os números ímpares e 5 para encerrar o programa: ");
        var1 = s.nextInt();

        if (var1 == 1){

            System.out.print("Digite 1 para armazenar números pares ou 2 para armazenar os números ímpares: ");
            var2 = s.nextInt();

            if (var2 == 1){
                for (int i = 0; i < vetA.length; i++){
                    System.out.printf("Informe o %dº. número par a ser guardado de um total de 50 números: ", (i+1));
                    temp1 = indicePar;
                    indicePar = s.nextInt();

                    if (indicePar % 2 == 0 && indicePar != temp1){
                        vetA[i] = indicePar;
                        System.out.print("Você quer continuar armazenando números? Se sim digite 1, se não, escolha outra opção, sendo elas: \n2 para procurar números, \n3 para exibir os números pares, \n4 para exibir os números ímpares ou \n5 para encerrar o programa: ");
                        var1 = s.nextInt();
                    } else {
                        System.out.println("O número informado precisa ser um número par e não pode ser um número repetido");
                        i--;
                    }

                }

            } else if (var2 == 2){
                for (int i = 0; i < vetB.length; i++){
                    System.out.printf("Informe o %dº. número ímpar a ser guardado de um total de 50 números: ", (i+1));
                    temp2 = indiceImpar;
                    indiceImpar = s.nextInt();

                    if (indiceImpar % 2 != 0 && indiceImpar != temp2){
                        vetB[i] = indiceImpar;
                        System.out.print("Você quer continuar armazenando números? Se sim digite 1, se não, escolha outra opção, sendo elas: \n2 para procurar números, \n3 para exibir os números pares, \n4 para exibir os números ímpares ou \n5 para encerrar o programa: ");
                        var1 = s.nextInt();
                    } else {
                        System.out.println("O número informado precisa ser um número ímpar e não pode ser um número repetido");
                        i--;
                    }

                }
            }

        } else if (var1 == 2){
            System.out.print("Digite 1 para procurar números pares ou 2 para procurar números ímpares: ");
            var2 = s.nextInt();

            if (var2 == 1){
                System.out.printf("Você tem %d números pares. Qual deles você quer mostrar? ", (vetA.length));
                int posicao = s.nextInt();
                if (posicao <= vetA.length){
                    System.out.print(vetA[posicao]);
                } else {
                    System.out.print("-1");
                }

                System.out.print("Você quer continuar mostrando números? Se sim digite 2, se não, escolha outra opção, sendo elas: \n1 para armazenar números, \n3 para exibir os números pares, \n4 para exibir os números ímpares ou \n5 para encerrar o programa: ");
                var1 = s.nextInt();

            } else if (var2 == 2){
                System.out.printf("Você tem %d números ímpares. Qual deles você quer mostrar? ", (vetB.length));
                int posicao = s.nextInt();
                if (posicao <= vetB.length){
                    System.out.print(vetB[posicao]);
                } else {
                    System.out.print("-1");
                }

                System.out.print("Você quer continuar mostrando números? Se sim digite 2, se não, escolha outra opção, sendo elas: \n1 para armazenar números, \n3 para exibir os números pares, \n4 para exibir os números ímpares ou \n5 para encerrar o programa: ");
                var1 = s.nextInt();
            }

        } else if (var1 == 3){
            for (int i = 0; i < vetA.length; i++){
                System.out.println("\nOs números pares são: " + vetA[i]);
            }
            System.out.print("Você quer continuar mostrando os números pares? Se sim digite 3, se não, escolha outra opção, sendo elas: \n1 para armazenar números, \n3 para exibir os números pares, \n4 para exibir os números ímpares ou \n5 para encerrar o programa: ");
            var1 = s.nextInt();

        } else if (var1 == 4){
            for (int i = 0; i < vetB.length; i++){
                System.out.println("\nOs números ímpares são :" + vetB[i]);
            }
            System.out.print("Você quer continuar mostrando os números ímpares? Se sim digite 4, se não, escolha outra opção, sendo elas: \n1 para armazenar números, \n3 para exibir os números pares, \n4 para exibir os números ímpares ou \n5 para encerrar o programa: ");
            var1 = s.nextInt();

        } else if (var1 == 5){
            System.exit(0);
        }
    }
}

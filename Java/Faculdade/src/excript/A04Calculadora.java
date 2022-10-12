package excript;

import java.util.Scanner;

public class A04Calculadora {

    public static void main(String[] args){

        Scanner in = new Scanner(System.in);

        System.out.println("Digite 1 para somar");
        System.out.println("Digite 2 para subtrair");
        System.out.println("Digite 3 para dividir");
        System.out.println("Digite 4 para multiplicar");

        int i = in.nextInt();

        if (i < 1 || i > 4){
            System.out.println("Opção inválida");
            System.exit(0);
        }

        System.out.print("Digite o primeiro número: ");
        double num1 = in.nextDouble();

        System.out.print("Digite o segundo número : ");
        double num2 = in.nextDouble();

        if (i == 1){
            System.out.println("A soma é: " + (num1 + num2));
            }else if (i == 2){
                System.out.println("A subtração é: " + (num1 - num2));
            }else if (i == 3){
                System.out.println("A divisão é: " + (num1 / num2));
            }else if (i == 4){
                System.out.println("A multiplicação é: " + (num1 * num2));
            }
        }
    }

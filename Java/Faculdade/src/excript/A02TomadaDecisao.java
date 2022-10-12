package excript;

import java.util.Scanner;

public class A02TomadaDecisao {

    public static void main(String[] args){

        System.out.print("Digite um número: ");

        Scanner in = new Scanner(System.in);

        int num = in.nextInt();

        if(num == 10){

            System.out.println("Sim, é igual a 10");
        }else{
            System.out.println("Não, não é igual a 10");
            
        }
    }
}

package excript;

import java.util.Scanner;

public class A03OperadoresLogicos {

    public static void main(String[] args){

        Scanner in = new Scanner(System.in);
        System.out.print("Digite a idade da pessoa: ");
        
        final int iJ, iI;

        iJ = 17;

        iI = 60;

        int idade = in.nextInt();

        if (idade <= iJ){
            System.out.println("A pessoa é jovem");
        }else if (idade >= 60){
            System.out.println("A pessoa é idosa");
        }else if (idade > iJ && idade < iI){
            System.out.println("A pessoa é  jovem ou de meia idade");
        }
    }
    
}

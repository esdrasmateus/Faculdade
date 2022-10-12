package br.com.esdrasmateus.aulasjava;

import java.util.Scanner;

public class VetoresLeo4 {
    
    public static void main(String[] args) {

        int x = 0, y = 0, total = 0, var2 = 1;
        String var1 = "S";
        double percBranco = 0, percJoao = 0, percMaria = 0, percPedro = 0, percLuis = 0, percAna = 0, percLuiza = 0, percSilvia = 0, percAndre = 0, percNulo = 0;
        Scanner s = new Scanner(System.in);

        int vetBranco[] = new int[100], vetJoao[] = new int[100], vetMaria[] = new int[100], vetPedro[] = new int[100], vetLuis[] = new int[100], vetAna[] = new int[100],
        vetLuiza[] = new int[100], vetSilvia[] = new int[100], vetAndre[] = new int[100], vetNulo[] = new int[100];
        
        System.out.println("Suas opções de voto são: \n0 para Branco \n1 para João \n2 para Maria \n3 para Pedro \n4 para Luís \n5 para Ana \n6 para Luiza \n7 para Silvia \n8 para André \n(Qualquer número diferente dos citados será contato como voto nulo)");
        
        while (var2 == 1) {
            
            y = s.nextInt();
            
            if (y == 1){
                x =+ 1;
                vetJoao[x] =+ 1;
            } else if (y == 2){
                x =+ 1;
                vetMaria[x] =+ 1;
            } else if (y == 3){
                x =+ 1;
                vetPedro[x] =+ 1;
            } else if (y == 4){
                x =+ 1;
                vetLuis[x] =+ 1;
            } else if (y == 5){
                x =+ 1;
                vetAna[x] =+ 1;
            } else if (y == 6){
                x =+ 1;
                vetLuiza[x] =+ 1;
            } else if (y == 7){
                x =+ 1;
                vetSilvia[x] =+ 1;
            } else if (y == 8){
                x =+ 1;
                vetAndre[x] =+ 1;
            } else if (y == 0){
                x =+ 1;
                vetBranco[x] =+ 1;
            } else if (y != 1 && y != 2 && y != 3 && y != 4 && y != 5 && y != 6 && y != 7 && y != 8 && y != 9){
                x =+ 1;
                vetNulo[x] =+ 1;
            }
            total += 1;
            System.out.print("Ainda existe alguém para votar? Digite 's' ou 'S' para sim e 'n' ou 'N' para não: ");
            var1 = s.next();
            if (var1 == "s" || var1 == "S"){
                var2 = 1;
            } else if (var1 == "n" || var1 == "N"){
                var2 = 0;
            }
        }

        for (double valor : vetBranco){
            percBranco = (valor / total);
        }
        for (double valor : vetJoao){
            percJoao = (valor / total);
        }
        for (double valor : vetMaria){
            percMaria = (valor / total);
        }
        for (double valor : vetPedro){
            percPedro = (valor / total);
        }
        for (double valor : vetLuis){
            percLuis = (valor / total);
        }
        for (double valor : vetAna){
            percAna = (valor / total);
        }
        for (double valor : vetLuiza){
            percLuiza = (valor / total);
        }
        for (double valor : vetSilvia){
            percSilvia = (valor / total);
        }
        for (double valor : vetAndre){
            percAndre = (valor / total);
        }
        for (double valor : vetNulo){
            percNulo = (valor / total);
        }

        System.out.println("A porcentagem de votos para os candidados e de nulos e brancos foi: \nJoao: " + percJoao + "%\nMaria: " + percMaria + "%\nPedro: " + percPedro + "%\nLuís: " + percLuis + "%\nAna: " + percAna + "%\nLuiza: " + percLuiza + "%\nSilvia: " + percSilvia + "%\nAndré: " + percAndre + "%\nBrancos: " + percBranco + "%\nNulos: " + percNulo + "%");

    }
}

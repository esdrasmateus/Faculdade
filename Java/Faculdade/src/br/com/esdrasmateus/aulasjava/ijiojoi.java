package br.com.esdrasmateus.aulasjava;
import java.util.Scanner;
import java.security.SecureRandom;
public class ijiojoi {


    public static void main(String[] args) {
     Scanner input = new Scanner(System.in);  
  
      int resp,cont;
      int [] [] jogoVelha =  new int [3][3];
     do{ 
    opcaoMenu();
    resp= input.nextInt();
     while(resp!=1 && resp!=2){
     System.out.println("por favor , escolha [1] para um jogador ou [2] para dois jogadores");   
     resp=input.nextInt();
     }
    if (resp==2){
      jogoDoisJogadores(jogoVelha);  
    } 
    if(resp==1){
      
     System.out.println("Em Qual Modo Voce Quer Jogar?");
     System.out.println("Digite [1] para facil");
     System.out.println("Digite [2] para dificil");     
     
     resp= input.nextInt();
     while(resp!=1 && resp !=2){
         
      System.out.println("digito errado , por favor digite 1 para facil e 2 para dificil");
      resp=input.nextInt();
     }
     
     if (resp==1){
         jogoRoboFacil(jogoVelha);
     }else{
         jogoRoboDificil(jogoVelha);
     }
     
     
    }
    System.out.println("deseja jogar novamente? Digite 1 pra sim e 2 pra não");
    cont=input.nextInt();
    
   while(cont!=1 && cont!=2){
       
      System.out.println("erro ao digitar , digite 1 para continuar ou 2 para encerrar"); 
      cont=input.nextInt();
   } 
    
    }while(cont==1);
    }
   public static void opcaoMenu(){
       
    
   
   System.out.println("Bem vindo ao jogo da velha ");
     System.out.println("Escolha a seguinte opcão");
       System.out.println("[1] Um jogador");
         System.out.println("[2]Dois jogadores");
         
     
    
       
       
       
   }
   public static void jogoDoisJogadores(int [] [] jogoVelha){
   SecureRandom random = new SecureRandom();
   
    
   Scanner input = new Scanner(System.in);
   String jogador1,jogador2;
   int jog1=1, jog2=-1, validacao,linha,coluna,j,flag=0;
   
   System.out.println("informe o nome do jogador 1");
   jogador1= input.nextLine();
   System.out.println("Agora informe o nome do jogador 2");
   jogador2= input.nextLine();
   
   int i =  random.nextInt(2);
   
   System.out.println("Sorteio para saber quem comeca primeiro , se o numero sorteado for 0 o jogador 1 será primera , se 1 o jogador 2 comecará");
   System.out.println("o numero sorteado foi "+i);
   
   
   
   if(i==0){
       
   System.out.println("Jogador 1 irá comecar a jogar primeiro");
  do{ 
  exibirJogo(jogoVelha);
  preenchimento(jogoVelha,1);
  
  checarVelha(jogoVelha);
  testeVitoria(jogoVelha);
  if(checarVelha(jogoVelha)==1){
   System.out.println("o jogo deu velha , ninguem ganhou");
   break;
  } if(testeVitoria(jogoVelha)==1){
    System.out.println("o jogador 1 ganhou , parebens!!!!");  
    break;  
  }
  
  
  exibirJogo(jogoVelha);
  System.out.println("jogador 2 , sua vez de jogar");
  preenchimento(jogoVelha,-1);
  
  if(checarVelha(jogoVelha)==1){
   System.out.println("o jogo deu velha , ninguem ganhou");
   break;}
  
  if(testeVitoria(jogoVelha)==-1){
    System.out.println("o jogador 2 ganhou , parabens!!!!!");
    break;
 
  
  }
  
  
   
   
   
   
   
   
   
   
    }while(flag==0);
   
   }else{
       
    System.out.println("o primeiro a jogar é o jogador 2");   
   do{  
    exibirJogo(jogoVelha);
  System.out.println("jogador 2 , sua vez de jogar");
  preenchimento(jogoVelha,-1);
  
  if(checarVelha(jogoVelha)==1){
   System.out.println("o jogo deu velha , ninguem ganhou");
   break;
  }
  
  if(testeVitoria(jogoVelha)==-1){
    System.out.println("o jogador 2 ganhou , parabens!!!!!");
    break;
 
  
  }  
       
  exibirJogo(jogoVelha);
  preenchimento(jogoVelha,1);
  
  checarVelha(jogoVelha);
  testeVitoria(jogoVelha);
  if(checarVelha(jogoVelha)==1){
   System.out.println("o jogo deu velha , ninguem ganhou");
   break;
  } if(testeVitoria(jogoVelha)==1){
    System.out.println("o jogador 1 ganhou , parebens!!!!");  
    break;  
  }     
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
   }while(flag==0);
   }
   }
  public static int checarLinha(int [][] jogoVelha){
     
  
   
  for(int linha=0 ; linha<3 ; linha++){

    if( (jogoVelha[linha][0] + jogoVelha[linha][1]+ jogoVelha[linha][2]) == -3){
    return -1;
  } if( (jogoVelha[linha][0] + jogoVelha[linha][1]+ jogoVelha[linha][2]) == 3) {
    return 1;  
  }         
   }
return 0;
      
  }
  public static int checarVelha(int [][] jogoVelha){
      
  for(int linha=0; linha<3; linha++){
      
  for(int coluna=0;coluna<3;coluna++){
    if(jogoVelha[linha][coluna] == 0)    
        return 0;
    }  
   }    
  return 1;  
  }
 public static int checarColuna(int [][] jogoVelha){
  
     
     for(int coluna=0 ; coluna<3 ; coluna++){

    if( (jogoVelha[0][coluna] + jogoVelha[1][coluna]+ jogoVelha[2][coluna]) == -3){
    return -1;
  } if( (jogoVelha[0][coluna] + jogoVelha[1][coluna]+ jogoVelha[2][coluna]) == 3) {
    return 1;  
  }         
   }
return 0;   
 }
  
 public static int checarDiagonal(int [][] jogoVelha){
     
 if( (jogoVelha[0][0]+ jogoVelha[1][1]+ jogoVelha[2][2] ==3 )){
    return 1; 
 } if( (jogoVelha[0][0]+ jogoVelha[1][1]+ jogoVelha[2][2] == -3 )){ 
    return -1;
 }if ( (jogoVelha[0][2]+ jogoVelha[1][1]+ jogoVelha[2][0] ==3 )){
    return 1;
 }if ( (jogoVelha[0][2]+ jogoVelha[1][1]+ jogoVelha[2][0] == -3 )){
    return -1;}
 
 
 return 0;
 }
    

 public static void exibirJogo(int [][] jogoVelha){
 System.out.println();
 int linha=0,coluna=0;
 
  for(linha=0;linha<3;linha++){
      
   for(coluna=0;coluna<3;coluna++){
       
      if(jogoVelha[linha][coluna]==-1){
                    System.out.print(" X ");
                }
                if(jogoVelha[linha][coluna]==1){
                    System.out.print(" 0 ");
                }
                if(jogoVelha[linha][coluna]==0){
                    System.out.print("   ");
                }
                
                if(coluna==0 || coluna==1)
                    System.out.print("|");
       
       
       
       
   }   
  System.out.println();
      
      
  }
      
      
  }
 
  public static int testeVitoria(int [][] jogoVelha){
      
      
   if(checarLinha(jogoVelha)== 1){
     return 1;   
   }if (checarColuna(jogoVelha)==1){
     return 1;  
   }if (checarDiagonal(jogoVelha)==1){
      return 1; 
   }if(checarLinha(jogoVelha)== -1){
     return -1;   
   }if (checarColuna(jogoVelha)==-1){
     return -1;  
   }if (checarDiagonal(jogoVelha)==-1){
      return -1;  
  }else{
    return 0;  
  }
  }
  
  public static int preenchimento(int [][] jogoVelha , int i){
     Scanner input = new Scanner(System.in); 
      int linha,coluna;
      
    if(i==1){
        
        System.out.println("linha = ");
    linha=input.nextInt();
    while(linha <0 || linha>2){
      System.out.println("por favor insira um valor de 0 a 2 para linha"); 
      linha=input.nextInt();
    }
   System.out.println("coluna= ");
    coluna=input.nextInt();
   while(coluna <0 || coluna>2){
      System.out.println("por favor insira um valor de 0 a 2 para a coluna"); 
       coluna=input.nextInt();
    }
   
   while(jogoVelha[linha][coluna] != 0){
     
    System.out.println("Posicao ja ocupada , insira outra linha e coluna para fazer o preenchimento"); 
     System.out.println("linha = ");
    linha=input.nextInt();
    while(linha <0 || linha>2){
      System.out.println("por favor insira um valor de 0 a 2 para linha"); 
      linha=input.nextInt();
    }
   System.out.println("coluna= ");
    coluna=input.nextInt();
   while(coluna <0 || coluna>2){
      System.out.println("por favor insira um valor de 0 a 2 para a coluna"); 
      coluna=input.nextInt();
   }
  
    }      
    jogoVelha[linha][coluna]=1;
    return 0;
    }
    
    else{
        System.out.println("linha = ");
    linha=input.nextInt();
    while(linha <0 || linha>2){
      System.out.println("por favor insira um valor de 0 a 2 para linha"); 
      linha=input.nextInt();
    }
   System.out.println("coluna= ");
    coluna=input.nextInt();
   while(coluna <0 || coluna>2){
      System.out.println("por favor insira um valor de 0 a 2 para a coluna"); 
      coluna=input.nextInt();
    }
   
   while(jogoVelha[linha][coluna] != 0){
     
    System.out.println("Posicao ja ocupada , insira outra linha e coluna para fazer o preenchimento"); 
     System.out.println("linha = ");
    linha=input.nextInt();
    while(linha <0 || linha>2){
      System.out.println("por favor insira um valor de 0 a 2 para linha"); 
      linha=input.nextInt();
    }
   System.out.println("coluna= ");
    coluna=input.nextInt();
   while(coluna <0 || coluna>2){
      System.out.println("por favor insira um valor de 0 a 2 para a coluna"); 
      coluna=input.nextInt();
   }
  
    }      
    jogoVelha[linha][coluna]=-1;
    return 0;
    }

    }
        
   
public static void jogoRoboFacil(int [][] jogoVelha){
  SecureRandom random = new SecureRandom();
  Scanner input = new Scanner(System.in);
  int b=0;
  String jogador;
  System.out.println("informe o seu nome");

   jogador= input.nextLine();
   
  System.out.println("Bem vindo "+jogador+", iremos fazer 0 ou 1 pare ver se voce ou o robo comeca o jogo");
  
  int i =  random.nextInt(2);
  
 if(i==0){
   System.out.println("o sorteio resultou em zero , voce comeca a jogar");
   
  do{
  exibirJogo(jogoVelha);
  preenchimento(jogoVelha,1);
  
  checarVelha(jogoVelha);
  testeVitoria(jogoVelha);
  if(checarVelha(jogoVelha)==1){
   System.out.println("o jogo deu velha , ninguem ganhou");
   break;
  } if(testeVitoria(jogoVelha)==1){
    System.out.println("o jogador 1 ganhou , parebens!!!!");  
    break;  
  }
  
  
  preenchimentoRoboFacil(jogoVelha,-1);
  exibirJogo(jogoVelha);
   
  checarVelha(jogoVelha);
  testeVitoria(jogoVelha);
  if(checarVelha(jogoVelha)==1){
   System.out.println("o jogo deu velha , ninguem ganhou");
   break;
  } if(testeVitoria(jogoVelha)==-1){
    System.out.println("o ROBO ganhou , voce foi derrotado!!!!");  
    break;  
  }
 }while(b==0);

 }else{
    System.out.println("o sorteio deu 1 e o robo irá jogar primeiro"); 
     
  do{   
     preenchimentoRoboFacil(jogoVelha,-1);
  exibirJogo(jogoVelha);
   
  checarVelha(jogoVelha);
  testeVitoria(jogoVelha);
  if(checarVelha(jogoVelha)==1){
   System.out.println("o jogo deu velha , ninguem ganhou");
   break;
  } if(testeVitoria(jogoVelha)==-1){
    System.out.println("o ROBO ganhou , Voce foi derrotado!!!!");  
    break;  
  }
   
  System.out.println("sua vez");
  exibirJogo(jogoVelha);
  preenchimento(jogoVelha,1);
  
  checarVelha(jogoVelha);
  testeVitoria(jogoVelha);
  if(checarVelha(jogoVelha)==1){
   System.out.println("o jogo deu velha , ninguem ganhou");
   break;
  } if(testeVitoria(jogoVelha)==1){
    System.out.println("o jogador  ganhou , parebens!!!!");  
    break;  
  }      
 }while(b==0);
}
}
public static void jogoRoboDificil(int[][] jogoVelha){
    
     SecureRandom random = new SecureRandom();
  Scanner input = new Scanner(System.in);
  int b=0,flag;
  String jogador;
  System.out.println("informe o seu nome");

   jogador= input.nextLine();
   
  System.out.println("Bem vindo "+jogador+", iremos fazer 0 ou 1 pare ver se voce ou o robo comeca o jogo");
  
  int i =  random.nextInt(2);
  
 if(i==0){
   System.out.println("o sorteio resultou em zero , voce comeca a jogar");
   
  do{
  exibirJogo(jogoVelha);
  preenchimento(jogoVelha,1);
  
  checarVelha(jogoVelha);
  testeVitoria(jogoVelha);
  if(checarVelha(jogoVelha)==1){
   System.out.println("o jogo deu velha , ninguem ganhou");
   break;
  } if(testeVitoria(jogoVelha)==1){
    System.out.println("o jogador 1 ganhou , parebens!!!!");  
    break;  
  }
  
  preenchimentoRoboDificil(jogoVelha,-1);
  
  checarVelha(jogoVelha);
  testeVitoria(jogoVelha);
  if(checarVelha(jogoVelha)==1){
   System.out.println("o jogo deu velha , ninguem ganhou");
   break;
  } if(testeVitoria(jogoVelha)==-1){
    System.out.println("o ROBO ganhou , voce foi derrotado!!!!");  
    break;  
  }
 
 }while(b==0);

 }else{
    System.out.println("o sorteio deu 1 e o robo irá jogar primeiro"); 
     
  do{   
       preenchimentoRoboDificil(jogoVelha,-1);
  
  checarVelha(jogoVelha);
  testeVitoria(jogoVelha);
  if(checarVelha(jogoVelha)==1){
   System.out.println("o jogo deu velha , ninguem ganhou");
   break;
  } if(testeVitoria(jogoVelha)==-1){
    System.out.println("o ROBO ganhou , voce foi derrotado!!!!");  
    break;  
  }
  
   
  System.out.println("sua vez");
  exibirJogo(jogoVelha);
  preenchimento(jogoVelha,1);
  
  checarVelha(jogoVelha);
  testeVitoria(jogoVelha);
  if(checarVelha(jogoVelha)==1){
   System.out.println("o jogo deu velha , ninguem ganhou");
   break;
  } if(testeVitoria(jogoVelha)==1){
    System.out.println("o jogador  ganhou , parebens!!!!");  
    break;  
  }      
 }while(b==0);
}
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
}
public static int preenchimentoRoboFacil(int [][] jogoVelha, int i){
 SecureRandom random = new SecureRandom();  
  int a,b,coluna=1,linha=1;

 

 for(a=0;a<2000;a++){
     
  coluna =  random.nextInt(3);
  linha =   random.nextInt(3);  
  
  if(jogoVelha[linha][coluna]==0){
 
  jogoVelha[linha][coluna]= i;
    break;  
 }
              
}
 return 0;
}   
public static int preenchimentoRoboDificil(int [][]jogoVelha,int i){
    SecureRandom random = new SecureRandom(); 
    int a,b,coluna=1,linha=1;
 // primeiro condicoes em que o robo ganha na primeira linha
 
 if ((jogoVelha[0][1] + jogoVelha[0][0]+jogoVelha[0][2])==-2 && jogoVelha[0][2]==0){ 
   jogoVelha[0][2]=-1;  
   return -1;
   
  }else if((jogoVelha[0][0] + jogoVelha[0][2])==-2 && jogoVelha[0][1]==0){
    jogoVelha[0][1]=-1; 
     return -1;
    
  }else  if((jogoVelha[0][1] + jogoVelha[0][2])==-2 && jogoVelha[0][0]==0){
      jogoVelha[0][0]=-1;
       return -1;
  }
   
 // segunda linha 
 
  else if ((jogoVelha[1][1] + jogoVelha[1][0])==-2 && jogoVelha[1][2]==0){ 
   jogoVelha[1][2]=-1;  
    return -1;
  }else if((jogoVelha[1][0] + jogoVelha[1][2])==-2 && jogoVelha[1][1]==0){
    jogoVelha[1][1]=-1; 
     return -1;
  }else if((jogoVelha[1][1] + jogoVelha[1][2])==-2 && jogoVelha[1][0]==0){
      jogoVelha[1][0]=-1;
       return -1;
  }
  // terceira linha 

 else if((jogoVelha[2][1] + jogoVelha[2][0])==-2 && jogoVelha[2][2]==0){ 
   jogoVelha[2][2]=-1;  
    return -1;
   
  }else if((jogoVelha[2][0] + jogoVelha[2][2])==-2 && jogoVelha[2][1]==0){
    jogoVelha[2][1]=-1; 
     return -1;
    
  }else if((jogoVelha[2][1] + jogoVelha[2][2])==-2 && jogoVelha[2][0]==0){
      jogoVelha[2][0]=-1;
       return -1;
    }  
  
  
 // agora a primeira coluna
 
else if((jogoVelha[0][0]+ jogoVelha[1][0])==-2 && jogoVelha[2][0]==0){
    jogoVelha[2][0]=-1; 
     return -1;
    
 }else if((jogoVelha[1][0]+ jogoVelha[2][0])==-2 && jogoVelha[0][0]==0){
      jogoVelha[0][0]=-1; 
       return -1;
      
 } else if((jogoVelha[0][0]+ jogoVelha[2][0])==-2 && jogoVelha[1][0]==0){
     jogoVelha[1][0]=-1; 
      return -1;
 }  
 
 // segunda coluna 
 
else if((jogoVelha[0][1]+ jogoVelha[1][1])==-2 && jogoVelha[2][1]==0){
    jogoVelha[2][1]=-1; 
     return -1;
    
 }else if((jogoVelha[1][1]+ jogoVelha[2][1])==-2 && jogoVelha[0][1]==0){
      jogoVelha[0][1]=-1; 
       return -1;
 }else  if((jogoVelha[0][1]+ jogoVelha[2][1])==-2 && jogoVelha[1][1]==0){
     jogoVelha[1][1]=-1; 
      return -1;
 }  
   //terceira coluna
 else if((jogoVelha[0][2]+ jogoVelha[1][2])==-2 && jogoVelha[2][2]==0){
    jogoVelha[2][2]=-1;
     return -1;
    
 }else if((jogoVelha[1][2]+ jogoVelha[2][2])==-2 && jogoVelha[0][2]==0){
      jogoVelha[0][2]=-1; 
       return -1;
      
 }else if((jogoVelha[0][2]+ jogoVelha[2][2])==-2 && jogoVelha[1][2]==0){
     jogoVelha[1][2]=-1; 
      return -1;
 }  
  
 // agora diagonais 
 
 else if((jogoVelha[0][0]+ jogoVelha[1][1])==-2 && jogoVelha[2][2]==0){
    jogoVelha[2][2]=-1; 
     return -1;
  
 }else if((jogoVelha[1][1]+ jogoVelha[2][2])==-2 && jogoVelha[0][0]==0){
    jogoVelha[0][0]=-1;
     return -1;

} else if((jogoVelha[0][0]+ jogoVelha[2][2])==-2 && jogoVelha[1][1]==0){
    jogoVelha[1][1]=-1; 
 return -1;}
 
// agora as outras diagonais

else if((jogoVelha[0][2]+ jogoVelha[1][1])==-2 && jogoVelha[2][0]==0){
    jogoVelha[2][0]=-1; 
     return -1;

}else if((jogoVelha[2][0]+ jogoVelha[1][1])==-2 && jogoVelha[0][2]==0){
    jogoVelha[0][2]=-1; 
     return -1;
}else if((jogoVelha[0][2]+ jogoVelha[2][0])==-2 && jogoVelha[1][1]==0){
    jogoVelha[1][1]=-1;   
     return -1;
}
 
  // impedir do jogador vencer
else if((jogoVelha[0][1] + jogoVelha[0][0])==2 && jogoVelha[0][2]==0){ 
   jogoVelha[0][2]=-1;  
    return -1;
  }else if((jogoVelha[0][0] + jogoVelha[0][2])==2 && jogoVelha[0][1]==0){
    jogoVelha[0][1]=-1; return -1; 
    
  }else if((jogoVelha[0][1] + jogoVelha[0][2])==2 && jogoVelha[0][0]==0){
      jogoVelha[0][0]=-1; return -1;
  }
   
 // segunda linha 
 
else if((jogoVelha[1][1] + jogoVelha[1][0])==2  && jogoVelha[1][2]==0){ 
   jogoVelha[1][2]=-1;   return -1;
   
  }else if((jogoVelha[1][0] + jogoVelha[1][2])==2 && jogoVelha[1][1]==0){
    jogoVelha[1][1]=-1;  return -1;
    
  }else if((jogoVelha[1][1] + jogoVelha[1][2])==2 && jogoVelha[1][0]==0){
      jogoVelha[1][0]=-1; return -1;
  }
  // terceira linha 

  else if((jogoVelha[2][1] + jogoVelha[2][0])==2 && jogoVelha[2][2]==0){ 
   jogoVelha[2][2]=-1;   return -1;
   
  }else if((jogoVelha[2][0] + jogoVelha[2][2])==2 && jogoVelha[2][1]==0){
    jogoVelha[2][1]=-1;  return -1;
    
  }else if((jogoVelha[2][1] + jogoVelha[2][2])==2 && jogoVelha[2][0]==0){
      jogoVelha[2][0]=-1; return -1;
    }  
  
  
 // agora a primeira coluna
 
  else if((jogoVelha[0][0]+ jogoVelha[1][0])==2 && jogoVelha[2][0]==0){
    jogoVelha[2][0]=-1;  return -1;
    
 }else if((jogoVelha[1][0]+ jogoVelha[2][0])==2 && jogoVelha[0][0]==0){
      jogoVelha[0][0]=-1;  return -1;
      
 } else if((jogoVelha[0][0]+ jogoVelha[2][0])==2 && jogoVelha[1][0]==0){
     jogoVelha[1][0]=-1;  return -1;
 }  
 
 // segunda coluna 
 
 else if((jogoVelha[0][1]+ jogoVelha[1][1])==2 && jogoVelha[2][1]==0){
    jogoVelha[2][1]=-1;  return -1;
    
 }else if((jogoVelha[1][1]+ jogoVelha[2][1])==2 && jogoVelha[0][1]==0){
      jogoVelha[0][1]=-1;  return -1;
      
 } else if((jogoVelha[0][1]+ jogoVelha[2][1])==2 && jogoVelha[1][1]==0){
     jogoVelha[1][1]=-1;  return -1;
 }  
   //terceira coluna
 else if((jogoVelha[0][2]+ jogoVelha[1][2])==2 && jogoVelha[2][2]==0){
    jogoVelha[2][2]=-1;  return -1;
    
 }else if((jogoVelha[1][2]+ jogoVelha[2][2])==2 && jogoVelha[0][2]==0){
      jogoVelha[0][2]=-1;  return -1;
      
 } else if((jogoVelha[0][2]+ jogoVelha[2][2])==2 && jogoVelha[1][2]==0){
     jogoVelha[1][2]=-1;  return -1;
 }  
  
 // agora diagonais 
 
 else if((jogoVelha[0][0]+ jogoVelha[1][1])==2 && jogoVelha[2][2]==0){
    jogoVelha[2][2]=-1;  return -1;
   
  
 } else if((jogoVelha[1][1]+ jogoVelha[2][2])==2 && jogoVelha[0][0]==0){
    jogoVelha[0][0]=-1;   return -1;

}else if((jogoVelha[0][0]+ jogoVelha[2][2])==2 && jogoVelha[1][1]==0){
    jogoVelha[1][1]=-1;  return -1;
}
 
// agora as outras diagonais

else if((jogoVelha[0][2]+ jogoVelha[1][1])==2 && jogoVelha[2][0]==0){
    jogoVelha[2][0]=-1;  return -1;

}else if((jogoVelha[2][0]+ jogoVelha[1][1])==2 && jogoVelha[0][2]==0){
    jogoVelha[0][2]=-1;  return -1;
    
}else if((jogoVelha[0][2]+ jogoVelha[2][0])==2 && jogoVelha[1][1]==0){
    jogoVelha[1][1]=-1;    return -1;
}

else{
    for(a=0;a<2000;a++){
     
  coluna =  random.nextInt(3);
  linha =   random.nextInt(3);  
  
  if(jogoVelha[linha][coluna]==0){
 
  jogoVelha[linha][coluna]= i;
    break;  
 }
}

 
}
 return 0;
}
}
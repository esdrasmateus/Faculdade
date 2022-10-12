package br.com.esdrasmateus.aulasjava;

public class S08ContaPoupanca {
    public static void main(String[] args){
        float Poupanca = 5000;
        System.out.println(Poupanca);
        Poupanca += 1000;
        System.out.println(Poupanca);
        Poupanca += (Poupanca * 0.5) / 100;
        System.out.println(Poupanca);
    }
}

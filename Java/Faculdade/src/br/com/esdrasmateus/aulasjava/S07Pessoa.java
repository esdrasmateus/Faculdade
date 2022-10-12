package br.com.esdrasmateus.aulasjava;

public abstract class S07Pessoa {

    protected String xNome;
    protected void Pessoa() {
    xNome = "Sem nome";
    }
    protected S07Pessoa(String nome){
    xNome = nome;
    }
    public String getNome(){
    return xNome;
    }
}

public class Idade extends S07Pessoa{
    private static String xCPF;

    public Idade() {
        super(xCPF);
    }
    public Idade(String nome){
    super(nome);
    }
    public String getCPF(){
    return  xCPF;
    }
}

class Principal{
    public static void main(String[] args){
    Idade pessoa1 = new Idade("Daniel");
    System.out.println (pessoa1.getNome());
    System.out.println (pessoa1.getCPF());
    }
}
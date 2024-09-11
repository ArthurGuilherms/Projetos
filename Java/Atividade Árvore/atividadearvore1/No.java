package atividadearvore1;

import java.util.ArrayList;

public class No {
    private No pai;
    private String nome;
    private ArrayList<No> listaFilhos = new ArrayList<No>();
    
    No(String nome)
    {
        this.nome = nome;
    }
    
    public String getNome()
    {
        return nome;
    }
    
    public void setPai(No n)
    {
        pai = n;
    }
    
    public No getPai()
    {
        return pai;
    }
    
    public ArrayList<No> getListaFilhos()
    {
        return listaFilhos;
    }
    
    public void adicionarFilho(No n)
    {
        listaFilhos.add(n);
    }
    
    public void removerFilho(No n)
    {
        listaFilhos.remove(n);
    }
}
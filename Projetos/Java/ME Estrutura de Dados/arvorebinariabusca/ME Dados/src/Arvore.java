import java.util.ArrayList;

public class Arvore {

    private No raiz;

    Arvore(No raiz) 
    {
        this.raiz = raiz;
    }

    public No getRaiz() {
        return raiz;
    }

    public void AdicionarNo(No n) 
    {
        boolean achouPai = false;
        No tentativaPai = raiz;
        while (!achouPai) 
        {
            if (n.getValor() < tentativaPai.getValor()) 
            {
                if (tentativaPai.getNoE() == null) 
                {
                    tentativaPai.setNoE(n);
                    n.setPai(tentativaPai);
                    achouPai = true;
                } 
                else 
                {
                    tentativaPai = tentativaPai.getNoE();
                }
            } 
            else if (n.getValor() > tentativaPai.getValor()) 
            {
                if (tentativaPai.getNoD() == null) 
                {
                    tentativaPai.setNoD(n);
                    n.setPai(tentativaPai);
                    achouPai = true;
                } 
                else 
                {
                    tentativaPai = tentativaPai.getNoD();
                }
            } 
            else 
            {
                System.out.println("Valor inserido já existe!");
            }
        }
    }

    public void RemoverNo(int valor) 
    {
        No n = AcharNo(valor, raiz);
        if (n.getValor() < n.getPai().getValor()) 
        {
            n.getPai().setNoE(null);
            n.setPai(null);
        } 
        else if (n.getValor() > n.getPai().getValor()) 
        {
            n.getPai().setNoD(null);
            n.setPai(null);
        }
    }

    public No AcharNo(int valor, No tentativa) 
    {
        if (valor < tentativa.getValor()) 
        {
            if (tentativa.getNoE() == null) 
            {
                return null;
            } 
            else 
            {
                return AcharNo(valor, tentativa.getNoE());
            }
        } 
        else if (valor > tentativa.getValor()) 
        {
            if (tentativa.getNoD() == null) 
            {
                return null;
            } 
            else 
            {
                return AcharNo(valor, tentativa.getNoD());
            }
        } 
        else 
        {
            return tentativa;
        }
    }

    
}

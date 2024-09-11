package atividadearvore1;

public class Arvore {
    private No raiz;
    
    Arvore(No n)
    {
        raiz = n;
    }

    public void Inserir(String nomePai, No n)
    {
        No pai = Achar(nomePai);
        if (pai != null)
        {
            n.setPai(pai);
            pai.adicionarFilho(n);
        }
    }
    
    public void Remover(No n)
    {
        No pai = n.getPai();
        pai.removerFilho(n);
    }
    
    public No Achar(String s)
    {
        if (raiz.getNome() == s)
        {
            return raiz;
        }
        else
        {
            if (raiz.getListaFilhos().isEmpty())
            {
                return null;
            }
            else
            {
                for (int i = 0; i < raiz.getListaFilhos().size(); i++)
                {
                    No elemento = Achar(raiz.getListaFilhos().get(i), s);
                    if (elemento != null)
                    {
                        return elemento;
                    }
                }
                return null;
            }
        }
    }
    
    public No Achar(No n, String s)
    {
        if (n.getNome() == s)
        {
            return n;
        }
        else
        {
            if (n.getListaFilhos().isEmpty())
            {
                return null;
            }
            else
            {
                for (int i = 0; i < n.getListaFilhos().size(); i++)
                {
                    No elemento = Achar(n.getListaFilhos().get(i), s);
                    if (elemento != null)
                    {
                        return elemento;
                    }
                }
                return null;
            }
        }
    }
    
    public int CalcularNivel(No n)
    {
        int nivel = 0;
        No elemento = n;
        while (elemento.getPai() != null)
        {
            elemento = elemento.getPai();
            nivel++;
        }
        return nivel;
    }
    
    public int CalcularAltura(No n)
    {
        int altura = 0;
        int maiorValor = 0;
        if (!n.getListaFilhos().isEmpty())
        {
            for (int i = 0; i < n.getListaFilhos().size(); i++)
            {
                int valor = CalcularAltura(n.getListaFilhos().get(i), altura+1);
                if (valor > maiorValor)
                {
                    maiorValor = valor;
                }
            }
        }
        return maiorValor;
    }
    
    public int CalcularAltura(No n, int a)
    {
        int altura = a;
        int maiorValor = a;
        if (!n.getListaFilhos().isEmpty())
        {
            for (int i = 0; i < n.getListaFilhos().size(); i++)
            {
                int valor = CalcularAltura(n.getListaFilhos().get(i), altura+1);
                if (valor > maiorValor)
                {
                    maiorValor = valor;
                }
            }
        }
        return maiorValor;
    }

    public String VerificarNo(String s)
    {
        No noVerificado = Achar(s);
        if (noVerificado == null) 
        {
            return "Nó não encontrado";
        }
        if (noVerificado == raiz) 
        {
            return "Esse é um nó raiz";
        }
        if (noVerificado.getListaFilhos().isEmpty() && noVerificado != raiz)
        {
            return "Esse é um nó folha";
        }
        if (!noVerificado.getListaFilhos().isEmpty() && noVerificado != raiz)
        {
            return "Esse é um nó galho";
        }
        return "Nó não encontrado";
        
    }
}
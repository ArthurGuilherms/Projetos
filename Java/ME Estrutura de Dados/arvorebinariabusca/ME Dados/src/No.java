

public class No {
    private No pai, noD, noE;
    private int valor;

    No(int valor)
    {
    	this.valor = valor;
    }
    
    public int getValor()
    {
    	return valor;
    }
    
    public No getPai() {
    	return pai;
    }
    
    public void setPai(No pai) {
    	this.pai = pai;
    }
    
    public No getNoD() {
    	return noD;
    }
    
    public void setNoD(No noD) {
    	this.noD = noD;
    }
    
    public No getNoE() {
    	return noE;
    }
    
    public void setNoE(No noE) {
    	this.noE = noE;
    }
        
    public static int NivelProfundidadeNo(No n)
    {
        if (n.getPai() != null)
        {
            return NivelProfundidadeNo(n.getPai());
        }
        return 0;
    }
        
    public static int AlturaNo(No n)
    {
        int altura = 0;
        int alturaNova = 0;
        if (n.getNoD() != null)
        {
            alturaNova = 1 + AlturaNo(n.getNoD());
            if (altura < alturaNova)
            {
                altura = alturaNova;
            }
        }
        if (n.getNoE() != null)
        {
            alturaNova = 1 + AlturaNo(n.getNoE());
            if (altura < alturaNova)
            {
                altura = alturaNova;
            }
        }
        return altura;
    }
}
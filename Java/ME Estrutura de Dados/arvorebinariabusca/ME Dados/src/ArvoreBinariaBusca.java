public class ArvoreBinariaBusca 
{
    public static void main(String[] args) 
    {
	Arvore arvore = new Arvore(new No(10));
	arvore.AdicionarNo(new No(5));
	arvore.AdicionarNo(new No(3));
	arvore.AdicionarNo(new No(2));
    arvore.AdicionarNo(new No(11));
    arvore.AdicionarNo(new No(6));
        No n = arvore.AcharNo(5, arvore.getRaiz());
        System.out.println(n.AlturaNo(n));
        System.out.println(No.NivelProfundidadeNo(n));

        ImprimirArvore(arvore.getRaiz(), 0);
    }

    public static void ImprimirArvore(No raiz, int nivel) {
        if (raiz == null) {
            return;
        }
        ImprimirArvore(raiz.getNoD(), nivel + 1);
        if (nivel != 0) {
            for (int i = 0; i < nivel - 1; i++) {
                System.out.print("|\t");
            }
            System.out.println("|-------[" + raiz.getValor() + "]");
        } else {
            System.out.println("[" + raiz.getValor() + "]");
        }
        ImprimirArvore(raiz.getNoE(), nivel + 1);
    }
}
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        No raiz = new No(50); // Exemplo de valor para a raiz
        Arvore arvore = new Arvore(raiz);

        int opcao;
        do {
            System.out.println("Escolha uma opção:");
            System.out.println("1. Adicionar nó");
            System.out.println("2. Remover nó");
            System.out.println("3. Encontrar nó");
            System.out.println("4. Calcular nível de profundidade da árvore");
            System.out.println("5. Calcular altura da árvore");
            System.out.println("0. Sair");

            opcao = scanner.nextInt();
            switch (opcao) {
                case 1:
                    System.out.println("Digite o valor do nó a ser adicionado:");
                    int valorAdicionar = scanner.nextInt();
                    arvore.AdicionarNo(new No(valorAdicionar));
                    break;
                case 2:
                    System.out.println("Digite o valor do nó a ser removido:");
                    int valorRemover = scanner.nextInt();
                    arvore.RemoverNo(valorRemover);
                    break;
                case 3:
                    System.out.println("Digite o valor do nó a ser encontrado:");
                    int valorEncontrar = scanner.nextInt();
                    No noEncontrado = arvore.AcharNo(valorEncontrar, arvore.getRaiz());
                    if (noEncontrado != null) {
                        No n = arvore.AcharNo(valorEncontrar, arvore.getRaiz());
                        System.out.println("Nó encontrado: " + noEncontrado.getValor());
                        System.out.println("Altura: " + No.AlturaNo(n));
                        System.out.println("Profundidade: " +No.NivelProfundidadeNo(n));
                    } else {
                        System.out.println("Nó não encontrado.");
                    }
                    break;
                case 4:
                    int nivelProfundidade = No.AlturaNo(arvore.getRaiz());
                    System.out.println("Nível de profundidade da árvore: " + nivelProfundidade);
                    break;
                case 5:
                    int altura = No.AlturaNo(arvore.getRaiz());
                    System.out.println("Altura da árvore: " + altura);
                    break;
                case 0:
                    System.out.println("Saindo...");
                    break;
                default:
                    System.out.println("Opção inválida!");
                    break;
            }
        } while (opcao != 0);
        
        scanner.close();
    }
}
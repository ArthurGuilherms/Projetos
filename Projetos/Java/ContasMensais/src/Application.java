import java.util.Scanner;
import java.util.ArrayList;

public class Application {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        Informaçoes informaçao = new Informaçoes();

        //Introdução
        System.out.println("Bem vindo ao calculador de boletos!");

        //Contar para quantos moradores será dividida a conta
        System.out.println("A conta será dividida para quantas pessoas?");
        informaçao.setMoradores(scanner.nextInt());

        //Selecionar se será considerada a condição especial (Homens pagarem mais devido ao ar condicionado)
        System.out.println("Considerar diferença de valor da energia devido ao quarto com ar condicionado? [S/N]");
        String condicao = scanner.next();

        //Mostrar as opões de contas disponiveis
        System.out.println("Selecione as contas que deseja dividir: \n 1- Água \n 2- Energia\n 3- Condomínio\n 4- Aluguel\n 5- Internet \n 6- Desfazer lista\n 7- Calcular\n");

        //Pedir ao usuário quais contas deseja pagar e armazenar na lista contasSelecionadas
        ArrayList<String> contasSelecionadas = new ArrayList<String>();
        while (true) {
            int opcao = scanner.nextInt();
            if (opcao == 7) {
                System.out.println("");
                break;
            }
            
            switch (opcao) {
                case 1:
                    contasSelecionadas.add("Água");
                    break;
                case 2:
                    contasSelecionadas.add("Energia");
                    break;
                case 3:
                    contasSelecionadas.add("Condomínio");
                    break;
                case 4:
                    contasSelecionadas.add("Aluguel");
                    break;
                case 5:
                    contasSelecionadas.add("Internet");
                    break;
                case 6:
                    contasSelecionadas.clear();
                    break;

                default:
                    System.out.println("Opção inválida. Digite novamente.");
                    break;
            
            }
            System.out.println("Contas selecionadas:" + contasSelecionadas);
        }

        // Pedir o valor das contas ao usuário e armazenar em uma lista o relatório escrito dos valores já divididos
        ArrayList<String> relatorio = new ArrayList<String>();
        String relatorioEscrito;
        if (contasSelecionadas.contains("Água")) {
            System.out.println("Qual o valor da conta de água?");
            informaçao.setContadeÁgua(scanner.nextDouble());
            relatorioEscrito = ("Água: " + informaçao.getContadeÁgua() + " / " + informaçao.getMoradores() + " = " + (informaçao.getContadeÁgua() / informaçao.getMoradores()));
            relatorio.add(relatorioEscrito);
        }

        //Verificar a condição especial e, se necessário, aplicar as alterações necessárias
        if (contasSelecionadas.contains("Energia")) {
            if (condicao.equalsIgnoreCase("S")) {
                System.out.println("Qual o valor da conta de energia?");
                informaçao.setContadeLuz((scanner.nextDouble()));
                relatorioEscrito = ("Energia: " + informaçao.getContadeLuz());
                relatorio.add(relatorioEscrito);
            }
            
            if (condicao.equalsIgnoreCase("N")) {
                System.out.println("Qual o valor da conta de energia?");
                informaçao.setContadeLuz((scanner.nextDouble()));
                relatorioEscrito = ("Energia: " + informaçao.getContadeLuz() + " / " + informaçao.getMoradores() + " = " + (informaçao.getContadeLuz() / informaçao.getMoradores()));
                relatorio.add(relatorioEscrito);
            }
        }

        if (contasSelecionadas.contains("Condomínio")) {
            System.out.println("Qual o valor da conta do condomínio?");
            informaçao.setCondominio((scanner.nextDouble()));
            relatorioEscrito = ("Condomínio: " + informaçao.getCondominio() + " / " + informaçao.getMoradores() + " = " + (informaçao.getCondominio() / informaçao.getMoradores()));
            relatorio.add(relatorioEscrito);
        }

        if (contasSelecionadas.contains("Aluguel")) {
            System.out.println("Qual o valor da conta do aluguel?");
            informaçao.setAluguel((scanner.nextDouble()));
            relatorioEscrito = ("Aluguel: " + informaçao.getAluguel() + " / " + informaçao.getMoradores() + " = " + (informaçao.getAluguel() / informaçao.getMoradores()));
            relatorio.add(relatorioEscrito);

        }
        if (contasSelecionadas.contains("Internet")) {
            System.out.println("Qual o valor da conta de internet?");
            informaçao.setInternet((scanner.nextDouble()));
            relatorioEscrito = ("Internet: " + informaçao.getInternet() + " / " + informaçao.getMoradores() + " = " + (informaçao.getInternet() / informaçao.getMoradores()));
            relatorio.add(relatorioEscrito);
        }
        
        //Impressão do relatório com os valores
        String relatorioFinal = String.join("\n", relatorio);
        System.out.println("\n" + relatorioFinal);
        System.out.println("---------------------------------");

        //Impressão caso não haja condição especial
        double ValorTotal = informaçao.getAluguel() + informaçao.getCondominio() + informaçao.getContadeLuz() + informaçao.getContadeÁgua() + informaçao.getInternet();
        if (condicao.equalsIgnoreCase("N")) {
            System.out.println("Total: " + (ValorTotal) + " / " + informaçao.getMoradores() + " = " + (ValorTotal / informaçao.getMoradores()));
        }

        //Condicao especial
        if (condicao.equalsIgnoreCase("S")) {
            System.out.println("Total: " + (ValorTotal));

            //Calculo da divisão de energia
            double totalMenosEnergia = ValorTotal - informaçao.getContadeLuz();
            System.out.println("Total: " + (ValorTotal) + " / " + informaçao.getMoradores() + " = " + (ValorTotal / informaçao.getMoradores()));
            System.out.println("\nHomens: " + ((totalMenosEnergia/informaçao.getMoradores()) + (informaçao.getContadeLuz() - 100)/2));
            System.out.println("Mulheres: " + ((totalMenosEnergia/informaçao.getMoradores()) + 50));
        }
        

        //Calcular condição especial da energia (Homens pagam mais devido ao ar condicionado)
        scanner.close();
    }
}
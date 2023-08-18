import java.util.ArrayList;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        String valorPorGenero = " ";
        boolean programa = true, condicao = false;
        int escolha, pessoaDesconto = 0;
        ArrayList ListaContas = new ArrayList<>();
        Contas conta = new Contas();

            // código para arredondar valores em duas casas decimais:
            int casasDecimais = 2;
            double fatorDeMultiplicacao = Math.pow(10, casasDecimais);
            /*double valorMultiplicado = valor * fatorDeMultiplicacao;
            double valorArredondado = Math.round(valorMultiplicado) / fatorDeMultiplicacao;
            Então:
            valorArredondado = Math.round(valor * fatorDeMultiplicacao) / fatorDeMultiplicacao;
            */

            System.out.println("Bem vindo, à calculadora de boletos!\nA divisão será feita para quantas pessoas?");
            int pessoas = scanner.nextInt();
            System.out.println("Deseja adicionar a diferença na conta de luz? (S/N)");
            String resposta = scanner.next();
            if (resposta.equalsIgnoreCase("n")) {
                condicao = false;
            }
            if (resposta.equalsIgnoreCase("s")) {
                condicao = true;
                System.out.println("Quantas pessoas pagarão a maior parte?");
                pessoaDesconto = scanner.nextInt();
            }

            while (programa == true) {
                System.out.println("\nQual das seguintes contas você deseja pagar?\n 1- Aluguel\n 2- Energia\n 3- Água\n 4- Condomínio\n 5- Internet\n 6- IPTU\n 7- Desfazer Lista\n 8- Calcular\n\nContas:");
                System.out.println(ListaContas);

                escolha = scanner.nextInt();
                if (escolha == 1) {
                    ListaContas.add("Aluguel");
                }
                if (escolha == 2) {
                    ListaContas.add("Energia");
                }
                if (escolha == 3) {
                    ListaContas.add("Água");
                }
                if (escolha == 4) {
                    ListaContas.add("Condomínio");
                }
                if (escolha == 5) {
                    ListaContas.add("Internet");
                }
                if (escolha == 6) {
                    ListaContas.add("IPTU");
                }
                if (escolha == 7) {
                    ListaContas.clear();
                }
                if (escolha == 8) {
                  break;
                }
                
            }
            
            ArrayList<String> Relatorio = new ArrayList<String>();
            String RelatorioEscrito;
            if (ListaContas.contains("Aluguel")) {
                    System.out.println("Qual o valor do Aluguel?");
                    conta.setContaAluguel(scanner.nextDouble());
                    RelatorioEscrito = ("Aluguel: " + conta.getContaAluguel() + " / " + pessoas + " = " + Math.round((conta.getContaAluguel()/pessoas) * fatorDeMultiplicacao) / fatorDeMultiplicacao);
                    Relatorio.add(RelatorioEscrito);
                }

                if (ListaContas.contains("Energia") && condicao == false) {
                    System.out.println("Qual o valor da Energia?");
                    conta.setContaEnergia(scanner.nextDouble());
                    RelatorioEscrito = ("Energia: " + conta.getContaEnergia() + " / " + pessoas + " = " + Math.round((conta.getContaEnergia()/pessoas) * fatorDeMultiplicacao) / fatorDeMultiplicacao);
                    Relatorio.add(RelatorioEscrito);
                }

                if (ListaContas.contains("Energia") && condicao == true) {
                    System.out.println("Qual o valor da conta de Energia?");
                    conta.setContaEnergia(scanner.nextDouble());
                    RelatorioEscrito = ("Energia: " + conta.getContaEnergia() + " / " + pessoas + " = " + Math.round((conta.getContaEnergia()/pessoas) * fatorDeMultiplicacao) / fatorDeMultiplicacao);
                    Relatorio.add(RelatorioEscrito);

                    //Calculo da divisão Homens x Mulheres:
                    int valorDesconto = 70;
                    double valorDescontado = (conta.getContaEnergia() - valorDesconto) / pessoas;
                    double valorHomens = Math.round((valorDescontado + (valorDescontado / pessoaDesconto)) * fatorDeMultiplicacao) / fatorDeMultiplicacao;
                    double valorMulheres = Math.round((valorDescontado) * fatorDeMultiplicacao) / fatorDeMultiplicacao;
                    valorPorGenero = ("\nHomens: " + valorHomens + "\nMulheres: " + valorMulheres);
                }

                if (ListaContas.contains("Água")) {
                    System.out.println("Qual o valor da conta de Água?");
                    conta.setContaAgua(scanner.nextDouble());
                    RelatorioEscrito = ("Aluguel: " + conta.getContaAgua() + " / " + pessoas + " = " + Math.round((conta.getContaAgua()/pessoas) * fatorDeMultiplicacao) / fatorDeMultiplicacao);
                    Relatorio.add(RelatorioEscrito);
                }

                if (ListaContas.contains("Condomínio")) {
                    System.out.println("Qual o valor da conta do Condomínio?");
                    conta.setContaCondomínio(scanner.nextDouble());
                    RelatorioEscrito = ("Aluguel: " + conta.getContaCondomínio() + " / " + pessoas + " = " + Math.round((conta.getContaCondomínio()/pessoas) * fatorDeMultiplicacao) / fatorDeMultiplicacao);
                    Relatorio.add(RelatorioEscrito);
                }

                if (ListaContas.contains("Internet")) {
                    System.out.println("Qual o valor da conta de Internet?");
                    conta.setContaInternet(scanner.nextDouble());
                    RelatorioEscrito = ("Internet: " + conta.getContaInternet() + " / " + pessoas + " = " + Math.round((conta.getContaInternet()/pessoas) * fatorDeMultiplicacao) / fatorDeMultiplicacao);
                    Relatorio.add(RelatorioEscrito);

                }

                if (ListaContas.contains("IPTU")) {
                    System.out.println("Qual o valor do IPTU?");
                    conta.setContaIPTU(scanner.nextDouble());
                    RelatorioEscrito = ("IPTU: " + conta.getContaIPTU() + " / " + pessoas + " = " + Math.round((conta.getContaIPTU()/pessoas) * fatorDeMultiplicacao) / fatorDeMultiplicacao);
                    Relatorio.add(RelatorioEscrito);
                }
            
        //Impressão do relatório com os valores
        double valorTotal = conta.getContaAgua() + conta.getContaAluguel() + conta.getContaCondomínio() + conta.getContaEnergia() + conta.getContaInternet() + conta.getContaIPTU();
        valorTotal = Math.round((valorTotal) * fatorDeMultiplicacao) / fatorDeMultiplicacao;
        String relatorioFinal = String.join("\n", Relatorio);
        System.out.println("\n" + relatorioFinal);
        System.out.println("---------------------------------");
        System.out.println("Total: " + valorTotal + " / " + pessoas + " = " + (valorTotal/pessoas));
        
        if (condicao = true) {
            System.out.println(valorPorGenero);
        }
            
        scanner.close();
    }
}

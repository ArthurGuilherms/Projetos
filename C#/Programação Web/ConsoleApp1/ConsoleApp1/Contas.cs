/*Desenvolver uma classe Conta que simule uma conta bancária, com a
capacidade de realizar transferências entre contas.
Requisitos:
1.Criação da Classe Conta:

A classe Conta deve ter os seguintes cinco atributos:

numero: Um número inteiro que representa o número da conta.
titular: Uma string que representa o nome do titular da conta.
saldo: Um valor decimal que representa o saldo atual da conta.
agencia: Uma string que representa o número da agência onde a
conta está registrada.
tipo: Uma string que indica o tipo da conta (por exemplo,

"corrente"
,

"poupança"). 

Métodos da Classe Conta:

Construtor: Um método construtor para inicializar os cinco atributos.
Depositar: Um método que recebe um valor decimal e adiciona ao saldo da
conta.
Sacar: Um método que recebe um valor decimal e subtrai do saldo da conta,
desde que o saldo seja suficiente.
Transferir: Um método que permite transferir uma quantia de dinheiro de uma
conta para outra. O método deve receber o valor a ser transferido e a conta
destinatária. O método deve verificar se a conta de origem tem saldo
suficiente para realizar a transferência.
ConsultarSaldo: Um método que retorna o saldo atual da conta.
ConsultarDados: Um método que exibe todos os dados da conta (número,
titular, saldo, agência e tipo).*/

namespace ConsoleApp1 {
    public class Conta 
{
    private int numero {get; set;}
    private string titular {get; set;}
    private float saldo {get; set;}
    private int agencia {get; set;}
    private string tipo {get; set;}

    public Conta(int n, string tit, float s, int a, string tip) 
    {
        this.numero = n;
        this.titular = tit;
        this.saldo = s;
        this.agencia = a;
        this.tipo = tip;
    }

    public void transferir(float deposito, Conta contaRecebe)
    {
        if (deposito <= this.saldo) 
        {
            contaRecebe.saldo += deposito;
            this.saldo -= deposito;
        }
        else 
        {
            Console.WriteLine("Você não possui saldo sulficiente.");
        }
    }

    public void depositar(float deposito)
        {
            this.saldo += deposito;
        }

    public float Saldo
    {
        get { return saldo; }
    }


}

    public class ContaPoupanca : Conta
{
    public float TaxaDeJuros { get; set; }

    public ContaPoupanca(int n, string tit, float s, int a, string tip, float taxaDeJuros)
        : base(n, tit, s, a, "Poupança")
    {
        this.TaxaDeJuros = taxaDeJuros;
    }

    public void AplicarJuros()
    {
        float juros = this.Saldo * (this.TaxaDeJuros / 100);
        this.depositar(juros);
        Console.WriteLine($"Juros de {juros} aplicados. Novo saldo: {this.Saldo}");
    }

    }

}


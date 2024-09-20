using System;
using System.Net.Http.Headers;
using ClassApp1;
using ConsoleApp1;

/*Exercício 1:
1)Escreva um programa que insere um inteiro de cinco dígitos, separa o
inteiro em seus dígitos individuais e imprime os dígitos separados
entre si por três espaços cada. [Dica: Utilize operadores de divisão de
inteiros e módulo.] Por exemplo, se o usuário digitar 42339, o
programa deve imprimir: 4 2 3 3 9*/

static void Exercicio1() {
    //Inicialização de variáveis
    int inteiro;

    string impressao = "";

    // Loop para garantir que o usuário insira um número inteiro de 5 dígitos
    while (true) 
    {   
        // Verifica se o número tem exatamente 5 dígitos
        Console.WriteLine("Digite um número inteiro de 5 digitos");
        inteiro = int.Parse(Console.ReadLine());
        if (inteiro.ToString().Length == 5) 
        {
            break;
        }
        // Verifica se o número é positivo
        if (inteiro.ToString().Length <= 0) 
        {
            Console.WriteLine("O número deve ser positivo");
        } 
        else 
        {
            Console.WriteLine("O número digitado deve ter 5 digitos");
        }
    }

    // Inicialização de variáveis para separação dos dígitos
    int repeticao = 5;
    int divisor = 10000;

    // Loop para separar e imprimir os dígitos com três espaços entre eles
    while (repeticao != 0) 
    {
        // Adiciona o dígito atual à string de impressão
        impressao = impressao + (inteiro / (divisor)).ToString() + " ";

        // Remove o dígito atual do número
        inteiro %= divisor;

        // Atualiza o divisor para o próximo dígito
        divisor /= 10;

        // Decrementa o contador de repetições
        repeticao--;
    }

    //Imprime a string final com os digitos separados
    Console.WriteLine(impressao);
}
//Exercicio1();


/*Exercício 2:
 2) Escreva um programa que calcula os quadrados e cubos dos inteiros
de 0 a 10 e usa tabulações para imprimir as seguintes tabelas de
valores. */

static void Exercicio2() {
    int digito = 0;
    Console.WriteLine("Número\tQuadrado\tCubo");
    while (digito != 11)
    {
        Console.WriteLine($"{digito,6}\t{digito * digito,8}\t{digito * digito * digito,4}");
        digito += 1;
    }
}
//Exercicio2();


/*Exercício 3:
3) Escrever programa que receba a medida de dois ângulos internos de um
triângulo, calcule e mostre a medida do terceiro ângulo; sabendo que a
soma dos ângulos internos de um triângulo é 180. */

static void Exercicio3() {
    int medida1;
    int medida2;
    int medida3;

    while (true) {
        Console.WriteLine("Digite a primeira medida do angulo interno do triangulo");
    medida1 = int.Parse(Console.ReadLine());
    Console.WriteLine("Agora digite a segunda medida");
    medida2 = int.Parse(Console.ReadLine());

    if (medida1 <= 0 || medida2 <= 0) 
    {
        Console.WriteLine("Os angulos devem ser positivos, maiores que 0.");
    }
    else 
    {
        if ((medida1 + medida2) >= 180) 
    {
        Console.WriteLine("Essas medidas não podem pertencer ao mesmo triângulo pois excedem 180 graus.");
    }
    else 
    {
        medida3 = 180 - (medida1 + medida2); 
        Console.WriteLine($"O terceiro angulo interno mede {medida3} graus");
        break;
    }
    }
    }
    
    
    
   
}

//Exercicio3();

/*Exercício 4:
1) Calcule a exiba a soma dos números primos entre 200 a 300. Lembre
de escrever na tela cada um desses números.

Obs:
- 2 é o único primo PAR;
- Números primos são números que possuem 2 divisores. 1 e o próprio
número.
*/

static void Exercicio4() {
    int numero = 200;
    int divisor = 2;
    int primo = 0;
    int total = 0;

    Console.WriteLine($"Primo\tSoma dos Primos");
    while (numero < 300) 
    {   
        // se for divisivel por outro numero que não seja ele mesmo não é primo
        if ((numero % divisor == 0) && (numero != divisor)) 
        {   
            numero += 1;
            divisor = 2;
        } 

        //se o numero for divisivel apenas por ele mesmo, é primo
        if ((numero % divisor == 0) && (numero == divisor)) 
        {
            primo = numero;
            total += primo;
            numero += 1;
            divisor = 2;
            Console.WriteLine($"{primo}\t{total}");
        }

        if ((numero % divisor != 0) && (numero != divisor)) 
        {
            divisor += 1;
        }
    }
}

//Exercicio4();

/*Conta conta1 = new Conta(1234, "Arthur", 5500, 001, "Corrente");
Conta conta2 = new Conta(4567, "Gabriel", 0, 001, "Corrente");

conta1.transferir(3500, conta2);

Console.WriteLine(conta1.Saldo);
Console.WriteLine(conta2.Saldo);*/

Cachorro cachorro = new Cachorro("Rex", "Pit Bull Enraivado");
cachorro.Latir();
cachorro.Comer();


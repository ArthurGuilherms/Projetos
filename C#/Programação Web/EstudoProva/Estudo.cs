namespace estudo;

/*(Valor: 1,0) Para gerar um número inteiro aleatório em C# podemos usar a classe
Random, que oferece uma maneira moderna e mais flexível de gerar números
aleatórios. Como podemos ver na função a seguir:
int aleatorio(int min, int max)
{
Random random = new Random();
return random.Next(min, max);
}
Assim, faça um programa que simule o lançamento de um dado 30 vezes, verifique
e informe:
i) Qual número aparece mais vezes
ii) Foram observados mais pares ou ímpares nos lançamentos? Mostre com os totais
de pares e ímpares.
iii) Mostre uma tabela de frequência para cada elemento do espaço amostral */


class Estudo {
    static void Main()
    {
        List<int> numeros = new List<int>();
        int numero;
        Random random = new Random();

        for (int i = 0; i < 30; i++)
                {
                   numero = random.Next(1, 7);
                   numeros.Add(numero);
                }


        // Usando um Dictionary para contar as frequências
        var frequencia = new Dictionary<int, int>();

        foreach (var lancamento in numeros)
        {
            if (frequencia.ContainsKey(lancamento))
            {
                frequencia[lancamento]++;
            }
            else
            {
                frequencia[lancamento] = 1; // Inicializa a contagem
            }
        }

        int numeroMaisFrequente = -1;
        int maxFrequencia = 0;

        foreach (var item in frequencia)
        {
            if (item.Value > maxFrequencia)
            {
                maxFrequencia = item.Value;
                numeroMaisFrequente = item.Key;
            }
        }

        Console.WriteLine($"O numero mais repetido é: {numeroMaisFrequente}");
        // Mostrando a tabela de frequência
        Console.WriteLine("Tabela de frequência:");
        for (int i = 1; i <= 6; i++)
        {
            Console.WriteLine($"Número {i}: {frequencia.GetValueOrDefault(i, 0)}");
        }
    
    }
}
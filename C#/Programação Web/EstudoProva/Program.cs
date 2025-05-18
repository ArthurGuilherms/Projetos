/*class Program
{
    static void Main()
    {
        // Criação da classe Random
        Random random = new Random();
        
        // Lista para armazenar os resultados dos lançamentos
        List<int> lancamentos = new List<int>();

        // Lançando o dado 30 vezes
        for (int i = 0; i < 30; i++)
        {
            int resultado = random.Next(1, 7); // Lança um dado (1 a 6)
            lancamentos.Add(resultado);
        }

        // i) Qual número aparece mais vezes
        var frequencia = new Dictionary<int, int>();
        foreach (var lancamento in lancamentos)
        {
            if (frequencia.ContainsKey(lancamento))
                frequencia[lancamento]++;
            else
                frequencia[lancamento] = 1;
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

        Console.WriteLine($"Número que aparece mais vezes: {numeroMaisFrequente} ({maxFrequencia} vezes)");

        // ii) Verificando pares e ímpares
        int pares = 0, impares = 0;

        foreach (var lancamento in lancamentos)
        {
            if (lancamento % 2 == 0)
                pares++;
            else
                impares++;
        }

        Console.WriteLine($"Total de pares: {pares}");
        Console.WriteLine($"Total de ímpares: {impares}");

        // iii) Tabela de frequência
        Console.WriteLine("Tabela de frequência:");
        for (int i = 1; i <= 6; i++)
        {
            Console.WriteLine($"Número {i}: {frequencia.GetValueOrDefault(i, 0)}");
        }
    }
}
*/
using System.Dynamic;

namespace ClassApp1 {
    public class Animal
{
    public string Nome { get; set; }

    public Animal(string nome) {
        this.Nome = nome;
    }

    public void Comer()
    {
        Console.WriteLine($"{Nome} está comendo.");
    }
}   

    public class Cachorro : Animal {
        public Cachorro(string nome, string raca) : base(nome)
        {
            this.Raca = raca;
        }

        public String Raca {get; set;}

         public void Latir() 
    {
        Console.WriteLine($"{Nome} está latindo!");
    }
    }

}
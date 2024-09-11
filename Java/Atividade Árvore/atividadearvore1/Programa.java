package atividadearvore1;

public class Programa {
    public static void main(String[] args) {
        Arvore a = new Arvore(new No("a"));
        a.Inserir("a", new No("b"));
        a.Inserir("a", new No("c"));
        a.Inserir("b", new No("d"));
        a.Inserir("c", new No("e"));
        a.Inserir("c", new No("f"));
        a.Inserir("f", new No("g"));
        if (a.Achar("f") == null)
        {
            System.out.println("Ele nao achou");
        }
        else
        {
            System.out.println("Ele achou");
        }
        System.out.println(a.CalcularAltura(a.Achar("b")));
    }
}
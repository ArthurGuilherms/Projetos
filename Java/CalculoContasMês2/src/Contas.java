public class Contas {    
    private double contaAluguel;
    private double contaEnergia;
    private double contaAgua;
    private double contaCondomínio;
    private double contaInternet;
    private double contaIPTU;
    private double valorTotal;

    //get 

    public double getContaAluguel() {
        return contaAluguel;
    }
    public double getContaAgua() {
        return contaAgua;
    }
    public double getContaCondomínio() {
        return contaCondomínio;
    }
    public double getContaEnergia() {
        return contaEnergia;
    }
    public double getContaIPTU() {
        return contaIPTU;
    }
    public double getContaInternet() {
        return contaInternet;
    }
    public void setValorTotal(double valorTotal) {
        this.valorTotal = valorTotal;
    }

    //set
    public void setContaAluguel(double contaAluguel) {
        this.contaAluguel = contaAluguel;
    }
    public void setContaAgua(double contaAgua) {
        this.contaAgua = contaAgua;
    }
    public void setContaCondomínio(double contaCondomínio) {
        this.contaCondomínio = contaCondomínio;
    }
    public void setContaEnergia(double contaEnergia) {
        this.contaEnergia = contaEnergia;
    }
    public void setContaIPTU(double contaIPTU) {
        this.contaIPTU = contaIPTU;
    }
    public void setContaInternet(double contaInternet) {
        this.contaInternet = contaInternet;
    }
    public double getValorTotal() {
        return valorTotal;
    }
}

public class Informaçoes {
    private int moradores;
    private double contadeLuz;
    private double contadeÁgua;
    private double internet;
    private double aluguel;
    private double condominio;

    //get
    public int getMoradores() {
        return moradores;
    }
    public double getContadeLuz() {
        return contadeLuz;
    }
    public double getContadeÁgua() {
        return contadeÁgua;
    }
    public double getInternet() {
        return internet;
    }
    public double getAluguel() {
        return aluguel;
    }
    public double getCondominio() {
        return condominio;
    }

    //set
    public void setMoradores(int moradores) {
        this.moradores = moradores;
    }
    public void setContadeLuz(double contadeLuz) {
        this.contadeLuz = contadeLuz;
    }
    public void setContadeÁgua(double contadeÁgua) {
        this.contadeÁgua = contadeÁgua;
    }
    public void setInternet(double internet) {
        this.internet = internet;
    }
    public void setAluguel(double aluguel) {
        this.aluguel = aluguel;
    }
    public void setCondominio(double condominio) {
        this.condominio = condominio;
    }   
    
}

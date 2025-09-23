public class Mainv3 {
    public static void main(String[] args) {
        int dia = 1;
        int mes = 1;
        int ano = 2017;

        while (ano <= 2020) {
            mes = 1;
            while (mes <= 12) {
                dia = 1;
                while (dia <= 30) {
                    System.out.println(dia + '/' + mes + '/' + ano);
                    dia += 1;
                mes += 1;
            ano += 1;
                }
            }
        }
    }
} 
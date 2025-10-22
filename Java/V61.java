package Java;
import java.util.Random;
public class V61 {
    public static void main(String[] args) {
        Random gerador = new Random();

        int qtdNums = 0;
        while (qtdNums < 6) {
            System.out.println(gerador.nextInt(50));
            qtdNums++;
        }
        }
    }
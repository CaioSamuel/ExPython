import java.util.Scanner;
import java.util.Random;

public class V66 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        Random rand = new Random();

        int num = rand.nextInt(100) + 1;
        int tent_total = 3;
        int tent = 0;

        System.out.println("Tente adivinhar o numero entre 1 e 100. Voce tem 3 tentativas.");

        while (tent < tent_total) {
            System.out.println("Tentativa: " + (tent + 1));
            int palp = entrada.nextInt();

            tent++;

            if (palp == num) {
                System.out.println("Parabens! Voce acertou, o numero era: ");
            }
        }
        entrada.close();
    }
}   

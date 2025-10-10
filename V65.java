import java.util.Scanner;
import java.util.Random;

public class V65 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        Random rand = new Random();

        int palp;

        int num = rand.nextInt(100) + 1;

        System.out.println("Adivinhe o número: ");
        palp = entrada.nextInt();

        while (palp != num) {
            if (palp > num) {
                System.out.println("O número é menor");
            } else {
                System.out.println("O número é maior");
            }
            System.out.println("Adivinhe o número: ");
            palp = entrada.nextInt();
        }
        System.out.println("Parabéns, você acertou! O número era:" + num);
        entrada.close();
    }
}
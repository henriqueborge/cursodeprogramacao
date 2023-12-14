package padrao;
import java.util.Scanner;

public class numuser {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o primeiro número: ");
        int N1 = scanner.nextInt();

        System.out.print("Digite o segundo número: ");
        int N2 = scanner.nextInt();

        N1 += N1 % 2 == 0 ? 1 : 0;

        StringBuilder impares = new StringBuilder("Os ímpares são: ");

        while (N1 <= N2) {
            impares.append(N1).append(" ");
            N1 += 2;
        }

        System.out.println(impares.toString());
        scanner.close();
    }
}


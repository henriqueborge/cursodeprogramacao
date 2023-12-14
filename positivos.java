package padrao;
import java.util.Scanner;

public class positivos {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int soma = 0;

        while (true) {
            System.out.print("Digite um número positivo (ou um número negativo para sair): ");
            int numero = scanner.nextInt();

            if (numero < 0) {
            	System.out.println("digite um numero valido");
                break;
            } else {
                soma += numero;
            }
        }
        System.out.println("A soma dos números positivos é: " + soma);

        scanner.close();
    }
}


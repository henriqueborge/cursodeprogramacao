package padrao;
import java.util.Scanner;

public class atualização {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite a quantidade de valores: ");
        int n1 = scanner.nextInt();
        int[] numero = new int[n1];

        for (int i = 0; i < numero.length; i++) {
            System.out.print("Digite um valor: ");
            numero[i] = scanner.nextInt();
        }

        // Mostra o array antes da atualização
        System.out.print("Array antes da atualização: ");
        for (int i = 0; i < numero.length; i++) {
            System.out.print(numero[i]);
            if (i < numero.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println();

        // Solicita a posição a ser atualizada
        System.out.print("Digite a posição a ser atualizada (0 a " + (numero.length - 1) + "): ");
        int posicao = scanner.nextInt();

        // Verifica se a posição é válida
        if (posicao >= 0 && posicao < numero.length) {
            System.out.print("Digite o novo valor: ");
            int novoValor = scanner.nextInt();
            numero[posicao] = novoValor;

            // Mostra o array após a atualização
            System.out.print("Array após a atualização: ");
            for (int i = 0; i < numero.length; i++) {
                System.out.print(numero[i]);
                if (i < numero.length - 1) {
                    System.out.print(", ");
                }
            }
            System.out.println();
        } else {
            System.out.println("Posição inválida. A posição deve estar entre 0 e " + (numero.length - 1));
        }

        // Fecha o scanner para evitar vazamento de recursos
        scanner.close();
    }
}

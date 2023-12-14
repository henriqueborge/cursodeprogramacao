package padrao;
import java.util.Scanner;

public class teste {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite um valor: ");
        int n1 = scanner.nextInt();

        int[] par = new int[n1];
        int[] impar = new int[n1];
        int countPar = 0;
        int countImpar = 0;
        int sum = 0;
        int soma = 0;

        for (int i = 0; i < n1; i++) {
            System.out.print("Digite um valor para a posição " + i + ": ");
            int valor = scanner.nextInt();

            if (valor % 2 == 0) {
                par[countPar++] = valor;
            } else {
                impar[countImpar++] = valor;
            }
        }

        System.out.print("Números pares inseridos pelo usuário: [");
        for (int i = 0; i < countPar; i++) {
            if (i > 0) {
                System.out.print(", ");
            }
            System.out.print(par[i]);
        }
        System.out.println("]");

        System.out.print("Números ímpares inseridos pelo usuário: [");
        for (int i = 0; i < countImpar; i++) {
            if (i > 0) {
                System.out.print(", ");
            }
            System.out.print(impar[i]);
        }
        System.out.println("]");
        
        for (int i = 0; i < par.length; i++) {
			sum += par[i];
		}
        System.out.println("Soma dos números pares inseridos pelo usuário: " + sum);
        
        for (int i = 0; i < impar.length; i++) {
			soma += impar[i];
		}
        System.out.println("Soma dos números impares inseridos pelo usuário: " + soma);

        scanner.close();
    }
}
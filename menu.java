package padrao;
import java.util.Scanner;

public class menu {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("MENU\n");
            System.out.println("1. Cadastrar produto");
            System.out.println("2. Imprimir produto");
            System.out.println("3. Atualizar produto");
            System.out.println("4. Deletar produto");
            System.out.println("5. Sair");

            System.out.print("Escolha uma opção: ");
            int opcao = scanner.nextInt();

            if (opcao == 1) {
                
            } else if (opcao == 2) {
                
            } else if (opcao == 3) {
                
            } else if (opcao == 4) {
                
            } else {
                break;
            }
        }

        scanner.close();
    }
}


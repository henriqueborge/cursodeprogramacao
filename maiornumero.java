package padrao;
import javax.swing.JOptionPane;
public class maiornumero {

	public static void main(String[] args) {
		int N1 = Integer.parseInt(JOptionPane.showInputDialog("Digite o primeiro numero"));
		int N2 = Integer.parseInt(JOptionPane.showInputDialog("Digite o segundo numero"));
		int N3 = Integer.parseInt(JOptionPane.showInputDialog("Digite o terceiro numero"));
		int N4 = Integer.parseInt(JOptionPane.showInputDialog("Digite o quarto numero"));
		int N5 = Integer.parseInt(JOptionPane.showInputDialog("Digite o quinto numero"));
		int max = N1;

        int[] numeros = {N2, N3, N4, N5};
        
		for (int numero : numeros) {
			if (numero > max ) {
				max = numero;
			}
		}
		JOptionPane.showMessageDialog(null, "O maior número é: " + max);

	}

}

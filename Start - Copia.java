package padrao;
import javax.swing.JOptionPane;
public class Start {

	public static void main(String[] args) {
		int numero = Integer.parseInt(JOptionPane.showInputDialog("Dgite um numero inteiro"));
		int numero2 = Integer.parseInt(JOptionPane.showInputDialog("Dgite um numero inteiro"));
		int numero3 = Integer.parseInt(JOptionPane.showInputDialog("Dgite um numero inteiro"));
		int numero4 = ((numero+numero2+numero3)/3);
		if (numero4 >= 7) {
			JOptionPane.showMessageDialog(null, numero4 + "Aprovado");
		}
		else {
			JOptionPane.showMessageDialog(null, numero4 + "Reprovado");
		}

	}

}

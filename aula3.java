package padrao;
import javax.swing.JOptionPane;
public class aula3 {

	public static void main(String[] args) {
		int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite um numero"));
		if (numero % 3 == 0 && numero % 5 == 0) {
			JOptionPane.showMessageDialog(null, "Este numero:" + numero + "pode ser dividido por 3 e 5");
		}
		else {
			JOptionPane.showMessageDialog(null, "Este numero:" + numero + "não pode pode ser dividido por 3 e 5" );
		}

	}

}

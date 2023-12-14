package padrao;
import javax.swing.JOptionPane;
public class somartodos {

	public static void main(String[] args) {
		int numero = Integer.parseInt(JOptionPane.showInputDialog("digite um numero"));
		int numero2 = Integer.parseInt(JOptionPane.showInputDialog("digite outro"));
		int soma = 0;
		for (int i = numero; i <= numero2; i += 1) {
			soma+=i;
		}
		JOptionPane.showMessageDialog(null, "total" + soma );
	}

}

package padrao;
import javax.swing.JOptionPane;
public class par {

	public static void main(String[] args) {
		int N1 = Integer.parseInt(JOptionPane.showInputDialog("digite o primeiro numero"));
		int N2 = Integer.parseInt(JOptionPane.showInputDialog("digite osegundo numero"));
		int soma = 0;
		for (int i = N1; i <= N2; i += 1) {
			soma+=i;
		}
		JOptionPane.showMessageDialog(null, "total: " + soma);
	}

}

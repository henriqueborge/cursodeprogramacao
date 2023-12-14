package padrao;
import javax.swing.JOptionPane;
public class idade2 {

	public static void main(String[] args) {
		int numero = Integer.parseInt(JOptionPane.showInputDialog("digite sua idade"));
		if (numero >= 18) {
			JOptionPane.showMessageDialog(null, "Parabens, você ja pode ser preso");
		}
		else {
			JOptionPane.showMessageDialog(null, "Você é ainda é de menor");
		}

	}

}

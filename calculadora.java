package padrao;
import javax.swing.JOptionPane;
public class calculadora {

	public static void main(String[] args) {
		float numero = Integer.parseInt(JOptionPane.showInputDialog("digite o primeiro numero"));
		String numero2 = JOptionPane.showInputDialog("escolha um sinal");
		float numero3 = Integer.parseInt(JOptionPane.showInputDialog("digite o segundo numero"));
		if (numero2.equals("+")) {
			JOptionPane.showMessageDialog(null, numero + numero3);
		}
		else if (numero2.equals("-")) {
			JOptionPane.showMessageDialog(null, numero - numero3);
		}
		else if (numero2.equals("*")) {
			JOptionPane.showMessageDialog(null, numero * numero3);
		}
		else if (numero2.equals("/")) {
			JOptionPane.showMessageDialog(null, numero / numero3);
		}
		else if (numero==0 || numero3==0 && numero2.equals("/")) {
			JOptionPane.showMessageDialog(null, "Numero não é valido");
		}
		else {
			JOptionPane.showMessageDialog(null, "Erro");
		}
		
	}
	

}

package padrao;
import javax.swing.JOptionPane;
public class vetor {

	public static void main(String[] args) {
		int[] numeros = new int[2];
		 numeros[0] = Integer.parseInt(JOptionPane.showInputDialog("digite um numero"));
		 numeros[1] = Integer.parseInt(JOptionPane.showInputDialog("digite outro"));
		
		JOptionPane.showMessageDialog(null, "primeiro numero: " + numeros[0]);
		JOptionPane.showMessageDialog(null, "segundo numero: " + numeros[1]);

	}

}

package padrao;
import javax.swing.JOptionPane;
public class vetorfor {

	public static void main(String[] args) {
		int n1 = Integer.parseInt(JOptionPane.showInputDialog("digite um valor"));
		int[] numero = new int[n1];
		int sum = 0;
		for (int i = 0; i < numero.length; i++) {
			numero[i] = Integer.parseInt(JOptionPane.showInputDialog("digite um valor"));
			sum += numero[i];
		}
		JOptionPane.showMessageDialog(null, "A soma dos números é: " + sum);
	}

}

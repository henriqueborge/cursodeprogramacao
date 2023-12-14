package padrao;

import javax.swing.JOptionPane;

public class idade {

	public static void main(String[] args) {
		int idade = Integer.parseInt(JOptionPane.showInputDialog("Digite sua idade"));
		if (idade <= 12) {
			JOptionPane.showMessageDialog(null, idade + "Criança");
		}
		else if (idade > 12 && idade <= 18) {
			JOptionPane.showMessageDialog(null, idade + "A");
		}
		else if (idade > 18 && idade <= 62) {
			JOptionPane.showMessageDialog(null, idade + "Adulto");
		}
		else{
			JOptionPane.showMessageDialog(null, idade + "Idoso");
		}

	}

}

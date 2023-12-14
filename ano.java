package padrao;
import javax.swing.JOptionPane;
public class ano {

	public static void main(String[] args) {
		int ano = Integer.parseInt(JOptionPane.showInputDialog("digite um ano: "));
		if ((ano % 4 == 0 && ano % 100 != 0) || (ano % 400 == 0)){
			 JOptionPane.showMessageDialog(null, ano + " É um ano bissexto.");
		}
		else {
			JOptionPane.showMessageDialog(null, ano + " Não é um ano bissexto.");
		}

	}

}

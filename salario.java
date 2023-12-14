package padrao;
import javax.swing.JOptionPane;
public class salario {

	public static void main(String[] args) {
		double salario = Integer.parseInt(JOptionPane.showInputDialog("Digite seu salario: "));
		if (salario >= 0 && salario < 280) {
			double total = salario * 0.20;
			JOptionPane.showMessageDialog(null, "Salario inicial: " + salario + " Salario com ajuste: "+ (salario + total) );
		}
		else if (salario >= 280 && salario < 700) {
			double total = salario * 0.15;
			JOptionPane.showMessageDialog(null, "Salario inicial: " + salario + " Salario com ajuste: "+ (salario + total) );
		}
		else if (salario >= 700 && salario < 1500) {
			double total = salario * 0.10;
			JOptionPane.showMessageDialog(null, "Salario inicial: " + salario + " Salario com ajuste: "+ (salario + total) );
		}
		else {
			double total = salario * 0.05;
			JOptionPane.showMessageDialog(null, "Salario inicial: " + salario + " Salario com ajuste: "+ (salario + total) );
		}

	}

}

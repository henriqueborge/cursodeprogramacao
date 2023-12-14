package padrao;
import javax.swing.JOptionPane;
public class tintas {

	public static void main(String[] args) {
		int metros = Integer.parseInt(JOptionPane.showInputDialog("digite a area em metros"));
		int litros = metros/3;
		int valor = 80;
		int capacidade = 18;
		int latas = litros/capacidade;
		int total = latas*valor;
		JOptionPane.showMessageDialog(null, "Voce precisara de " + latas + " latas e custara " + total + " reais");

	}

}

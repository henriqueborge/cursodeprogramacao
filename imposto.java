package padrao;
import javax.swing.JOptionPane;
public class imposto {

	public static void main(String[] args) {
		float N1 = Integer.parseInt(JOptionPane.showInputDialog("digite seu salario"));
		float N2 = Integer.parseInt(JOptionPane.showInputDialog("digite quantas horas voce trabalha por dia"));
		double ir = 0.11;
		double inss = 0.08;
		double sindicato = 0.05;
		float valor = N1*N2;
		double imp1 = valor*ir;
		double imp2 = valor*inss;
		double imp3 = valor*sindicato;
		double liquido = (valor-imp1-imp2-imp3);
		JOptionPane.showMessageDialog(null, "valor: " + valor + " imposto 1: " + imp1 + " imposto 2: " + imp2 + " imposto 3: " + imp3 + " valor liquido: " + liquido);

	}

}

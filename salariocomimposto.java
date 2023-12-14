package padrao;
import javax.swing.JOptionPane;
public class salariocomimposto {

	public static void main(String[] args) {
		double valor = Integer.parseInt(JOptionPane.showInputDialog("digite quanto voce ganha por hora: "));
		double horas = Integer.parseInt(JOptionPane.showInputDialog("Digite quantas horas voce trabalha por mes: "));
		double sindicato = 0.03;
		double fgts = 0.11;
		double salario = valor*horas;
		double sind = salario*sindicato;
		double fgt = salario*fgts;
		double bruto = (salario-sind-fgt);
		if (bruto < 900) {
			JOptionPane.showMessageDialog(null, bruto + "Esta isento de desconto");
		}
		else if (bruto > 900 && bruto <= 1500) {
			double ir = bruto*0.05;
			double desconto = (bruto-ir);
			JOptionPane.showMessageDialog(null, "Valor total: " + bruto + " valor com desconto: " + desconto);
		}
		else if (bruto > 1500 && bruto < 2500) {
			double ir = bruto*0.10;
			double desconto = (bruto-ir);
			JOptionPane.showMessageDialog(null, "Valor total: " + bruto + " valor com desconto: " + desconto);
		}
		else {
			double ir = bruto*0.20;
			double desconto = (bruto-ir);
			JOptionPane.showMessageDialog(null, "Valor total: " + bruto + " valor com desconto: " + desconto);
		}

	}

}

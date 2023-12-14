package padrao;
import javax.swing.JOptionPane;
public class assassino {

	public static void main(String[] args) {
		 int[] insp = new int[5];

	        insp[0] = JOptionPane.showInputDialog("Telefonou para a vítima?").equalsIgnoreCase("sim") ? 1 : 0;
	        insp[1] = JOptionPane.showInputDialog("Esteve no local do crime?").equalsIgnoreCase("sim") ? 1 : 0;
	        insp[2] = JOptionPane.showInputDialog("Mora perto da vítima?").equalsIgnoreCase("sim") ? 1 : 0;
	        insp[3] = JOptionPane.showInputDialog("Devia para a vítima?").equalsIgnoreCase("sim") ? 1 : 0;
	        insp[4] = JOptionPane.showInputDialog("Já trabalhou com a vítima?").equalsIgnoreCase("sim") ? 1 : 0;

	        int suspeitaCount = 0;

	        for (int answer : insp) {
	            suspeitaCount += answer;
	        }

	        if (suspeitaCount == 2) {
	            JOptionPane.showMessageDialog(null, "Suspeita");
	        } else if (suspeitaCount >= 3 && suspeitaCount <= 4) {
	            JOptionPane.showMessageDialog(null, "Cúmplice");
	        } else if (suspeitaCount == 5) {
	            JOptionPane.showMessageDialog(null, "Assassino");
	        } else {
	            JOptionPane.showMessageDialog(null, "Inocente");
	        }
	    }
	}



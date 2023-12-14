package padrao;
import javax.swing.JOptionPane;

public class tintas2 {
    public static void main(String[] args) {
        double areaA_Pintar = Double.parseDouble(JOptionPane.showInputDialog("Informe a área a ser pintada em metros quadrados:"));

        // Calcular apenas latas de 18 litros
        int latas = (int) Math.ceil(areaA_Pintar / 6 / 18 * 1.1);
        double precoLatas = latas * 80.0;
        double desperdicioLatas = Math.max(0, latas * 18.0 * 1000 - areaA_Pintar * 1000);

        // Calcular apenas galões de 3,6 litros
        int galoes = (int) Math.ceil(areaA_Pintar / 6 / 3.6 * 1.1);
        double precoGaloes = galoes * 25.0;
        double desperdicioGaloes = Math.max(0, galoes * 3.6 * 1000 - areaA_Pintar * 1000);

        // Calcular mistura de latas e galões
        int latasMistura = (int) Math.ceil(areaA_Pintar / 6 / 18 * 1.1);
        int galoesMistura = (int) Math.ceil((areaA_Pintar - latasMistura * 18) / 6 / 3.6 * 1.1);
        double precoMistura = latasMistura * 80.0 + galoesMistura * 25.0;
        double desperdicioMistura = Math.max(0, (latasMistura * 18.0 + galoesMistura * 3.6) * 1000 - areaA_Pintar * 1000);

        // Exibir resultados usando JOptionPane
        JOptionPane.showMessageDialog(null,
                "Comprar apenas latas de 18 litros\nQuantidade necessária: " + latas +
                        "\nPreço total: R$" + precoLatas + "\nDesperdício: " + desperdicioLatas + " ml");

        JOptionPane.showMessageDialog(null,
                "Comprar apenas galões de 3,6 litros\nQuantidade necessária: " + galoes +
                        "\nPreço total: R$" + precoGaloes + "\nDesperdício: " + desperdicioGaloes + " ml");

        JOptionPane.showMessageDialog(null,
                "Misturar latas e galões\nQuantidade de latas necessárias: " + latasMistura +
                        "\nQuantidade de galões necessários: " + galoesMistura + "\nPreço total: R$" + precoMistura +
                        "\nDesperdício: " + desperdicioMistura + " ml");
    }
}





import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Extra lyxig miniräknare");

        while (true) {
            System.out.print("Skriv in tal 1: ");
            String num1 = scanner.nextLine();
            System.out.print("Skriv in tal 2: ");
            String num2 = scanner.nextLine();

            System.out.println("Tryck [A]ddition, [D]ivision, [M]ultiplikation, [E]xit");
            String menu = scanner.nextLine();

            if (menu.equals("A")) {
                System.out.println(num1 + num2);
            } else if (menu.equals("D")) {
                System.out.println(num1 +"/"+ num2);
            } else {
                System.out.println(Integer.parseInt(num1) * Integer.parseInt(num2));
            }
        }
    }
}

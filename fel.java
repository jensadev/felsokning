import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static int inputInt(String text) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println(text);
            int choice = scanner.nextInt();
            return choice;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean menu = true;
        while (menu) {
            int choice = inputInt("1. Add to inventory \n2. List inventory \n3. Remove from inventory \n4. Exit");
            ArrayList<String> inventory = new ArrayList<>();
            scanner.nextLine(); // consume newline left-over

            switch (choice) {
                case 1:
                    System.out.println("Add item to inventory");
                    String item = scanner.nextLine();
                    inventory.add(item);
                    break;
                case 2:
                    System.out.println("List inventory");
                    for (String i : inventory) {
                        System.out.println(i);
                    }
                    break;
                case 3:
                    System.out.println("Remove item from inventory");
                    for (int i = 0; i < inventory.size(); i++) {
                        System.out.println((i) + ". " + inventory.get(i));
                    }
                    int index = scanner.nextInt();
                    if (index > 0) {
                        inventory.remove(index - 1);
                    }
                    break;
                case 4:
                    System.out.println("Exit");
                default:
                    System.out.println("Invalid input");
                    break;
            }
        }
        scanner.close();
    }
}

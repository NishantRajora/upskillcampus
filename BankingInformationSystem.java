import java.util.*;

class User {
    String username;
    String password;
    double balance;

    User(String username, String password) {
        this.username = username;
        this.password = password;
        this.balance = 0.0;
    }
}

public class BankingInformationSystem {
    static Scanner scanner = new Scanner(System.in);
    static HashMap<String, User> users = new HashMap<>();

    public static void main(String[] args) {
        System.out.println("Welcome to the Banking Information System");

        while (true) {
            System.out.println("\n1. Register");
            System.out.println("2. Login");
            System.out.println("3. Exit");
            System.out.print("Choose an option: ");
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    register();
                    break;
                case 2:
                    login();
                    break;
                case 3:
                    System.out.println("Thank you for using the system!");
                    return;
                default:
                    System.out.println("Invalid option. Try again.");
            }
        }
    }

    static void register() {
        System.out.print("Enter a username: ");
        String username = scanner.nextLine();
        if (users.containsKey(username)) {
            System.out.println("Username already exists.");
            return;
        }

        System.out.print("Enter a password: ");
        String password = scanner.nextLine();
        users.put(username, new User(username, password));
        System.out.println("User registered successfully.");
    }

    static void login() {
        System.out.print("Enter username: ");
        String username = scanner.nextLine();
        System.out.print("Enter password: ");
        String password = scanner.nextLine();

        User user = users.get(username);

        if (user != null && user.password.equals(password)) {
            System.out.println("Login successful.");
            userMenu(user);
        } else {
            System.out.println("Invalid credentials.");
        }
    }

    static void userMenu(User user) {
        while (true) {
            System.out.println("\n--- Account Menu ---");
            System.out.println("1. View Balance");
            System.out.println("2. Deposit Money");
            System.out.println("3. Withdraw Money");
            System.out.println("4. Logout");
            System.out.print("Choose an option: ");
            int option = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (option) {
                case 1:
                    System.out.println("Current Balance: ₹" + user.balance);
                    break;
                case 2:
                    System.out.print("Enter amount to deposit: ₹");
                    double deposit = scanner.nextDouble();
                    user.balance += deposit;
                    System.out.println("Deposited ₹" + deposit + ". New balance: ₹" + user.balance);
                    break;
                case 3:
                    System.out.print("Enter amount to withdraw: ₹");
                    double withdraw = scanner.nextDouble();
                    if (withdraw > user.balance) {
                        System.out.println("Insufficient balance.");
                    } else {
                        user.balance -= withdraw;
                        System.out.println("Withdrew ₹" + withdraw + ". Remaining balance: ₹" + user.balance);
                    }
                    break;
                case 4:
                    System.out.println("Logged out successfully.");
                    return;
                default:
                    System.out.println("Invalid option.");
            }
        }
    }
}

import java.util.HashMap;
import java.util.Map;
import java.util.Random;

public class AccountNumberGenerator {
    // Map to store the next available account number counter for each prefix
    private static Map<String, Integer> accountNumberCounters = new HashMap<>();

    // Method to generate spending account numbers (starting with "SP")
    public static String generateSpendingAccountNumber() {
        return generateAccountNumber("SP");
    }

    // Method to generate saving account numbers (starting with "SA")
    public static String generateSavingAccountNumber() {
        return generateAccountNumber("SA");
    }

    // Method to generate account numbers with a specified prefix
    private static String generateAccountNumber(String prefix) {
        int nextAccountNumber = accountNumberCounters.getOrDefault(prefix, 0) + 1;
        accountNumberCounters.put(prefix, nextAccountNumber);
        // Generate a random 6-digit number
        Random random = new Random();
        int randomNumber = 100000 + random.nextInt(900000); // Generates a number between 100000 and 999999
        // Combine the prefix, the counter, and the random number
        return prefix + nextAccountNumber + String.format("%06d", randomNumber); // Ensures random number is 6 digits long
    }

    public static void main(String[] args) {
        // Example usage
        String spendingAccountNumber1 = generateSpendingAccountNumber();
        String savingAccountNumber1 = generateSavingAccountNumber();
        String spendingAccountNumber2 = generateSpendingAccountNumber();
        String savingAccountNumber2 = generateSavingAccountNumber();

        System.out.println("Spending Account Number 1: " + spendingAccountNumber1);
        System.out.println("Saving Account Number 1: " + savingAccountNumber1);
        System.out.println("Spending Account Number 2: " + spendingAccountNumber2);
        System.out.println("Saving Account Number 2: " + savingAccountNumber2);
    }
}
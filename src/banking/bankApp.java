package banking;

public class bankApp {

    int balance;
    int previousTransaction;
    String customerName;
    String customerID;

    void deposit(int amount){
        if(amount != 0)
        {
            balance = balance + amount;
            previousTransaction = amount;
        
        }
    }

    
}

package banking;

import java.util.Scanner;

public class bankApp {

    int balance;
    int previousTransaction;
    String customerName;
    String customerID;


    bankApp(String cname , String cid)
    {
        customerName = cname;
        customerID = cid;
    }

    void deposit(int amount){
        if(amount != 0)
        {
            balance = balance + amount;
            previousTransaction = amount;
        
        }
    }

    void withdraw(int amount){

        if (amount != 0 )
        {
            balance = balance - amount;
            previousTransaction = -amount;
        }
    }

    void getPreviousTransaction()
    {
        if(previousTransaction > 0)
        {
            System.out.println(" Deposited : " +previousTransaction);
        }
        else if(previousTransaction < 0)
        {
            System.out.println("withdrawn: " +Math.abs(previousTransaction));
        }
        else
        {
            System.out.println("No transaction occured");
        }

    }

    void showMenu()
    {
        char option = '\0';
        Scanner scanner = new Scanner(System.in);

        System.out.println("Wellcome " +customerName);
        System.out.println("Your ID is " +customerID + "\n");
        System.out.println("A. Check Balance");
        System.out.println("B. Deposit");
        System.out.println("C. Withdraw");
        System.out.println("D. PreviousTransaction");
        System.out.println("E. Exit ");

        do {
            System.out.println("======================================================================");
            System.out.println("Enter an Option \n");
            System.out.println("======================================================================");
            option =scanner.next().charAt(0);

        }

        

    }



    
}

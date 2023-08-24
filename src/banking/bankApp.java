package banking;

import java.util.Scanner;

public class bankApp {

    int balance;
    int previousTransaction;
    String customerName;
    String customerID;


    public bankApp(String cname , String cid)
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

    public void showMenu()
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
            System.out.println("====================================================================== \n");
            option =scanner.next().charAt(0);

            switch(option)
            {
                case 'A':
                    System.out.println("_____________________________");
                    System.out.println("Balance " +balance);
                    System.out.println("_____________________________ \n");  
                    break;
                case 'B':                    
                    System.out.println("_____________________________");
                    System.out.println("Enter amount to deposit ");
                    System.out.println("_____________________________ \n");
                    int depositAmount = scanner.nextInt();
                    deposit(depositAmount);
                    System.out.println("\n");
                    break;
                case 'C':                    
                    System.out.println("_____________________________");
                    System.out.println("Enter amount to Withdraw ");
                    System.out.println("_____________________________ \n");
                    int withdawAmount = scanner.nextInt();
                    withdraw(withdawAmount);
                    System.out.println("\n");
                    break;
                case 'D':                    
                    System.out.println("_____________________________");
                    getPreviousTransaction();
                    System.out.println("_____________________________ \n");
                    break;

                case 'E':
                    System.out.println("*****************************************");
                    break;

                default:
                    System.out.println("Invalid option please try Again");
                    break;
            }
        }
        while(option != 'E');
        System.out.println("Thankyou for services");

        

    }



    
}

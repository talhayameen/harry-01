import java.util.Scanner;

public class simpleAddition {

     public void inputMethodForAddition() {

        
        System.out.println("A basic addition program of two digits: " );
        //Making scanner class object here
        Scanner scan = new Scanner(System.in);


        System.out.println("Enter number two");
        int num2 = scan.nextInt();

        //Adding 
        System.out.println("Here is the Sum : ");
        int sum = num1 + num2;
        
        System.out.println("The sum of numbers is : " +sum);
    }
    
}

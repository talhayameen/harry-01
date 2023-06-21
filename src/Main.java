import java.util.Scanner;

public class Main {


    public static void inputMethodForAddition() {

        
        System.out.println("A basic addition program : " );
        //Making scanner class object here
        Scanner scan = new Scanner(System.in);

        //Taking some input in int/
        System.out.println("Enter number one");
        int num1 = scan.nextInt();
        System.out.println("Enter number two");
        int num2 = scan.nextInt();

        //Adding 
        System.out.println("Here is the Sum : ");
        int sum = num1 + num2;
        System.out.println("The sum of numbers is : " +sum);
    }


    public static void main(String[] args)
    {
        System.out.println("Hi Exercise 1 java");
        inputMethodForAddition();
    }


}
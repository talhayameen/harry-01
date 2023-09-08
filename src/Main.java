import banking.connection;
import banking.testCon;
import userApp.DatabaseConnection;

public class Main {


    public static void main(String[] args) throws Exception
    {
        System.out.println("\n\n\nHi Enjoying Learning Java ? \n");

        // Calling DB Con

        DatabaseConnection databaseConnection = new DatabaseConnection();
        databaseConnection.databaseConnection();
        
        // connection con = new connection();        
        // con.readDataBase();

        // testCon testCon = new testCon();
        // testCon.connectionTest();



        //Calling BankApp
        // bankApp bankapp = new bankApp("talha", "345");
        // bankapp.showMenu();
        
        //Calling AdditionMethod
        // simpleAddition simpleadd = new simpleAddition();
        // simpleadd.inputMethodForAddition();
        
        
        //Calling 2-D array
        // multiDimentionalArray multdim = new multiDimentionalArray();
        // multdim.workingMultidimentionalArrays();


        //Calling methodOverloading
        // methodOverloading methodoverloading = new methodOverloading();
        // methodoverloading.multiply(34,45);

        //Calling Factorial
        // factorial fact = new factorial();
        // int value = fact.fact(5);
        // System.out.println("Factorial : " +value);

        //Calling Palindrome
        // palindromeChecker palindromeChecker = new palindromeChecker();
        // Boolean result = palindromeChecker.isPalindrome("madam");
        // if (result == true)
        // {

        //     System.out.println("Yes ! Its a palindrome \n");
        // }
        // else{

        //     System.out.println("No ! Its not a palindrome \n");
        // }

        // nestedPalindrome nestedPalindrome = new nestedPalindrome();
        // Boolean res = nestedPalindrome.isnestPalindrome("talha");
        // if (res == true)
        // {

        //     System.out.println("Yes ! Its a palindrome \n");
        // }
        // else{

        //     System.out.println("No ! Its not a palindrome \n");
        // }

    //###############################################################
    // bubbleSort bs = new bubbleSort();
    // int arr[] ={4,2,1,7,5,3};

    // System.out.println("Array Before Bubble Sort");
    // for(int x=0; x < arr.length; x++){
    //   System.out.print(arr[x] + " \n");
    // }

    // System.out.println();
    // bs.bubbleSortmeth(arr);

    // System.out.println("Array After Bubble Sort");

    // for(int x=0; x < arr.length; x++){
    //   System.out.print(arr[x] + " \n");
    // }
    //###############################################################


    }


}
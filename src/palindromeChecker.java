public class palindromeChecker {
    
    
    public boolean isPalindrome(String input){

        //taking input
        String cleanedup = input.replaceAll("a-zA-Z0-9", "").toLowerCase();

        //get length in a variable of cleaned input
        int length = cleanedup.length();


    for(int i = 0 ; i < length / 2 ; i++)
    {

        if(cleanedup.charAt(i) != cleanedup.charAt(length - 1 - i)){
            return false;
        }

    }
    return true;



    
 }

    
}

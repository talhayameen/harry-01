public class palindromeChecker {
    
    
    public static boolean isPalindrome(String input){

        //taking input
        String cleanedup = input.replaceAll("a-zA-Z0-9", "").toLowerCase();

        //get length in a variable of cleaned input
        int length = cleanedup.length();

    //loop wise checking both end of the string for palindrome
    //When checking if a string is a palindrome, we iterate 
    //through the characters from both ends and compare them. 
    //The reason we divide the length of the string by 2 is to avoid redundant comparisons.

    //Let's consider an example to understand this. Suppose we have the string "racecar". 
    //If we compare the characters from both ends without dividing the length by 2, 
    //we would perform the following comparisons:

    // Comparing the first character 'r' with the last character 'r'
    // Comparing the second character 'a' with the second-to-last character 'a'
    // Comparing the third character 'c' with the third-to-last character 'c'

    //Notice that the comparisons are symmetrical, and we don't need to compare each character twice.
    // By dividing the length of the string by 2, we can ensure that 
    // we only perform comparisons up to the midpoint of the string.

    for(int i = 0 ; i < length / 2 ; i++)
    {

    }




    }

    
}

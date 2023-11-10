package java_programs;
import javax.lang.model.util.ElementScanner6;

public class nestedPalindrome {

    public boolean isnestPalindrome(String input) {

        // taking input
        String cleanedup = input.replaceAll("a-zA-Z0-9", "").toLowerCase();
        System.out.println("We have cleaned your entered x25");

        // get length in a variable of cleaned input
        int res = cleanedup.length();

        for (int i = 0; i < res; i++) {

            for (int j = res - 1; j >= 0; j--) {

                System.out.println("i= " + cleanedup.charAt(i) + " ------ " + "j= " + cleanedup.charAt(j));
                if (cleanedup.charAt(i) == cleanedup.charAt(j)) {
                    return true;
                } else {
                    
                    break;
                }
            }

        }
        return false;

    }

}

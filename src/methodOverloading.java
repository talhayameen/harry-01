public class methodOverloading {

    //look here if I am not using void I have to return a value to the method

    int multiply(int a,int b){

        int c = a * b;
        System.out.println("Multiplication Result : " +c);
        return c;

    }

    double multiply(double a, double b){

        double c = a * b;
        System.out.println("Multiplication Result : " +c);
        return c;
        
    }

    int multiply(int a , int b ,  int c){

        int d = a*b*c;
        System.out.println("Multiplication Result : " +d);
        return d;
    }
    
}

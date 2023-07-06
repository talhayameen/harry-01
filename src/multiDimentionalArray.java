public class multiDimentionalArray {

     public void workingMultidimentionalArrays(){
        int [][] flat; // A 2-D Array

        flat = new int[3][3]; //passing values to initialized 2D array

        //now assigning values into array


        //Row-1
        flat[0][0] = 100;
        flat[0][1] = 101;
        flat[0][2] = 102;

        //Row-2
        flat[1][0] = 103;
        flat[1][1] = 104;
        flat[1][2] = 105;

        //Row-3
        flat[2][0] = 106;
        flat[2][1] = 107;
        flat[2][2] = 108;


        //Displaying Arracy
        for (int i = 0; i<flat.length; i++)
        {

            for (int j = 0; j<flat[i].length; j++)
            {
            System.out.print(flat[i][j]);
            System.out.print(" ");
            }
            
            System.out.println("\n");
            System.out.println("\n");
        }



    }
    
}

public class bubbleSort {


    public void bubbleSortmeth(int[] arr) {
    int n = arr.length;
    int tmp = 0;
    for(int x=0; x < n; x++){

     for(int y=1; y < (n-x); y++)
     {

        if(arr[y-1] > arr[y]){

        //swap elements
        tmp = arr[y-1];
        arr[y-1] = arr[y];

        arr[y] = tmp;

        }
     }
   }
 }

 public int anotherSort(int var){


    return var;

 }
    
}

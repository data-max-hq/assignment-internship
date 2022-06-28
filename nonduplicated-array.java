import java.util.Arrays;

public class Main {

    public static void main(String[] args) {

        //2 vektoret qe do perdorim per testim
        int [] firstArray = {1,2,3,8,100,4,65,9,7,5,5,5,6,6,30,30,30,30};
        int [] secondArray = {5,6,43,8,39,74,9,100};

        //deklarojme vektorin e ri ne menyre dinamike qe te kete maksimumi si permase shumat e dy vektoreve
        int[] newArray = new int[firstArray.length + secondArray.length];

        // indeksimi i vektorit te ri
        int newIteration = 0;

        // nje flag qe do detektoje nqs nje element perseritet ose jo
        int elementDuplicated = 0;


        // iterojme vektorin e pare dhe shohim nqs ka elemente qe perseriten ne te
        for (int i=0; i< firstArray.length ; i++) {
            elementDuplicated = 0;

            if (newIteration!=0) {
                for (int j=0; j<newIteration; j++) {
                    if (firstArray[i] == newArray[j]) {
                        elementDuplicated = 1;
                        break;
                    }
                }
            }
            if (elementDuplicated == 0) {
                newArray[newIteration] = firstArray[i];
                newIteration++;
            }
        }

        // iterojme vektorin e dyte dhe shohim nqs ka elemente qe perseriten ne te
        for (int i=0; i< secondArray.length ; i++) {
            elementDuplicated = 0;
            if (newIteration!=0) {
                for (int j=0; j<newIteration; j++) {
                    if (secondArray[i] == newArray[j]) {
                        elementDuplicated = 1;
                        break;
                    }
                }
            }
            if (elementDuplicated == 0) {
                newArray[newIteration] = secondArray[i];
                newIteration++;
            }
        }

        // printojme vektorin e ri
        System.out.println(Arrays.toString(newArray));

    }
}

import java.util.ArrayList;
import java.util.List;

public class MagicSquare {


    public static void main(String[] args) {
        
        List<List<Integer>> matrix = List.of(
            List.of(5, 3, 4),
            List.of(1, 5, 8),
            List.of(6, 4, 2)
        );

        int results = MagicSquare.formingMagicSquare(matrix);

        System.out.println(results);
    }


    public static int formingMagicSquare(List<List<Integer>> s) {


        int sumConstant = 15;
        List<List<Integer>> seenColoumns = new ArrayList<>();

        for (int i = 0; i<s.size(); i++){

            // check Horizontal
            if (sumEqualsConstant(s.get(i))) {
                continue;
            }
            for (int j = 0; j<s.size(); j++){
                
                // Check vertical
                int start = 0;
                int sum = 0;
                while (start < 3) {
                    sum += s.get(start).get(j);
                    start++;
                }

                if (sum == sumConstant){
                    break;
                }

                // Check diagonal
                
                if (j == 0 || j==2 || (j==1 && i == 1)) {

                    if ((j==0 && i==0) || (i==2 && j==2) || (i==1)){
                        start = 0;
                        sum = 0;
                        while (start< 3) {
                            sum += s.get(start).get(start);
                            start++;
                        }
                        if (sum==15) {
                            break;
                        }
                    }

                    else if ((j==2 && i==0)  ||  (j==0 && i == 2) || (i==1)){
                        start = 2;
                        sum = 0;
                        while (start > -1) {
                            sum += s.get(start).get(start);
                            start--;
                        }

                        if (sum == 15) {
                            break;
                        }
                    }

                }


                System.out.println("Couldn't find sum of 15 in the digonal and vertical and horizontal");

                // Pick the row to get the sum of the numbers 

                int difference = rowDifference(s.get(i), j);

                s.get(i).set(j, difference);
                seenColoumns.add(List.of(s.get(i).get(j), difference));

            }
        }

        System.out.println(seenColoumns);

        return 0;
    }


    public static boolean sumEqualsConstant(List<Integer> row){

        int sum = 0;
        for (int i = 0; i<row.size(); i++){
            sum += row.get(i);
        }
        return sum == 15;
    }

    public static int rowDifference(List<Integer> row, int column){
        // return the differennce
        int sum = 0 ;

        for (int i = 0 ; i< row.size(); i++){
            if (i==column) {
                continue;
            }

            sum += row.get(i);
        }



        return 15 - sum;
    }


    
}

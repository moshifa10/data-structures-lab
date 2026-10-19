
import java.util.ArrayList;
import java.util.List;

public class MagicSquare {

    public static void main(String[] args) {

        List<List<Integer>> matrix = new ArrayList<>(List.of(
                new ArrayList<>(List.of(5, 3, 4)),
                new ArrayList<>(List.of(1, 5, 8)),
                new ArrayList<>(List.of(6, 4, 2))
        ));

        List<List<Integer>> matrix2 = new ArrayList<>(List.of(
                new ArrayList<>(List.of(4, 8, 2)),
                new ArrayList<>(List.of(4, 5, 7)),
                new ArrayList<>(List.of(6, 1, 6))
        ));

        int results = MagicSquare.formingMagicSquare(matrix);
        int results2 = MagicSquare.formingMagicSquare(matrix2);

        System.out.println(results);
        System.out.println(results2);
    }

    public static int formingMagicSquare(List<List<Integer>> s) {

        int sumConstant = 15;
        List<List<Integer>> seenColumns = new ArrayList<>();

        for (int i = 0; i < s.size(); i++) {

            // check Horizontal
            if (sumEqualsConstant(s.get(i))) {
                continue;
            }

            for (int j = 0; j < s.size(); j++) {

                // Check vertical
                int start = 0;
                int sum = 0;

                while (start < 3) {
                    sum += s.get(start).get(j);
                    start++;
                }

                if (sum == sumConstant) {
                    continue;
                }

                // Check diagonal
                if (j == 0 || j == 2 || (j == 1 && i == 1)) {

                    // FIXED: Top-left to bottom-right
                    if ((j == 0 && i == 0) || (i == 2 && j == 2)) {
                        start = 0;
                        sum = 0;

                        while (start < 3) {
                            sum += s.get(start).get(start);
                            start++;
                        }

                        if (sum == 15) {
                            continue;
                        }
                    }

                    // FIXED: Top-right to bottom-left
                    else if ((j == 2 && i == 0) || (j == 0 && i == 2)) {
                        start = 2;
                        sum = 0;

                        while (start > -1) {
                            sum += s.get(start).get(2 - start);
                            start--;
                        }

                        if (sum == 15) {
                            continue;
                        }
                    }

                    else if ((i == 1 && j == i)) {
                        start = 0;
                        sum = 0;

                        while (start < 3) {
                            sum += s.get(start).get(start);
                            start++;
                        }

                        if (sum == 15) {
                            continue;
                        }

                        start = 2;
                        sum = 0;

                        while (start > -1) {
                            sum += s.get(start).get(2 - start);
                            start--;
                        }

                        if (sum == 15) {
                            continue;
                        }
                    }
                }

                // Pick the row to get the sum of the numbers
                if (sumEqualsConstant(s.get(i))) {
                    break;
                }

                int difference = rowDifference(s.get(i), j);
                seenColumns.add(List.of(s.get(i).get(j), difference));
                s.get(i).set(j, difference);
            }
        }

        return cost(seenColumns);
    }

    public static int cost(List<List<Integer>> differenceCost) {
        System.out.println(differenceCost);
        int difference = 0;

        for (int i = 0; i < differenceCost.size(); i++) {
            difference += Math.abs(differenceCost.get(i).get(0) - differenceCost.get(i).get(1));
        }

        return Math.abs(difference);
    }

    public static boolean sumEqualsConstant(List<Integer> row) {
        int sum = 0;

        for (int i = 0; i < row.size(); i++) {
            sum += row.get(i);
        }

        return sum == 15;
    }

    public static int rowDifference(List<Integer> row, int column) {
        // return the difference
        int sum = 0;

        for (int i = 0; i < row.size(); i++) {
            if (i == column) {
                continue;
            }
            sum += row.get(i);
        }

        return Math.abs(15 - sum);

    }
}

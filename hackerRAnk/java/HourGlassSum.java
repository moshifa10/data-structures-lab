import java.util.ArrayList;
import java.util.List;

public class HourGlassSum{

    public static void main(String[] args) {
        List<List<Integer>> matrix = new ArrayList<>(List.of(
                List.of(-9, -9, -9, 1, 1, 1),
                List.of(0, -9, 0, 4, 3, 2),
                List.of(-9, -9, -9, 1, 2, 3),
                List.of(0, 0, 8, 6, 6, 0),
                List.of(0, 0, 0, -2, 0, 0),
                List.of(0, 0, 1, 2, 4, 0)
        ));
        System.out.println(hourglassSum(matrix));
    }


    public static int hourglassSum(List<List<Integer>> arr) {
        // Write your code here
        int holder = 0;
        List<Integer> integers = new ArrayList<>();
        for (int i = 0; i<arr.size()-2; i++){
            for (int j = 0; j< arr.size()-2; j++) {
                holder += arr.get(i).get(j);
                holder += arr.get(i).get(j+1);
                holder += arr.get(i).get(j+2);
                holder += arr.get(i+2).get(j);
                holder += arr.get(i+2).get(j+1);
                holder += arr.get(i+2).get(j+2);
                holder += arr.get(i+1).get(j+1);
                integers.add(holder);
                holder = 0;

            }
        }
        int higher = integers.get(0);
        for (int i = 1; i<integers.size(); i++){
            if(integers.get(i) > higher){
                higher = integers.get(i);
            }
        }
        return  higher;

    }
}
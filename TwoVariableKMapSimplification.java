import java.util.*;

public class TwoVariableKMapSimplification {
    public static void main(String[] args) {
        int[][] karnaughMap = {
            {0, 1},
            {1, 0}
        };

        String simplifiedExpression = simplifyKarnaughMap(karnaughMap);
        System.out.println("Simplified Boolean Expression: " + simplifiedExpression);
    }

    public static String simplifyKarnaughMap(int[][] karnaughMap) {
        int rows = karnaughMap.length;
        int cols = karnaughMap[0].length;
        List<String> terms = new ArrayList<>();

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (karnaughMap[i][j] == 1) {
                    String term = String.format("(%c%c)", (char) ('A' + j), (char) ('B' + i));
                    terms.add(term);
                }
            }
        }

        if (terms.isEmpty()) {
            return "0"; // The function is a constant 0
        } else {
            StringBuilder expression = new StringBuilder();
            for (String term : terms) {
                if (expression.length() > 0) {
                    expression.append(" + ");
                }
                expression.append(term);
            }
            return expression.toString();
        }
    }
}

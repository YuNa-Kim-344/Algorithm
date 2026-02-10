class Solution {
    public int solution(int n) {
        int answer = 0;

        // 10진수 -> 3진수 (정방향)
        String ternaryNum = changeTernary(n);

        // 3진수 문자열 뒤집기
        String reversedNum = reversal(ternaryNum);

        // 3진수 -> 10진수
        answer = changeDecimal(reversedNum);

        return answer;
    }

    // 10진수 -> 3진수 변환
    private String changeTernary(int n) {
        String ternaryNum = "";
        while (n > 0) {
            ternaryNum = (n % 3) + ternaryNum;
            n /= 3;
        }
        return ternaryNum;
    }

    // 문자열 뒤집기
    private String reversal(String n) {
        return new StringBuilder(n).reverse().toString();
    }

    // 3진수 -> 10진수 변환
    private int changeDecimal(String n) {
        return Integer.parseInt(n, 3);
    }
}

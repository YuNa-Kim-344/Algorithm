public class Solution {
    public int solution(int n) {
        int answer = 0;

        while (n > 0){
            int i = n%10;
            answer += i;
            n = n/10;
        }

        return answer;
    }
}

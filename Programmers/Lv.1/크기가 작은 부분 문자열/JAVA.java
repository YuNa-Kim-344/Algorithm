class Solution {
    public int solution(String t, String p) {
        int answer = 0;

        int p_len = p.length();
        int t_len = t.length();
        long p_int = Long.parseLong(p);

        for (int i = 0; i <= t_len - p_len; i++) {
            long t_number = Long.parseLong(t.substring(i, i + p_len));
            if (t_number <= p_int) {
                answer++;
            }
        }

        return answer;
    }
}

class Solution {
    public String solution(String s) {
        String answer = "";
        int m = 0;
        
        int len = s.length();
        if(len%2 == 0){
            m = len/2 -1;
            answer = s.substring(m, m+2);
        }else{
            m = len/2;
            answer = String.valueOf(s.charAt(m));
        }
        
        return answer;
    }
}

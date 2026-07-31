class Solution {
    public String solution(String phone_number) {
        String answer = "";
        
        int l = phone_number.length();
        
        for(int i = 0; i < l-4; i++){
            answer += "*";
        }
        
        for(int i = l-4; i<l;i++){
            answer += phone_number.charAt(i);
        }
        
        return answer;
    }
}

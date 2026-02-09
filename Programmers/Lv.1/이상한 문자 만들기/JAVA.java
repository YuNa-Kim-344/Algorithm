class Solution {
    public String solution(String s) {
        String answer = "";
        
        String[] words = s.split(" ", -1);
        
        
        for(String word:words){
            String newWord = "";
            
            for(int i=0; i < word.length(); i++){
                char c = word.charAt(i);
                if (i % 2 == 0) {
                    newWord += Character.toUpperCase(c);
                } else {
                    newWord += Character.toLowerCase(c);
                }
            }
             answer += newWord + " ";
        }
        if (!answer.isEmpty()) {
            answer = answer.substring(0, answer.length() - 1);
        }
        
        return answer;
    }
}

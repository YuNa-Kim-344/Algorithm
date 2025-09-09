import java.util.*;

class Solution {
    public int solution(String s) {
        Map <String, String> num_dic = new HashMap<>();
        
        int answer = 0;
        
        num_dic.put("zero" , "0");
        num_dic.put("one", "1");
        num_dic.put("two", "2");
        num_dic.put("three", "3");
        num_dic.put("four", "4");
        num_dic.put("five", "5");
        num_dic.put("six" , "6");
        num_dic.put("seven", "7");
        num_dic.put("eight", "8");
        num_dic.put("nine", "9");
        
    
        for (Map.Entry<String, String> entry : num_dic.entrySet()) {
            s = s.replace(entry.getKey(), entry.getValue());
        }

        answer = Integer.parseInt(s);
    
        
        return answer;
    }
}

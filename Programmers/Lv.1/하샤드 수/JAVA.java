class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        int sum = 0;
        
        String num = String.valueOf(x);
        String[] num_list = num.split("");
        for(String s : num_list){
            sum += Integer.parseInt(s);
        }
        
        if(x%sum != 0){
            answer = false;
        }
        
        return answer;
    }
}

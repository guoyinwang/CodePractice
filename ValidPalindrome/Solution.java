public class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }
        int div =1;
        while(x/div>=10){div =div *10;}
        int left =x;
        int right =x;
        while(div>1){
            if(left/div !=right%10){ return false;}
            else{
                left = left - (left/div)*div ;
                right = right /10;
                div =div/10;
            }
            
        }
        return true;
    }
    public static void main(String[] args){
        int x =121;
        Solution a = new Solution();
        System.out.println(a.isPalindrome(x));
    
    }
}
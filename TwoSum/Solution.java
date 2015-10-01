import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> map = new HashMap<Integer,Integer>();
        for (int i=0;i<nums.length;i++)
        {
            int x = nums[i];
            if(map.containsKey(target - x))
            {
                return new int[] {map.get(target-x)+1,i+1};
            }
            else
            {
                map.put(x,i);
            }
            
        }
        throw new IllegalArgumentException("No two sum solution");
    }
    public static void main(String[] args) {
    	int[] nums = {3,2,4};
    	int target = 6;
    	Solution a = new Solution();
    	int[] result = a.twoSum(nums, target);
    	System.out.println(Arrays.toString(result));
    }
}
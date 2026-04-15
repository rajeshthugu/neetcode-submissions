class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> diffs = new HashMap<>();
        for(int i=0; i<nums.length;i++){
            int diff = target - nums[i];
            if(diffs.containsKey(nums[i])){
                return new int[]{diffs.get(nums[i]), i};
            }
            diffs.put(diff, i);
        }

        return new int[]{-1,-1};
        
    }
}

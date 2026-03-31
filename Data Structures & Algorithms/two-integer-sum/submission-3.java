class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> sumMap = new HashMap<Integer, Integer>();
        // int[] answers = new int[2];
        for (int index = 0; index < nums.length; index++) {
            if (sumMap.containsKey(target-nums[index])) {
                // answers[1] = index;
                // answers[0] = sumMap.get(target-nums[index]);
                return new int[] {sumMap.get(target-nums[index]), index};
                // break;
            }
            sumMap.put(nums[index], index);
        }

        return new int[0];

    }
}

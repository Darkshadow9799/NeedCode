class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        int lengthOfString = s.length();
        Map<Character, Integer> anagramMap = new HashMap<Character, Integer>();
        for (int index = 0; index < lengthOfString; index++){
            char stringChar = s.charAt(index);
            char tStringChar = t.charAt(index);
            anagramMap.put(stringChar, anagramMap.getOrDefault(stringChar, 0) + 1);
            anagramMap.put(tStringChar, anagramMap.getOrDefault(tStringChar, 0) - 1);
        }

        for (Map.Entry<Character, Integer> entry : anagramMap.entrySet()) {
            if (entry.getValue() != 0) return false;
        }

        return true;
    }
}

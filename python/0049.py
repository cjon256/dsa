class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}

        output = []
        for word in strs:
            cw = "".join(sorted(word))
            if cw in anagrams_dict:
                anagrams_dict[cw].append(word)
            else:
                word_list = [word]
                output.append(word_list)
                anagrams_dict[cw] = word_list
        return output

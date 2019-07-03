def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]

        Given an array of strings, group anagrams together.
        """
        s_ana = {}
        result = []
        
        for word in strs:
            joined = ''.join(sorted(word))
            if joined not in s_ana:
                s_ana[joined] = [word]
            else:
                s_ana[joined].append(word)
        
        for anag in s_ana.keys():
            result.append(sorted(s_ana[anag]))
        
        return sorted(result, key=len)
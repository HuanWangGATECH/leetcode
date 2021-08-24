class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        result=[]
        
        for word in words:
            if self.sameRow(word):
                result.append(word)
                
        return result
            
            
    def sameRow(self,word):
        dictString={}
        
        for s in "qwertyuiop":
            
            dictString[s]=1
        
        for s in "asdfghjkl":
            dictString[s]=2
        
        for s in "zxcvbnm":
            dictString[s]=3
        prev=0
        for s in word:
            character=s.lower()
            if prev==0:
                prev=dictString[character]
            
            if dictString[character]!=prev:
                return False 
            
            
            prev=dictString[character]
            
        return True 
        
        
# others solution that is smart 


class Solution:
    def findWords(self, words):
        first_row = set(list('qwertyuiop'))
        second_row = set(list('asdfghjkl'))
        third_row = set(list('zxcvbnm'))
        word_list = []
        for word in words:
            res = 0

            word_set = set(list(word.lower()))
            if word_set.intersection(first_row) == word_set:
                res+=1
            if word_set.intersection(second_row) == word_set:
                res+=1
            if word_set.intersection(third_row) == word_set:
                res+=1
            if res:
                word_list.append(word)
        return word_list

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
        
        

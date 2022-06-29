
class Solution:
    def romanToInt(self, s: str) -> int:
        
        table={'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,
			'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
            
        value=0
        temp=''
        cursor=0
        while cursor<len(s): # length of input string
			
			# Check now character, now+1 character
			# while string length
			# check two characters
            if (cursor+1)!=len(s) and s[cursor]+s[cursor+1] in table:
                value+=table[s[cursor]+s[cursor+1]]
                cursor+=2
            else:
                # if not two characters, check one character
                value+=table[s[cursor]]
                cursor+=1
                
        return value
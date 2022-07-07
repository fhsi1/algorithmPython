vowels = ['a', 'e', 'i', 'o', 'u', 'y']
def sol(s):
    ans = ''
    s = s.lower()
    for i in vowels:
        s = s.replace(i, '')
    for i in s:
        ans += '.'
        ans += i
 
    return ans
s = input()
print(sol(s))
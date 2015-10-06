# return a greeting of the form "Hello Bob!". 
def hello_name(name):
    result1 = "{0}{1}{2}".format('Hello ',name,'!')
    return result1
      
# Given two strings, a and b, return the result 
# of putting them together in the order abba, 
# e.g. "Hi" and "Bye" returns "HiByeByeHi". 
def make_abba(a, b):
    result2 = "{0}{1}{1}{0}".format(a,b)
    return result2 
    
# The web is built with HTML strings like "<i>Yay</i>" 
# which draws Yay as italic text. 
# In this example, the "i" tag makes <i> and </i> which 
# surround the word "Yay". 
# Given tag and word strings, create the HTML string 
# with tags around the word, e.g. "<i>Yay</i>".
def make_tags(tag, word):
    a=list(tag)
    a.insert(1,'/')
    a=''.join(a)
    result3 = "{0}{1}{2}".format(tag,word,a)
    return result3
    
# Given an "out" string length 4, such as "<<>>", and a word, 
# return a new string where the word is in the middle of the 
# out string, e.g. "<<word>>". 
def make_out_word(out, word):
    result4 = out[:2]+word+out[2:]
    return result4
    
# Given a string, return a new string made of 3 copies of the last 
# 2 chars of the original string. The string length will be at least 2. 
def extra_end(str):
    result5 = 3*'{0}'.format(str[-2:])
    return result5
    
    
# Given a string, return the string made of its first two chars, 
# so the String "Hello" yields "He". If the string is shorter than 
# length 2, return whatever there is, so "X" yields "X", and the 
# empty string "" yields the empty string "". 
def first_two(str):
    result6 = str[:2] if len(str)>2 else str
    return result6
    

# Given a string of even length, return the first half. 
# So the string "WooHoo" yields "Woo". 
def first_half(str):
    result7 = str[:int(len(str)/2)]
    return result7
    

# Given a string, return a version without the first and last char, 
# so "Hello" yields "ell". The string length will be at least 2. 
def without_end(str):
    result8 = str[1:-1]
    return result8
    
    
# Given 2 strings, a and b, return a string of the form short+long+short, 
# with the shorter string on the outside and the longer string on the inside. 
# The strings will not be the same length, but they may be empty (length 0). 
def combo_string(a, b):
    result9='{0}+{1}+{0}'.format(a,b) if len(b)>len(a) else '{0}{1}{0}'.format(b,a)
    return result9
    
    
# Given 2 strings, return their concatenation, except omit the first char of each. 
# The strings will be at least length 1. 
def non_start(a, b):
    result10 = a[1:]+b[1:]
    return result10
    
       
# Given a string, return a "rotated left 2" version where the first 2 chars 
# are moved to the end. The string length will be at least 2. 
def left2(str):
    result11=str[2:]+str[:2]
    return result11


def checkKey(dic, key):  
    if key in dic: 
        print("The given key value is Present in the dictionary.") 
        print("The value for given key is:", dic[key]) 
    else: 
        print("The given key value isnot Present in the dictionary.") 
# Driver Code 
dic = {'a': 100, 'b':200, 'c':300} 
print("The dictionary is:", dic) 
key = input("enter the key")

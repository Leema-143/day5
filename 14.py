def Check_Vow(string, vowels): 
    final = [each for each in string if each in vowels] 
    print("The number of vowels in the string is:",len(final)) 
    print("The vowels are:",final) 
# Driver Code 
string = input("enter the string for finding no.of vowels in the string:") 
vowels = "AaEeIiOoUu" 
Check_Vow(string, vowels)

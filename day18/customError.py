#we can address the problem faced on day 5 using custom errors

a = int(input("Enter any value between 5 and 9"))

if(a<5 or a>9):
    raise ValueError("Value shuld be between 5 and 9")

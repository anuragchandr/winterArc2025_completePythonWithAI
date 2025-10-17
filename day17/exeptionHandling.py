a = input("Enter a Number:")
print(f"Multiple table of {a} is: ")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
#except ValueError:     #(IndexError)
    #print("Number Entered is not an integer")
#except:
    #print(""Error)
print("Some imp lines of Code")


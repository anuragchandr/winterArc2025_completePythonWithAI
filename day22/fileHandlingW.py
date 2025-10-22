f = open('myfile2.txt','w') #write Mode(it overwrites but to append text we use append mode )
f.write("Hello World")
f.close()
#f.truncate(5)
f = open('myfile2.txt','a')
f.write("Hello World")
f.close()

with open("myfile2.txt", 'a') as f:
    f.write("Hello")
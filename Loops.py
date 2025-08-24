# only two type of loop
#for and while
# #range(start, stop, step)


# for i in range(0,11,2):
#     print(i)


#reverse order
# for i in range(10,-1,-1):   #10 to 0
#     print(i)


# for i in range(-5,-15,-1):   #-5 to -15
#     print(i)



#lets print a table of five
# for i in range(1,11,1):
#     print(f"5 * {i} = {i*5}")

# for i in range(7,(7*10)+1,7):
#     print(i)

#question 1
# len=int(input("Enter the no. "))

# for i in range(len):
#     print(f"{i+1} Hello world")



#question 2
# num=int(input("Enter the number: "))
# total=0

# for i in range(1,num+1):
#     total+=i

# print(total)

#question factorial

# num=int(input("Enter the no.: "))
# total=1

# for i in range(1,num+1,1):
#     total*=i

# print(total)

#question check perfect number

# num=int(input("Enter the number: "))
# total=0
# check=False
# for i in range(1,(num//2)+1):
#     total+=i
#     if total==num :
#         check=True
#         break

# if(check):
#     print("Yes it is a perfect number")
# else:
#     print("No it is not a perfect number")



#reverse a string

# s=str(input("Enter the word: "))
# for i in range(len(s)-1,-1,-1):
#     print(s[i])


#check string is palindrom or not
# s=str(input("Enter the word: "))
# check=True
# b=len(s)-1

# for i in range(len(s)//2):
#     if(s[i]!=s[b]):
#         check=False
#         break
#     else:
#         b-=1

# if(check):
#     print("yes")
# else:
#     print("No")


# s=str(input("Enter the value: "))
# Chars=0
# Digits=0
# Symbol=0

# for i in s:
#     if i.isdigit():
#         Digits+=1
#     elif i.isalpha():
#         Chars+=1
#     else:
#         Symbol+=1

# print(f"Chars= {Chars}\n Digits= {Digits}\n Symbol= {Symbol} ")



# while loop        while condition

# s="nikhil"
# start=0
# end=len(s)-1
# check=True
# while start<end :
#     if s[start]!=s[end]:
#         check=False
#         break
#     else:
#         start+=1
#         end-=1

# if(check):
#     print("yes")
# else:
#     print("no")


# start=0
# end=10

# while start<end :
#     print(f"{start} and {end}")
#     start+=1
#     end-=1



#seperate all digit like 256    o/p  6,5,2

# a=121
# b=a
# total=0

# while a!=0:
#     print(a%10)
#     total=total*10+(a%10)
#     a//=10
    
# print(total)
# print(b)

# if(b==total):
#     print("yes")
# else:
#     print("no")


a=0
while a!=3:
    num=int(input("Guess the no. between 1 to 10: "))
    if(num==8):
        print("------Yes you guess the right number----")
        break
    else:
        print("Sorry you guess wrong number try again ")
    a+=1

if(a==3):
    print("-------Sorry you Loss------")
my_srt = "hello people****"
rep_str = my_srt.replace("*","")
print(rep_str)

print("----------------------------")

numbers = [1,5,3,2,5,47,23,0,9,11,2,81,6,2,99,1555] 
my_flag = False 
for i in numbers:
    if i > 1:
        for j in range(2 , int(i ** 0.5) + 1): 
            if (i % j) == 0:
                my_flag = True 
                break
    if my_flag:
        print(i, "Not a prime number")
        my_flag = False
    else:
        print(i, "a prime number")

print("----------------------------")

abcde = "abcdefghijklmnopqrstuvwxyz"
my_paragrah = "Hello people lorem ipusem it is just test  "
for each in abcde:
    counter = my_paragrah.count(each)
    if counter >1 :
        print (each , counter)


print("end")
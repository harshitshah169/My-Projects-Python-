count = 99
for num in range(100):
    if count>=2:
        print(str(count) + " bottles of beer on the wall, "+ str(count) + " bottles of beer.")
        count = count - 1
        print("Take one down and pass it around, " + str(count) + " bottles of beer on the wall.\n")


print(str(count) + " bottles of beer on the wall, "+ str(count) + " bottles of beer.")
print("Take one down and pass it around, no more bottles of beer on the wall.\n")
print("No more bottles of beer on the wall, no more bottles of beer. ")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")

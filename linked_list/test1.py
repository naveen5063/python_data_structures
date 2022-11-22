input = "32 4 S 5 13 S 9 6 S 4 1 G 4 S 6 1 S 8 11 G 13 G 1 S 12 12 G 10 S 15 13 S 2 13 S 7 5 S 10 3 G 6 G 10 S 15 14 S 5 12 G 5 G 7 G 15 G 5 G 6 G 10 S 7 13 G 14 S 8 9 G 4 S 6 11 G 9 S 6 12 G 3"
operations = "S 5 13 S 9 6 S 4 1 G 4 S 6 1 S 8 11 G 13 G 1 S 12 12 G 10 S 15 13 S 2 13 S 7 5 S 10 3 G 6 G 10 S 15 14 S 5 12 G 5 G 7 G 15 G 5 G 6 G 10 S 7 13 G 14 S 8 9 G 4 S 6 11 G 9 S 6 12 G 3"

res = operations.split(' ')
print("res", res)
#capacity = res[1]

setoperation = 2
getoperation = 1
count = 0

while count < len(input):
    if input[count] == "S":
        val = f'l1.set({input[count+1]}{count+2})'
        count += setoperation+1
    if input[count] == "G":
        val = f'l1.set({input[count + 1]})'
        count += getoperation +1
formNumber = 24
toNumber = 1280
searchedDigit = 0

def dig_count ( number, digit ):
    br = 0
    n = number
    while n > 0:
        #print (n)
        if  n % 10 == digit:
            br += 1
        n = n // 10
    return br

digits_number = 0
for i in range (formNumber, toNumber+1):
    cnt_dig = dig_count(i, searchedDigit)
    digits_number += cnt_dig
    print (i, ' - ', cnt_dig)

print ("Digits " + str(searchedDigit) + " from " + str(formNumber) + " to " + str(toNumber) + " are " + str(digits_number))   

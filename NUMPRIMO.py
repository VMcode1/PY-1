num = int (input ('Digite um número:'))
total = 0
for c in range (1, num + 1):
    if num % c == 0 :
        print ('\033[34m')
        total += 1
    else:
        print ('\033[m')
    print ("{}".format(c) , end = '')
    if total == 2:
        print ( " Então ele é primo!")
    else:
        print ("Então ele não é primo!")    
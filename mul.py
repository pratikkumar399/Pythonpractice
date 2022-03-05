def print_table(num):
    for i in range(num, 21):
        for j in range(1,21):
            print("%-5d X %5d = %5d" % (i, j, i*j))
        print('************')
        


n = int(input('Please Enter the number from which you want to print the multiplication table: '))


print_table(n)

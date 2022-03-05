# Python program to demonstrate
# opening a file


# Open function to open the file "myfile.txt"
# (same directory) in append mode and store
# it's reference in the variable file1
file1 = open("myfile.txt", "a")

# Writing to file
file1.write("\nWriting to file :)")

# Closing file
file1.close()

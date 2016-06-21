#my_file = open('22.txt', 'r')
#first_line = my_file.readline()
#second_line = my_file.readline()
#print "first line = ", first_line
#print "second line = ", second_line
#my_file.seek(0)

my_file = open('22.txt','a')
my_file.write('\nappend 3st!')
print >> my_file, "\nappend 4st!"
my_file.close()
my_file = open('22.txt', 'r')
lines = my_file.readlines()
print lines
my_file.close()

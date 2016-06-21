#write a txt file include number 0~99999999.
#time:2016-05-24
#authur:SunJoy

my_file = open('pswd.dic', 'w')
my_file.write("password ")
for i in range(100000000):
    if len(str(i)) < 8:
        my_file.write("0"*(8-len(str(i)))+'%d'%i+" ")
    else:
        my_file.write('%d'%i+" ")
my_file.close()

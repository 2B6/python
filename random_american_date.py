#the program generate random date in american style
import random, os
path = 'C:\\Users\\12931\\Desktop\\coding\\python\\codes\\c9'
if not(os.path.exists('american_date')):
    os.makedirs('american_date');
os.chdir(path+'\\american_date')

for file in range(50):
    #American-style dates (MM-DD-YYYY)
    month_1 = [1,3,5,7,8,10,12]
    month_2 = [4,6,9,11]
    month_3 = [2]
    
    random.shuffle(month_1)
    random.shuffle(month_2)

    file_name = ['','','']
    file_name[0] = str(month_1[0]) +'-'+ str(random.randint(1,31)) + '-2018.txt'
    file_name[1] = str(month_2[0]) +'-'+ str(random.randint(1,30)) + '-2018.txt'
    file_name[2] = str(month_3[0]) +'-'+ str(random.randint(1,28)) + '-2018.txt'
    
    random.shuffle(file_name)
    file = open(file_name[0], 'w')
    file.close()
    
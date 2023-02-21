import os as fuk


ch = ' '
#kaya to empty kase gagamitin naten sa while loop

file = input('input the file name you want to use or to create or enter the existing file name without the extension:')
t = '.txt'
tt = file + t
#pinag sama ko yung file name at .txt para maging file sya
#makikita nyo sa function na addData na with open tt ayun na yong file nyo msmo na na create nyo


def addData():
    fuk.system('clear')
    #ginamitan ko ng a yung file instead of w para pag nag add ako ng data hindi mawala yung naunang data
    with open(tt, 'a') as tae:
        text = input('Add data::')
        #etong text variable ang mag sisilbing data input nyo
        tae.write(text+'\n')
        #makikita nyo den na nag write ako file using write method
        tae.close()
        print('Your data', text,' added to list')
    
    
def viewData():
    fuk.system('clear')
    with open(tt, 'r') as file:
        t = file.read()
        print(t)
        

        #etong part na to para makita nyo yung nilalaman ng file na ginawa nyo
        #pero with newline sya syempre
        lines = [[x.rstrip('\n')] for x in file]
        print(lines)
        file.close()
        
def deleteData():
    fuk.system('clear')
    if fuk.path.exists(tt):
        #yung tt ayan yng variable na may value na filename.txt
        #so idedelete nya yan pag natawag yung function
        fuk.remove(tt)
        print('deleted!')

    else:
        #kung mapindot mo ulet eto i aoutput nya pag wala ng ung file
        print('No file was found!')
        
def viewPath():
        fuk.system('clear')
        #common naman na kita na sa vaariable na path sya or list ng directory
        path = fuk.listdir('/storage/emulated/0/download/termux/pract/pqssword manager/bank pract')
        print(path)
        
def deleteItem():
    fuk.system('clear')
    with open(tt,'w') as tae:
        tae.write(' ')
        #naka white space yung write method para ma replace lahat ng data sa loob
        #take note w ginamit ko imbes na a, para lahat ma rewrite
        print('All data are erased!')

while ch != 'q':
    print('''1.Add data\n2.View data\n3.Delete file\n4.Delete items\n5.View Files''')
    
    ch = input('E::')
    
    if ch == '1':
        addData()
    elif ch == '2':
        viewData()
    elif ch == '3':
        deleteData()
    elif ch == '4':
        deleteItem()
    elif ch == '5':
        viewPath()
    else:
        print('bye!')


print("BYE!")

import os as fuk


ch = ' '

file = input('input the file name you want to use or to create or enter the existing file name without the extension:')
t = '.txt'
tt = file + t
#if file == null:
    


def addData():
    fuk.system('clear')
    with open(tt, 'a') as tae:
        text = input('Add data::')
        tae.write(text+'\n')
        tae.close()
        print('Your data', text,' added to list')
    
    
def viewData():
    fuk.system('clear')
    with open(tt, 'r') as file:
        t = file.read()
        print(t)
        
        if file == False:
            viewPath()
        
        lines = [[x.rstrip('\n')] for x in file]
        print(lines)
        file.close()
        
def deleteData():
    fuk.system('clear')
    if fuk.path.exists(tt):
        fuk.remove(tt)
        print('deleted!')

    else:
        print('No file was found!')
        
def viewPath():
        fuk.system('clear')
        path = fuk.listdir('/storage/emulated/0/download/termux/pract/pqssword manager/bank pract')
        print(path)
        
def deleteItem():
    fuk.system('clear')
    with open(tt,'w') as tae:
        tae.write(' ')
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
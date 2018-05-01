#Backing Up a Folder into a ZIP File with different versions
import os, zipfile

#TODO: find directory
def find_dir():
    print('C:\\Users\\12931\\Desktop\\coding\\python\\codes\\c9\\american_date')
    path = input("Enter your zip source directory (single back slash): ")
    print('Recieved: %s ' % (path))
    return path
    
# TODO: figure out name
def find_name(file_path, dump_path):
    file_name = os.path.basename(file_path)
    version = 0
    
    temp_name = file_name
    #figure out version of file
    while(os.path.exists(temp_name)):
        version = version + 1
        temp_name = file_name + str(version)
    
    file_name = file_name + str(version)
    return file_name
        
    
# TODO: zip folder
def zip_dir(file_path, file_name, dump_path):
    newZip = zipfile.ZipFile(file_name, 'a')
    os.chdir(file_path)
    for single_file in os.listdir(file_path):
        newZip.write(single_file, compress_type=zipfile.ZIP_DEFLATED)
    newZip.close()
    os.chdir(dump_path)
    return newZip

#main
#dump zip into a higher dir
file_path = find_dir()
dump_path = os.path.dirname(file_path)
#print(dump_path)
os.chdir(dump_path)

file_name = find_name(file_path, dump_path)
#print(file_name)

zip_file = zip_dir(file_path, file_name, dump_path)
print('Your file is saved as %s' %(file_name))
print('Your file is saved in %s' %(dump_path))





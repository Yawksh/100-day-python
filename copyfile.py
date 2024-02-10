
import shutil
import os
#copyfile()= copies content of a file
#copy()=copyfile() +permission mode + destination can a directory
#copy2() = copy() + copies metadata (file's creation  and modification times)
#shutil.copy("x.txt","C:\\Users\\HP\\Desktop\\yawk\\python dev\\abc.txt")#src,des
source="x.txt"
destination="abcd\\z.txt"
try:
    
    if os.path.exists(destination):
        
            os.replace(source, destination)
            print("there is already an file there")
    else:
        os.replace(source,destination)
except FileNotFoundError:
    
     print(source+" was not found sorrry")

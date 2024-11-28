z=open("zipper.zip","x")

# zip
import zipfile
with zipfile.ZipFile("zipper.zip","w") as z:
    z.write("Test2.py")
    z.write("achu.txt")
    
# unzip
import zipfile
with zipfile.ZipFile('zipper.zip','r') as z:
    z.extractall("zipster")
    list1=z.namelist()
    print(list1)


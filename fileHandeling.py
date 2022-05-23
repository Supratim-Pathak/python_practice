# reading file content
myfile = open('files_python/userdata.txt', mode='r')
content  = myfile.read()
myfile.close()
myfile2 = open('files_python/userdata1.txt', mode='w+')
myfile2.write(content)
myfile2.seek(0)
print(myfile2.read())
myfile2.close()



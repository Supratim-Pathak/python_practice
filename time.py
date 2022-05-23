from time import *

var = time()
varLoc = localtime()

print(ctime(var))
print(varLoc.tm_mon)

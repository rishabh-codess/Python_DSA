def square (n):
    for i in range(4):
        yield i**2

for i in square(4):
    print(i)

## read large file 
def read_large_file(file_path):
    with open (file_path, 'r') as file :
        for line in file:
            yield line 

file_path= 'large_file.txt'
for line in read_large_file(file_path):
    print (line.strip())
    

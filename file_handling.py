
f = open("wasteland.txt", mode='wt', encoding='utf-8')
f.write('What are you doing? I am learning pyton file handling')
f.write('\n you should know file handling')
f.write('\n Although not used much')
f.close()

#read the file now
f = open('wasteland.txt', mode='rt', encoding='utf-8')
print(f.read())

f.seek(0)
print(f.readline())
print(f.readline())
print(f.readline())

f.seek(0)
my_list = f.readlines()
print(my_list)

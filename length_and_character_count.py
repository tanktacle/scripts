import os

file = os.open("<path_to_file.txt>", os.O_RDWR)
passwords = os.read(file, 99999)
count = 0
char_counter = 0

for n in passwords.splitlines():
    big_list = n.decode("utf-8")
    
    if len(big_list) > 0:
        #if big_list[5] == 'r':
            print ('word: ', big_list + ' length: ', len(big_list))
            count = count + 1
            times_looped = 0
            
            for n in big_list:
                if n == 't' and times_looped == 0:
                    char_counter = char_counter + 1
                    print('word: ', big_list + ' letter: ', n)
                    times_looped = 1

print("Words in list: ", count)
print("Words with the character: ", char_counter)

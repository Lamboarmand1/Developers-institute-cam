#with open('/home/jane/Developers_institute/Week5/names_list.txt', 'r') as file:
    #Read the file line by line
    #for line in file.readlines():
    #    print(line)
    
    #Read only the 5th line of the file
    #print(file.readline(5))
    #Read only the 5th first characters of the file
    #print(file.read(3))
    #Read all the file and return it as a list of strings.
    #entire_file= file.read()
    #list_name = entire_file.split('\n')
    #print(list_name)
    #print(f'Darth apparait {list_name.count("Darth")} fois')
    #print(f'Luke apparait {list_name.count("Luke")} fois')
    #print(f'Lea apparait {list_name.count("Lea")} fois')


#with open('/home/jane/Developers_institute/Week5/names_list.txt', 'a') as file:
#    file.write('\nAlexandra')


with open('/home/jane/Developers_institute/Week5/names_list.txt', 'r+') as file1:
    name=' Skywalker'
    for line in file1.readlines():
        if 'Luke' in line:
            cur_pos = file1.tell()
            file1.seek(cur_pos)
            
            print(line)


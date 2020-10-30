from solution import File
file_obj_1 = File('file' + '_1')
file_obj_2 = File('file' + '_2')
file_obj_1.write('line 1\n')
file_obj_2.write('line 2\n')
new_file_obj = file_obj_1 + file_obj_2
print(new_file_obj)
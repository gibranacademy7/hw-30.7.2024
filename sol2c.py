import func_with_return_2c

list1 = [9, 8, 7];
list2 = [6, 5, 4, 3];
list3 = [2, 1];

res_con = func_with_return_2c.concat_list(list1, list2, list3);

print("Concatenated list:", res_con);
print("Length of the list:", len(res_con));

help(func_with_return_2c.concat_list);

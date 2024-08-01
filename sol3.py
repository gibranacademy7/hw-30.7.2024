from func_with_return_3 import bool_ann;

# Testing the function with individual calls
print(bool_ann(True));
print(bool_ann(False));

for value in [True, False]:
    print(bool_ann(value));

# Help documentation
help(bool_ann)

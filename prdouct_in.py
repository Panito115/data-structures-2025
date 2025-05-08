




def product_in_list(arr, key_prod):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] * arr[j] == key_prod:
                return True
    return False



test_n = 10000
test_arr = [2] * test_n
test_key_prod = 7
print(product_in_list(test_arr, test_key_prod))
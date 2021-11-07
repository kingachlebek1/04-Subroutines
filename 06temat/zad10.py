def compare(array1, array2):
    if len(array1) == len(array2):
        for index in range(len(array1)):
            if not array1[index] == array2[index]:
                return False
            return True
        else:
            return False

array1 = ["water","book","sky"]
array2 = ["water","book","sky"]

print(f"Array1: {array1}")

comparison = compare(array1, array2)
print(f"arrays are the same? {comparison}")
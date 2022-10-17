# Поиск общих элементов в двух списках


arr1 = ['p','y','t','h','o','n',' ','3','.','0']
arr2 = ['p','y','d','e','v',' ','2','.','0']

def interSection(arr1, arr2): 
   out = list(filter(lambda it: it in arr1, arr2))
   return out

if __name__ == "__main__":
    out = interSection(arr1, arr2)
    print("Отфильтрованный список:", out)
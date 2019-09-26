
array = [1,4,2,5,6,1]


for x in range(0, len(array)):
    aux = 0;
    for y in range(x+1, len(array)):
        if (array[x] >= array[y]):
            aux = array[y];
            array[y] = array[x];
            array[x] = aux;
print(array);
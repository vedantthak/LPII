numbers =[54,87,12,15,1]

def selection_sort():
    for i in range(len(numbers)):
        min_index = i
        for j in range(i+1,len(numbers)):
            if(numbers[min_index]>numbers[j]):
                min_index =j
        numbers[min_index],numbers[i]=numbers[i],numbers[min_index]
selection_sort()
print(numbers)
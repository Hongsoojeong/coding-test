array = [7,5,9,0,3,1,6,2,4,8]

def select_sort(array):
# 선택 정렬
# 특정한 리스트에서 가장 작은 데이터를 찾을 때 쓰일 수도
    for i in range(len(array)):
        min_idx = i # 가장 작은 인덱스
        for j in range(i+1, len(array)): 
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]


def insert_sort(array):
# 데이터가 거의 정렬되어 있을 때 효율적
# 특정한 데이터를 적절한 위치에 '삽입'한다
# 적절한 위치에 삽입 전, 그 앞 까지는 이미 정렬되어있다고 가정
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break


# 정렬 알고리즘 중에서 가장 많이 사용되는 알고리즘
# pivot 이 사용된다.
def quick_sort(array, start, end):

    if start >= end:
        return

    pivot = start # 피벗은 첫번째 원소
    
    left = start + 1
    right = end

    while left <= right:

        while left <= end and array[left] <= array[pivot]:
            left += 1

        while right > start and array[right] >= array[pivot]:
            right -= 1


        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

# quick_sort(array,0,len(array)-1)


# 특정한 조건이 부합할 때만 사용할 수 있다.
def count_sort(array):
    count = [0] * (max(array)+1)

    for i in range(len(array)):
        count[array[i]]+=1
    
    print(count)
    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')

count_sort(array)
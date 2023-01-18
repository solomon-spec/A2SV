def countingSort(arr):
    # Write your code here
    answer = [0]*100 
    for i in arr:
        answer[i] += 1
    return answer

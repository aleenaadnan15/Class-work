#Question num 4:

''' RUNNER UP SCORE '''

if __name__=="__main__":
    n = input()
    arr = map(int, n.split())
    arr = list(set(list(arr)))
    ar = len(arr)
    arr = sorted(arr)
    print(arr[ar-2])

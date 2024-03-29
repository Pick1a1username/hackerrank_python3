INF = 10**9 # a number larger than all ratings

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def candies(n, arr):
    # Write your code here
    # https://www.hackerrank.com/challenges/candies/editorial?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming

    # add sentinels
    arr = [INF] + arr + [INF]

    candies = [0]*(n+1)
    # populate 'valleys'
    for i in range(1,n+1):
        if arr[i-1] >= arr[i] <= arr[i+1]:
            candies[i] = 1
    save_candies(candies, 'after_valleys.txt')

    # populate 'rises'
    for i in range(1,n+1):
        if arr[i-1] < arr[i] <= arr[i+1]:
            candies[i] = candies[i-1] + 1
    save_candies(candies, 'after_rises.txt')

    # populate 'falls'
    for i in range(n,0,-1):
        if arr[i-1] >= arr[i] > arr[i+1]:
            candies[i] = candies[i+1] + 1
    save_candies(candies, 'after_falls.txt')

    # populate 'peaks'
    for i in range(1,n+1):
        if arr[i-1] < arr[i] > arr[i+1]:
            candies[i] = max(candies[i-1], candies[i+1]) + 1
    save_candies(candies, 'after_peaks.txt')

    return sum(candies)

def save_candies(cadies, save_path):
    with open(save_path, 'w') as f:
        f.write('\n'.join([str(x) for x in cadies]))
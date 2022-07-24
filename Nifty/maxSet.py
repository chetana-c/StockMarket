def maxCount(a,n):
    # Counting frequencies of elements
    freq = {}
    for i in range(n):
        if (a[i] in freq):
            freq[a[i]] += 1
        else:
            freq[a[i]] = 1

    # Finding max sum of adjacent indices
    ans = 0
    for key, value in freq.items():
        if (key + 1 in freq):
            ans = max(ans, freq[key] + freq[key + 1])

    return ans

if __name__ == '__main__':
    arr = [8,4,5,7,9,10,6]
    n = 7
    result = maxCount(arr,n)
    print(result)
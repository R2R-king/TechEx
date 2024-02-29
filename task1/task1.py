class Solution:
    def circle_array(n, m):

        if n < 1 or m < 1:
            print("numbers must be positive  ")
            return 0

        result = []
        n_array = []
        count = m
        index = 0
        array = [x for x in range(1, n +1)]

        while True:
            if count == 0:
                count = m
                index -= 1
                result.append(n_array[0])
                if n_array[-1] == 1:
                    break
                n_array = []
            n_array.append(array[index])
            count -= 1
            if index == n - 1:
                index = 0
            else:
                index += 1

        return "".join(map(str, result))

n = int(input())
m = int(input())

print(Solution.circle_array(n, m))


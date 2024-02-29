class Solution:

    def read(self, file1):
        try:
            with open(file1, 'r') as file:
                lines = file.readlines()
                arr = [int(line.strip()) for line in lines]
                return arr  # Возвращаем считанный массив

        except FileNotFoundError:
            print(f"Файл не найден {file1}")
            return None
        except ValueError:
            print(f"Ошибка при считывании значений из файла {file1}")
            return None

    def minMoves2(self, array):
        if len(array) < 2:
            return 0
        result = 0
        array.sort()
        middle = len(array)//2

        for elem in array:
            result += abs(elem - array[middle])
        return result

a = Solution()

file_data = a.read("numbers.txt")
if file_data is not None:
    print(a.minMoves2(file_data))
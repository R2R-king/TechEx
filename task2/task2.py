class Solution:

    def read(file1, file2):
        try:
            with open(file1, 'r') as file:
                r_x, r_y = map(float, file.readline().split())
                r = float(file.readline())
                if r < 0:
                    print(f"Radius must be positive, given r = {r}")
                    return 0

        except FileNotFoundError:
            print(f"Файл не найден {file1}")
            return 0
        except ValueError:
            print(f"Ошибка при считывании значений из файла {file1}")
            return 0

        try:
            with open(file2, 'r') as file:
                points = []

                for line in file:
                    x, y = map(float, line.split())
                    points.append((x, y))
        except FileNotFoundError:
            print(f"Файл не найден {file2}")
            return 0
        except ValueError:
            print(f"Ошибка при считывании значений из файла {file2}")
            return 0
        return r_x, r_y, r, points

    def calc_pos(x, y, r, r_x, r_y):
        res = (x - r_x) ** 2 + (y - r_y) ** 2
        if res == r ** 2:
            print(0)
        elif res > r ** 2:
            print(2)
        else:
            print(1)


input_data = Solution.read("circle.txt", "dot.txt")

if input_data:
    r_x, r_y, r, points = input_data

    for point in points:
        x, y = point
        Solution.calc_pos(x, y, r, r_x, r_y)

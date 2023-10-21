grades_count = int(input().strip())

grades = []

for _ in range(grades_count):

    grades_item = int(input().strip())
    grades.append(grades_item)


def round(n):
    r_v = (abs(n//5)+1)*5
    #print(r_v)
    if abs(r_v-n)<3:
        return r_v
    else:
        return n 




for i in range(grades_count):

    print(round(grades[i]))



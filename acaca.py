


def is_pal(s):

    reverse = s[::-1]
    rev = reverse

    # проверяем, совпадают ли строки
    if (s == rev):
        return True
    else:
        return False


b = str(input())
print(is_pal(b))
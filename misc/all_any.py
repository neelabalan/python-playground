if __name__ == '__main__':
    num = int(input())
    lst = list(map(int, input().strip().split()))
    lst_str = list(map(str, lst))
    # all postive and any palindromic 
    if all([x>=0 for x in lst]):
        print(
            any(
                list(
                    map(lambda x: x==x[::-1], lst_str)
                )
            )
        )
    else:
        print(False)
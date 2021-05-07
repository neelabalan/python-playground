input_lst = [
    [10,  2,   5],
    [7,   1,   0],
    [9,   9,   9],
    [1,   23,  12],
    [6,   5,   9]
]

index = 1

if __name__ == '__main__':
    # not really using m here
    n, m = input().strip().split()
    athelete_list = list()
    for _ in range(int(n)):
        athelete_list.append(
            list(
                map(int, input().strip().split())
            )
        )
    index = int(input())
        
    athelete_list.sort(key=lambda x: x[index])
    for ath in athelete_list:
        print(
            ' '.join(
                list(map(str, ath))
            )
        )
    
'''
input

10 2 5
7 1 0
9 9 9
1 23 12
6 5 9


output

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
'''
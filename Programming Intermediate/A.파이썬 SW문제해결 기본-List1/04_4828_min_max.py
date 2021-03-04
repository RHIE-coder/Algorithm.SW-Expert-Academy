# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

# [입력]
# 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
# 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
# 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai ≤ 1000000 )

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

with open('./04_4828_output.txt', 'r') as f:
    print(f.readlines())

with open('./04_4828_input.txt', 'r') as f:
    T = int(f.readline())
    for test_case in range(1, T + 1):
        # N = int(input())
        N = int(f.readline())
        # data = list(map(int, input().split))
        data = list(map(int, f.readline().split()))

        for i in range(N):
            for k in range(i+1, N):
                if data[i] > data[k]:
                    data[i], data[k] = data[k], data[i]
        result = data[-1] - data[0]
        print(f"#{test_case} {result}".format(test_case, result))

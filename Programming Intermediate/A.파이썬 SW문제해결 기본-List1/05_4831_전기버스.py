# A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
# 충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
# 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.

# [입력]
# 첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )

# [출력]
# #과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.

output_file_name = '05_4831_output.txt'
input_file_name = '05_4831_input.txt'

with open(output_file_name, 'r') as f:
    print(f.readlines())

with open(input_file_name, 'r') as f:
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

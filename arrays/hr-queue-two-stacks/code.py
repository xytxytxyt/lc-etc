# https://www.hackerrank.com/challenges/queue-using-two-stacks/problem

spush = []
spop = []


def shift():
    if len(spop) == 0:
        while spush:
            spop.append(spush.pop())


if __name__ == '__main__':
    n_queries = int(input())
    while True:
        # print('currently: ', spush, spop)
        try:
            query = input()
        except EOFError:
            break

        if query[0] == '1':  # enqueue
            query_type, v = query.split()
            spush.append(v)
        elif query[0] == '2':  # dequeue
            shift()
            spop.pop()
        elif query[0] == '3':  # peek
            shift()
            print(spop[-1])

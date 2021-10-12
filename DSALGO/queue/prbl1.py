# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
class StackQueue:
    def __init__(self):
        self.stack = []
        self.__queue = []

    def push(self, x):
        self.stack.append(x)
        self.__queue.append(self.stack.pop())

    def pop(self):
        if not self.is_empty():
            return self.__queue.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.__queue[0]
        else:
            return None

    def is_empty(self):
        return True if self.stack_size() == 0 else False

    def stack_size(self):
        return len(self.__queue)


q = int(input())
st = StackQueue()

while q > 0:
    ip = input().split(" ")
    if int(ip[0]) == 1:
        st.push(int(ip[1]))
    elif int(ip[0]) == 2:
        st.pop()
    else:
        print(st.peek())
    q -= 1

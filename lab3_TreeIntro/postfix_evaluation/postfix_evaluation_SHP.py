'''<Lab 5-1: Postfix Evaluation>
Read a postfix expression from the given input file, and evaluate the value of the postfix expression using stack ADT.
1. Input
Obtain a postfix expression from the given input file (expr_input.txt). The expression ends with #.
A detailed specification of operators and operands is provided below.

- Available operators : +, -, *, /, and %
- Operands: single-digit numbers (1, 2, 3, 4, 5, 6, 7, 8, and 9)
- Conditions:
    - The expression shouldbe no more than 100 characters.
    - The delimiter for the end of the expression is '#'.
    - No exception handling is required for checking whether the input file exists. '''

class ArrayStack:
    def __init__(self, max_size=100):
        self.data = []
        self.max = max_size-1

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def isFullStack(self):
        if self.peek == self.max:
            return True
        else:
            return False

    def pop(self):                                  # 맨 위에 있는 데이터 제거
        try:
            return self.data.pop()
        except IndexError:
            print("Index Error!")
            exit(0)

    def peek(self):                                 # 스택 맨 위에 있는 데이터를 반환
        try:
            return self.data[-1]
        except IndexError:
            print("Index Error!!")
            exit(0)

    def push(self, item):                           # 매개변수로 넘어온 data를 스택에 추가
        self.data.append(item)


def read_file(file):
    f = open(file, 'r', encoding='UTF-8')
    content = f.readlines()
    return content


def splitTokens(exprStr):
    tokens = []


    for c in exprStr:
        tokens.append(str(c))

    return tokens


def post_Cal(postfix):
    valStack = ArrayStack()

    prec = {
        '(': 3, '*': 2, '/': 2, '%': 2, '+': 1, '-': 1
    }
    for token in postfix:
        if token in prec:                                   # 연산자일 경우
            num1 = valStack.pop()                                  # 스택에 쌓여 있던 두 피연산자(숫자)를 꺼내
            num2 = valStack.pop()
            if token == '+':                                    # 덧셈(+)
                valStack.push(int(num2 + num1))
            elif token == '-':                                  # 뺄셈(-)
                valStack.push(int(num2 - num1))
            elif token == '/':                                  # 나눗셈(/)
                valStack.push(int(num2 / num1))
            elif token == '*':                                  # 곱셈(*)
                valStack.push(int(num2 * num1))                         # 두 피연산자에 대해 각 연산자에 해당하는 연산을 수행한 값을 스택에 push해준다
            elif token == '%':
                valStack.push(int(num2 % num1))                     # 나머지(%)

        elif token == '#':
            break

        else:                                               # 숫자일 경우
            valStack.push(int(token))                                # 해당 숫자를 int형으로 스택에 push

    return valStack.pop()                                          # 계산된 값을 반환한다


if __name__ == "__main__":
    file = 'expr_input.txt'
    documents = read_file(file)
    data = documents[0]

    tokens = splitTokens(data)
    postfix_token = tokens[:-1]
    postfix = ''.join(postfix_token)

    print(f"converted postfix form : {postfix}")
    result = post_Cal(tokens)
    print(f"evaluation result : {result}")


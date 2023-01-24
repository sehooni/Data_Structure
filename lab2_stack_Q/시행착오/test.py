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
    val = 0
    valProcessing = False

    for c in exprStr:
        if c == '':
            continue  # 그냥 넘어감

        # 숫자일 때
        if c in '0123456789':
            val = str(c)
            valProcessing = True

        # 연산자일 때
        else:
            if valProcessing:
                tokens.append(val)
                val = 0

            valProcessing = False                   # 십진수를 처리하고있지 않았음을 나타냄
            tokens.append(c)

    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):                      # 중위표현식을 후위표현식으로 바꾸는 함수
    prec = {
        '(': 3, '*': 2, '/': 2, '%': 2, '+': 1, '-': 1
    }
    oper = ['(', ')', '+', '-', '*', '/', '%', '#']
    openStack = ArrayStack()
    postfixList = []  # 리스트로 만들어서 함수를 리턴

    for token in tokenList:

        # 1. 피연산자일 때
        if token not in oper:
            token = int(token)
            postfixList.append(str(token))

        # 2. 열린 괄호 일 때
        elif token == '(':
            openStack.push(token)

        # 3. 닫힌 괄호 일 때
        elif token == ')':
            while not openStack.peek() == '(':
                postfixList.append(openStack.pop())
            openStack.pop()

        # 4. # 일 때
        elif token == '#':
            while not openStack.isEmpty():
                postfixList.append(openStack.pop())

        # 5. 연산자일 때
        else:
            while not openStack.isEmpty():
                if openStack.peek() == '(':
                    break
                elif prec[openStack.peek()] < prec[token]:
                    break
                postfixList.append(openStack.pop())

            openStack.push(token)

    while not openStack.isEmpty():
        postfixList.append(openStack.pop())

    return postfixList


if __name__ == "__main__":
    file = '../expr_input.txt'
    documents = read_file(file)
    data = documents[0]

    tokens = splitTokens(data)
    infix_token = tokens[:-1]
    infix = ''.join(infix_token)

    print(f"original infix form : {infix}")
    postfix_token = infixToPostfix(tokens)
    postfix = ''.join(postfix_token)
    print(f"converted postfix form : {postfix}")
class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty!")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0


# 사용자가 입력한 수식에서 피연산자를 인식하기 위한 함수
def recognize_Operands(infix):
    numbers = list('0123456789')                       # 실수 계산기 이므로, 모든 피연산자는 0~9인 정수와 .으로 이루어진다
    recognized = []                                      # 수식의 숫자들을 피연산자로 인식하여 다시 담아 줄 리스트

    i = 0
    while i < len(infix):
        j = 1
        if infix[i] in numbers:                         # 연산자가 아닐 경우, 즉 숫자 또는 .일 경우
            while i + j < len(infix):                   # 해당 요소의 다음 요소도 숫자 또는 .인지를 판별하고
                if infix[i + j] in numbers:
                    j += 1
                else:
                    break
            recognized.append(''.join(infix[i:i + j]))   # 이들을 하나로, 즉 하나의 숫자로 인식 할 수 있도록 묶어준다
            i += j
        else:                                           # 연산자일 경우엔 리스트에 바로 추가해준다
            recognized.append(infix[i])
            i += 1
    return recognized

priority = {'(': 3, ')': 3, '+': 1, '-': 1, '*': 2, '/': 2, '%' : 2}   # 연사자의 우선 순위(숫자가 클수록 더 높은 우선 순위)


# 중위 표기법 수식을 후위 표기법으로 바꿔주는 함수
def in2post(infix):
    s = Stack()                                             # 스택 생성
    postfix = []                                            # 후위 표기법으로 바뀐 수식을 담아 줄 리스트
    for i in infix:
        if i == '(':                                        # 여는 괄호('(')일 경우 스택에 바로 push
            s.push(i)
        elif i == ')':                                      # 닫는 괄호(')')일 경우
            while s.top() != '(':                           # '('와 ')'사이의 연산자들을 모두 postfix 리스트에 추가
                postfix.append(s.pop())
            s.pop()                                         # 그리고 stack에 들어있던 '('는 삭제. (후위 표기법은 괄호를 표시하지 않으므로)
        elif i in priority:                                 # '+ - * /'일 경우
            while not s.isEmpty():                          # 스택이 비어 있지 않을 때
                if priority[s.top()] >= priority[i]:        # 스택의 top에 해당하는 연산자의 우선순위가 비교할 연산자의 우선순위보다 크거나 같을 경우
                    postfix.append(s.pop())                 # 해당 연산자(top)를 postfix 리스트에 추가한다
                else:
                    break
            s.push(i)                                       # 스택이 비어있을 경우엔 해당 연산자를 스택에 바로 push
        else:                                               # 피연산자(숫자)의 경우 리스트에 바로 추가
           postfix.append(i)
    while not s.isEmpty():                                  # '('보다 밑 스택에 남아있던 연산자들을
        postfix.append(s.pop())                             # 모두 리스트에 추가해준다

    return postfix                                          # 변환된 후위 표기식을 반환한다


def read_file(file):
    f = open(file, 'r', encoding='UTF-8')
    content = f.readlines()
    return content

if __name__ == "__main__":
    file = '../expr_input.txt'
    documents = read_file(file)
    data = documents[0]

    infix = recognize_Operands(data)  # 오류가 없을 경우 수식의 연산자를 인식하여 정리한다
    postfix = in2post(infix)
    print(postfix)

if __name__=='__main__':
    # 실행시킨 파일의 명령 확인
    f = open(r'../lab3_input.txt', 'r', encoding='UTF-8')
    content = f.readlines()
    for e, line in enumerate(content):
        line = line.strip('')  # 줄 끝의 줄 바꿈 문자를 제거한다.
        # line = line.split()
        if line[0] == 'i':
            number = line[1][:6]
            print(number)
        print(line)

        # print(type(line))

    print(content)
    f.close()

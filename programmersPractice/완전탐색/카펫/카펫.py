# 노란색(yellow)를 구성하는 값이 되는 곱들 중에 가로가 세로보다 더 길어지는 순간 break

def solution(brown, yellow):

    # 가로
    width = 1

    # 세로
    length = 1

    while width <= yellow:
        if yellow % width == 0:
            length = yellow // width
        
        # brown 개수 = 전체 개수 - yellow 개수
        # width와 length가 곱해지면 yellow 크기여야 함
        # 만약 가로 길이가 세로 길이를 넘어서면 break
        if brown == (width+2)*(length+2)-yellow and width * length == yellow and width >= length:
            break

        width += 1

    # 가로 길이에서 +2, 세로 길이에서 +2한 결과가 정답
    result = [width+2, length+2]

    return result
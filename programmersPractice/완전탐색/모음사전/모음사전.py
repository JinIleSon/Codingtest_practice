# 모든 값을 순회해야 하니 DFS 사용

def solution(word):
    count = 0
    # 단어들 모음은 순서가 있으니 set 말고 리스트로
    visited = []
    vowel = ['A', 'E', 'I', 'O', 'U']
    find = False

    def dfs(v, visited):
        nonlocal count
        nonlocal word
        # 재귀든 아니든 nonlocal은 전체 공유
        nonlocal find
        visited.append(v)
        print(visited)
        # 해당 값을 append 했을 때 바로 같은지 확인해야 함
        if word == ''.join(visited):
            find = True
            return count
        # 값이 정해진 모음이기 때문에(AEIOU) 굳이 graph로 사용x
        if len(visited) < 5 and find == False:
            for node in vowel:
                # find가 True가 되어도 for문이 멈추지 않는 문제가 있어 내부 if문 넣기
                if find == True:
                    break
                # 모든 모음을 순회해야 하기 때문에 if node not in visited: 필요x
                count += 1
                # count로 굳이 받지 않아도 nonlocal이기 때문에(전역변수) count는 이어받는 중 
                dfs(node, visited)
                # 자식 노드 전부 탐색한 후(모두 끝나면 pop시켜서 depth 필요 x)
                visited.pop()
        return count
    
    # 시작점이 서로 다른 5개의 그래프가 있다고 생각하기
    # [A, E, I, O, U]의 서로 다른 시작점의 개수
    for node in vowel:
        if find:
            break
        count += 1
        # count가 nonlocal 변수라 +=이 아니라 =으로 계속 받아주면 됨
        dfs(node, visited)
        # 루트 노드도 pop시키기
        visited.pop()
    return count

"""
1. sorting & loop
"""
def solution(participant, completion):
    answer = ''

    # 1. 두 list를 sorting한다
    participant.sort()
    completion.sort()

    # 2. completeion list의 len만큼 participant를 찾아서 없는 사람을 찾는다
    for i in range(len(completion)):
        if(participant[i] != completion[i]):
            return participant[i]

    # 3. 전부 다 돌아도 없을 경우에는 마지막 주자가 완주하지 못한 선수이다.
    return participant[len(participant)-1]

# print(solution(["mimi", "gomi", "tokki"], ["gomi", "tokki"]))

"""
2. hash 활용
"""

def solution(participant, completion):
    hashDict = {}
    sumHash = 0
    # 1. part~list의 hash 구하고, hash값 더함
    for part in participant:
        # hash(part) -> key값, part -> value(실제 선수의 이름)
        hashDict[hash(part)] = part
        sumHash += hash(part)
        
    # 2. comp~list의 hash를 뺌
    for comp in completion:
        sumHash -= hash(comp)
        
    # 남은 값이 완주하지 못한 선수의 hash값이 됨
    return hashDict[sumHash]
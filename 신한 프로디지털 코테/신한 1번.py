"""
입력값: 
terms = [ "(required)this term need to be agreed", "(optional)this term is an option"],
agreement = ["disagree", "agree"]
출력값: 0

보험조항에서 required와 optional이 있는데 
required는 무조건 agree를 해야하기 때문에 disagree라 하면 해당 문항은 추후에 다시 동의를 받아야 한다. 
terms와 agreement가 다음과 같이 주어졌을때,
출력값으로 추후 다시 동의를 받아야하는 문항의 인덱스번호를 출력할 수 있도록 하는 
함수 check(terms, agreement)를 작성하라.

"""
def check(terms, agreement):
    disagree_indices = []
    for i in range(len(terms)):
        if 'required' in terms[i] and agreement[i] == 'disagree':
            disagree_indices.append(i)
    return disagree_indices if disagree_indices else -1

terms = ["(required)this term need to be agreed", "(optional)this term is an option", "(required)agree if you are an adult."]
agreement = ["disagree", "agree", "disagree"]
print(check(terms, agreement))  # 출력: [0, 2]


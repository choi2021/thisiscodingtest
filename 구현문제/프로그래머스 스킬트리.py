skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]


def solution(skill, skill_trees):
	count=0
	for sk in skill_trees:
		idx=0
		result=True
		for j in sk:
			if j in skill:
				index=skill.index(j)
				if idx==index:
					idx+=1
				else:
					result=False
					break
		if result:
			count+=1

	return count





solution(skill, skill_trees)

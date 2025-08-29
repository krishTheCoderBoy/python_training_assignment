
# This is the first code of list in python

scores = []
scores.extend([85, 90, 78, 92, 88])
print("After appending:", scores)

scores.insert(2, 80)
print(scores)

scores.remove(92)
print(scores)

scores.sort()
print(scores)

scores.reverse()
print(scores)

print("max:", max(scores))
print("min:", min(scores))
print(90 in scores)
print("total:", len(scores))
print("First three scores:", scores[:3])
print("last element:", scores[-1])

scores[2] = 95
print("after replacing:", scores)

copied = scores.copy()
print(copied)


# This is the seconde code of if else in python

score = scores[0]  
if score > 90:
    grade = 'A'
elif score > 80:
    grade = 'B'
elif score > 70:
    grade = 'C'
elif score > 60:
    grade = 'D'
else:
    grade = 'F'

print(score,"->",grade)

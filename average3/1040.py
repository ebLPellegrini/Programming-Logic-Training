import math

scores = input().split(" ")

score1, score2, score3, score4 = scores
score1 = float(score1)
score2 = float(score2)
score3 = float(score3)
score4 = float(score4)

average = ((score1 * 2) + (score2 * 3) + (score3 * 4) + score4) / 10

print('Average: %.1f' %(average))

if average >= 7.0 and average <= 10.0:
    print('Approved.')
elif average < 5.0:
    print('Reproved.')
elif average >= 5.0 and average < 7.0:
    print('In exam.')
    examScore = float(input('Exam score: '))
    
    average = (examScore + average) / 2
    
    if average >= 5.0:
        print('Approved.')
    elif average < 5.0:
        print('Reproved.')
        
    print('Final average: %.1f' %(average))
else:
    print('Scores not valid')
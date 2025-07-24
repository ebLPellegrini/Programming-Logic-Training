def main():
    team = {
    "1": "Rolien",
    "2": "Naej",
    "3": "Elehcim",
    "4": "Odranoel"
    }
    
    work_days = int(input())

    for i in range(work_days):
        total_feedbacks = int(input())
        for j in range(total_feedbacks):
            feedback = input()
            print(team[feedback])
            

main()
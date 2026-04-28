import random
# This is the event part or the random senaroios that can happen to twan it is seprated by two part
def trigger_academic_event(player):
    print("\n--- ACADEMIC EVENT ---")
    event_roll = random.randint(1, 4)

    if event_roll == 1:
        print("Pop Quiz!! Professor surprises you with a quiz.")
        print("1. Cheat (+5 Stress, +0.1 GPA, 15% catch chance)")
        print("2. Wing it (-5 Stress, GPA depends on readiness)")
        choice = input("Select choice (1/2): ")
        
        if choice == "1":
            if random.random() < 0.15:
                player.is_alive = False
                player.death_reason = "Caught cheating on a quiz! Game Over."
            else:
                player.update_stats(gpa_change=0.1, stress_change=5)
        else:
            gpa_impact = 0.1 if player.readiness > 50 else -0.1
            player.update_stats(gpa_change=gpa_impact, stress_change=-5)

    elif event_roll == 2:
        print("Group Project! Partners are doing nothing.")
        print("1. Do it all (+20 Stress)")
        print("2. Report them (+5 Stress, -10 Peer Respect)")
        choice = input("Select choice (1/2): ")
        
        if choice == "1":
            player.update_stats(stress_change=20)
        else:
            player.update_stats(stress_change=5, respect_change=-10)

    elif event_roll == 3:
        print("Essay due in 2 hours!")
        print("1. CHATGPT!! (-10 Stress, +0.05 GPA, 10% catch chance)")
        print("2. Do it yourself (+10 Stress, GPA boost)")
        choice = input("Select choice (1/2): ")
        
        if choice == "1":
            if random.random() < 0.10:
                player.is_alive = False
                player.death_reason = "Caught using AI. Plagiarism expulsion! Game Over."
            else:
                player.update_stats(gpa_change=0.05, stress_change=-10)
        else:
            player.update_stats(gpa_change=0.1, stress_change=10)
    elif event_roll == 4:
     print("Final Exam Season!")

def final_exam(player):
    print("\n--- FINAL EXAM WEEK ---")

    if player.readiness >= 80:
        print("Flow State: You are prepared! (+0.3 GPA)")
        player.update_stats(gpa_change=0.3, stress_change=10)

    elif player.readiness >= 40:
        print("Tried Best: You did okay (+0.1 GPA)")
        player.update_stats(gpa_change=0.1, stress_change=15)

    else:
        print("Brain Fog: You were unprepared (-0.5 GPA)")
        player.update_stats(gpa_change=-0.5, stress_change=25)



def trigger_social_event(player):
    print("\n--- SOCIAL & FINANCIAL EVENT ---")
    event_roll = random.randint(1, 4)

    if event_roll == 1:
        print("Party!!!!!!!! Your friends wanna go out.")
        print("1. Stay Home (+5 Stress)")
        print("2. Go Party (-20 Stress, -3 Readiness, 1% Arrest chance)")
        choice = input("Select choice (1/2): ")
        
        if choice == "2":
            if random.random() < 0.01:
                player.is_alive = False
                player.death_reason = "Arrested at the party! Game Over."
            else:
                player.update_stats(stress_change=-20, readiness_change=-3)
        else:
            player.update_stats(stress_change=5)

    elif event_roll == 2:
        print("Networking Event! Build connections.")
        print("1. Go!!! (+20 Respect, +5 Stress)")
        print("2. NO (-5 Stress)")
        choice = input("Select choice (1/2): ")
        
        if choice == "1":
            player.update_stats(respect_change=20, stress_change=5)
        else:
            player.update_stats(stress_change=-5)

    elif event_roll == 3:
        if player.peer_respect >= 40:
            print("Private Internship Event!")
            print("1. Go!!! (50% Chance of Internship, -30 Stress)")
            choice = input("Go? (y/n): ")
            if choice.lower() == 'y':
                if random.random() < 0.50:
                    player.has_internship = True
                    player.update_stats(stress_change=-30)
                    print("SUCCESS! You landed the internship!")
                else:
                    print("Denied. Better luck next time.")
        else:
            print("Club member wants you to join. (+5 Stress, +20 Respect)")
            player.update_stats(stress_change=5, respect_change=20)

    elif event_roll == 4:
        print("Laundry Day: Someone took your clothes!")
        print("1. Crash out (+20 Stress)")
        print("2. Ask friends (Requires 15 Respect, 50% success)")
        choice = input("Select choice (1/2): ")
        
        if choice == "2" and player.peer_respect >= 15:
            if random.random() < 0.5:
                print("Friends helped you find them!")
                player.update_stats(stress_change=-10)
            else:
                print("Friends couldn't help.")
                player.update_stats(stress_change=15)
        else:
            player.update_stats(stress_change=20) 
 # I need to work on the balance of the events and the stats changes to make it more fun and engaging. I also want to add more variety to the events and maybe some rare special events that can have big impacts on the player's stats. 
 #also need to make sure the events are not too punishing or too rewarding to keep the game balanced and enjoyable.
def vacuum_world():
    # initializing goal_state
    # 0 indicates Clean and 1 indicates Dirty
    goal_state = {'A': '0', 'B': '0'}
    cost = 0
    location_input = input("Enter Location of Vacuum: ")  # user_input of location vacuum is placed
    status_input = input("Enter status of " + location_input + ": ")  # user_input if location is dirty or clean
    status_input_complement = input("Enter status of other room: ")

    print("Initial Location Condition: " + str(goal_state))

    if location_input == 'A':
        # Location A is Dirty.
        print("Vacuum is placed in Location A")
        if status_input == '1':
            print("Location A is Dirty.")
            # suck the dirt and mark it as clean
            goal_state['A'] = '0'
            cost += 1  # cost for suck
            print("Cost for CLEANING A: " + str(cost))
            print("Location A has been Cleaned.")

            if status_input_complement == '1':
                # if B is Dirty
                print("Location B is Dirty.")
                print("Moving right to Location B.")
                cost += 1  # cost for moving right
                print("COST for moving RIGHT: " + str(cost))
                # suck the dirt and mark it as clean
                goal_state['B'] = '0'
                cost += 1  # cost for suck
                print("COST for SUCK: " + str(cost))
                print("Location B has been Cleaned.")
            else:
                print("Location B is already clean. No action.")
        else:
            print("Location A is already clean.")
            if status_input_complement == '1':  # if B is Dirty
                print("Location B is Dirty.")
                print("Moving right to Location B.")
                cost += 1  # cost for moving right
                print("COST for moving RIGHT: " + str(cost))
                # suck the dirt and mark it as clean
                goal_state['B'] = '0'
                cost += 1  # cost for suck
                print("Cost for SUCK: " + str(cost))
                print("Location B has been Cleaned.")
            else:
                print("Location B is already clean. No action.")

    else:
        print("Vacuum is placed in Location B")
        # Location B is Dirty.
        if status_input == '1':
            print("Location B is Dirty.")
            # suck the dirt and mark it as clean
            goal_state['B'] = '0'
            cost += 1  # cost for suck
            print("COST for CLEANING B: " + str(cost))
            print("Location B has been Cleaned.")

            if status_input_complement == '1':
                # if A is Dirty
                print("Location A is Dirty.")
                print("Moving left to Location A.")
                cost += 1  # cost for moving left
                print("COST for moving LEFT: " + str(cost))
                # suck the dirt and mark it as clean
                goal_state['A'] = '0'
                cost += 1  # cost for suck
                print("COST for SUCK: " + str(cost))
                print("Location A has been Cleaned.")
            else:
                print("Location A is already clean. No action.")
        else:
            print("Location B is already clean.")
            if status_input_complement == '1':  # if A is Dirty
                print("Location A is Dirty.")
                print("Moving left to Location A.")
                cost += 1  # cost for moving left
                print("COST for moving LEFT: " + str(cost))
                # suck the dirt and mark it as clean
                goal_state['A'] = '0'
                cost += 1  # cost for suck
                print("Cost for SUCK: " + str(cost))
                print("Location A has been Cleaned.")
            else:
                print("Location A is already clean. No action.")

    # done cleaning
    print("GOAL STATE: ")
    print(goal_state)
    print("Performance Measurement: " + str(cost))

# Call the function
vacuum_world()

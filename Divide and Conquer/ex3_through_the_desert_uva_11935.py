if __name__ == "__main__":
    
    distance_per_litre = 100.0

    while True:
        tank, max_tank, current_position, last_position, distance, leak, consummation = 0, 0, 0, 0, 0, 0, 0
        goal = False
        
        sample_input = input().split()

        if sample_input[1] == 'Fuel':
            if sample_input[3] == '0':
                break

        current_position = int(sample_input[0])
        consummation = int(sample_input[3])         
        last_position = current_position

        while True:
            sample_input = input().split()
            current_position = int(sample_input[0])  

            distance = current_position - last_position
            last_position = current_position

            tank += (distance / distance_per_litre) * consummation + distance * leak
            max_tank = max(max_tank, tank)

            if sample_input[1] == 'Fuel':
                consummation = int(sample_input[3])
            elif sample_input[1] == 'Leak':
                leak += 1
            elif sample_input[1] == 'Gas':
                tank = 0
            elif sample_input[1] == 'Mechanic':
                leak = 0
            elif sample_input[1] == 'Goal':
                break # Get out of the loop
        
        print('{:.3f}'.format(max_tank))
    
if __name__ == "__main__":

    while True:
        sample_input = []

        while not sample_input:
            sample_input = input().split()

        n_of_campsites, n_of_days = int(sample_input[0]) + 1, int(sample_input[1])
        campsites = [0] * n_of_campsites

        for index in range(n_of_campsites): 
            campsites[index] = int(input())

        min_dist, max_dist = 0, sum(campsites)
        final_dist = max_dist

        while True:
            mid_dist = (max_dist + min_dist) // 2
            index, walking, max_walking_distance, walking_days = 0, 0, 0, 0
            #print('(Min, Max) - ({}, {})'.format(min_dist, max_dist))

            while index != n_of_campsites:
                walking += campsites[index]
                if walking <= mid_dist:
                    max_walking_distance = max(max_walking_distance, walking)
                    index += 1
                else:
                    if index == 0 or walking_days > n_of_days + 1:
                        break
                    walking = 0
                    walking_days += 1

            if walking_days == 0: # In case the step is less than the current campsite
                min_dist = mid_dist + 1
            elif walking_days <= n_of_days:
                max_dist = mid_dist - 1
            else:
                min_dist = mid_dist + 1

            if max_walking_distance != 0 and walking_days <= n_of_days:
                final_dist = min(max_walking_distance, final_dist)
            
            #print('Days - {} of {} possible'.format(walking_days, n_of_days))
            #print('Current max {}'.format(max_walking_distance))

            if max_dist < min_dist:
                break

        print(final_dist)

    
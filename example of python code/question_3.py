def getPasserRating(filename):
    '''takes in the name of a file containing data on NFL players, returns
       a dictionary of the players names with their passer ratings.
       lines with # are ignored, file must be in specific format of:
       player name, attempts, completions, yards, Touch Downs, interceptions

    Args:
        filename (str): name of file to be opened and data to be read from

    Raises:
        ValueError: file does not follow format specified
        KeyError: file contains more than one data set for a player

    Returns:
        player_dict (dict): dictionary of players against passer ratings
    '''
    file_pointer = open(filename, "r")
    player_dict = {}
    for line in file_pointer:
        # for every line in file that does not start with #, split into list
        if line[0] != "#":
            line_data = line.split(",")
            # check line is valid and convert numbers to floats
            if len(line_data) != 6:
                raise ValueError("file is not in the correct format")
            if line_data[0] in player_dict.keys():
                raise KeyError("the name for two sets of data is the same")
            for num in range(1, 6):
                line_data[num] = float(line_data[num])
            # complete and scale values to calculate passer_rating
            completion_percent = ((line_data[2]/line_data[1])-0.3)*5
            if completion_percent > 2.375:
                completion_percent = 2.375
            if completion_percent < 0:
                completion_percent = 0

            yards_per_attempt = ((line_data[3]/line_data[1])-3)*0.25
            if yards_per_attempt > 2.375:
                yards_per_attempt = 2.375
            if yards_per_attempt < 0:
                yards_per_attempt = 0

            touchdowns_per_attempt = (line_data[4]/line_data[1])*20
            if touchdowns_per_attempt > 2.375:
                touchdowns_per_attempt = 2.375
            if touchdowns_per_attempt < 0:
                touchdowns_per_attempt = 0

            interceptions_per_attempt = (2.375 -
                                         (line_data[5]/line_data[1])*25)
            if interceptions_per_attempt > 2.375:
                interceptions_per_attempt = 2.375
            if interceptions_per_attempt < 0:
                interceptions_per_attempt = 0
            # use formula to calculate passer_rating and add to dictionary
            passer_rating = ((completion_percent +
                              yards_per_attempt +
                              touchdowns_per_attempt +
                              interceptions_per_attempt)/6)*100
            player_dict[line_data[0]] = round(passer_rating, 1)
    return player_dict

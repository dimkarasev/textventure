def draw (green, max, unlock_difficulty):
    print (str("■" * green + "□" * (max - green) + "(" + str(green) + "/" + str(unlock_difficulty) + ")"))
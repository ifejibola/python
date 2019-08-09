def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")


def get_scores():
    # score_total = 0
    # counter = 0

    scores = []
    while True:
        score = input("Enter test score: ")
        if score == "x":
            # return  score_total, counter
            return scores
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                # score_total += score
                # counter += 1
                scores.append(score)
            else:
                print(
                    "Test score must be from 0 through 100. "
                    + "Score discarded. Try again."
                )


def process_scores(score_list):
    # def process_scores(score_total, count):

    # calculate average score
    total = 0
    numberOfScores = len(score_list)
    # total scores in the list, len() to get number of scores in the list, get avg by dividing totalscores by len
    for score in score_list:
        total += score
    average = round(total / len(score_list))

    # get min and max
    low_score = min(score_list)
    high_score = max(score_list)

    # get median
    median_index = len(score_list) // 2
    if len(score_list) % 2 == 1: #odd
        median_score = score_list[median_index]
    else:   # even
        middle1 = score_list[median_index]
        middle2 = score_list[median_index-1]
        median_score = (middle1 + middle2)/2

    # format and display the result
    print()
    print("Score total:       ", total)
    print("Number of Scores:  ", len(score_list))
    print("Average Score:     ", average)
    print("Low Score: ", low_score)
    print("High Score: ", high_score)
    print("Median: ", median_score)


def main():
    display_welcome()
    # score_total, count = get_scores()
    # process_scores(score_total, count)

    score_list = get_scores()
    process_scores(score_list)
    print("")
    print("Bye!")


# if started as the main module, call the main function
if __name__ == "__main__":
    main()


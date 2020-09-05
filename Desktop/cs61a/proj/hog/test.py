from random import randint
GOAL_SCORE = 100
def make_fair_dice(sides):
    """Return a die that returns 1 to SIDES with equal chance."""
    assert type(sides) == int and sides >= 1, 'Illegal value for sides'
    def dice():
        return randint(1,sides)
    return dice

def silence(score0, score1):
    """Announce nothing (see Phase 2)."""
    return silence

four_sided = make_fair_dice(4)
six_sided = make_fair_dice(6)

def make_test_dice(*outcomes):

    assert len(outcomes) > 0, 'You must supply outcomes to make_test_dice'
    for o in outcomes:
        assert type(o) == int and o >= 1, 'Outcome is not a positive integer'
    index = len(outcomes) - 1
    def dice():
        nonlocal index
        index = (index + 1) % len(outcomes)
        return outcomes[index]

def always_roll(n):

    def strategy(score, opponent_score):
        return n
    return strategy

def other(player):
    return 1 - player

def is_swap(player_score, opponent_score):
    """
    Return whether the two scores should be swapped
    """
    # BEGIN PROBLEM 4
    #create vars to hold digits
    player_left_digit, oppon_left_digit, player_right_digit, oppon_right_digit = 0,0,0,0
    #calculate right score first before calculate left
    if player_score >= 10:
        player_right_digit = player_score % 10
    else:
        player_left_digit = player_score
        player_right_digit = player_score
    if opponent_score >= 10:
        oppon_right_digit = opponent_score % 10
    else:
        oppon_left_digit = opponent_score
        oppon_right_digit = opponent_score
    while player_score >= 10:
        player_left_digit = player_score // 10
        player_score = player_score //10
    while opponent_score >= 10:
        oppon_left_digit = opponent_score // 10
        opponent_score = opponent_score //10
    if (player_left_digit *player_right_digit) == (oppon_left_digit * oppon_right_digit):
        return True
    else:
        return False

def take_turn(num_rolls, opponent_score, dice=six_sided):

    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 3
    #if player dont roll dice
    if num_rolls == 0:
        #input opponent_score to calculate players free bacon score
        return free_bacon(opponent_score)
    #other player rolls a dice
    else:
        #input num of rolls and dice type
        return roll_dice(num_rolls, dice)
    # END PROBLEM 3

def free_bacon(score):

    assert score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    #when score  is smaller than 10
    if score < 10:
            #not need to fill zero, just give it ten
        score = 10
        return score
    else:
            #convert int to string
        score = str(score)
            #substring str to compare min value#
        score = 10 - min(int(score[0]), int(score[1]))
        return score

def roll_dice(num_rolls, dice=six_sided):

    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    #instantiate num_of_one, n turn, sum and curr_outcome
    one = 0
    n, score = 0, 0
    curr = 0
    # run loop if num_rolls is larger than 0
    while num_rolls > n:
        curr = dice()
        if curr == 1:
            one = one + 1
        score = score + curr
        n = n + 1
    if one > 0:
        return 1
    else:
        return score



def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence, feral_hogs=True):

    player = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    while score0 < goal and score1 < goal:
        if player == 0:
            score0 = score0 + take_turn(strategy0(score0,score1), score1, dice)
            if is_swap(score0, score1):
                score0, score1 = score1, score0
        else:
            score1 = score1 + take_turn(strategy1(score1, score0), score0, dice)
            if is_swap(score0, score1):
                score0, score1 = score1, score0

        #say = say(score0, score1)
        player = other(player)
    return score0, score1



always_one = make_test_dice(1)

s0, s1 = play(lambda score, other: (score + 3) // 4 * 2 + 3, lambda score, other: 4 - other // 4 * 2, score0=0, score1=0, goal=10, dice=always_one)

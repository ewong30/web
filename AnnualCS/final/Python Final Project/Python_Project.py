import random
import matplotlib.pyplot as plt
import numpy as np

#Reading in data file for round 6:
rps_file = open('rpsdataset.txt', encoding="utf8")
text = rps_file.read()

#Round 0: The setup
roundd = 0
#Roundd will keep track of our stages, which will be how we're going to navigate what we're doing at each turn

wins = 0
losses = 0
ties = 0

rocks = 0
rockwins = 0
rocklosses = 0
rockties = 0

papers = 0
paperwins = 0
paperlosses = 0
paperties = 0

scissors = 0
scissorwins = 0
scissorlosses = 0
scissorties = 0
#The counters for data later on

last = None
#How we'll be using the markov dictionary later on

last_result = None

if roundd == 0:
    print('Welcome to (a slightly smarter) game of Rock Paper Scissors!')
    name = input("To get started, what's your name?\n ")
    starting = input('Hello ' + name + '! Would you like to begin? y/n\n ')
    if starting == 'y':
        roundd += 1
    if starting == 'n':
        roundd = 7
    if ((starting != 'n') and (starting != 'y')):
        roundd = 8
    
#Round 1: The first move
#the rules/formal intro:
if roundd == 1:
    print("\nAlright! The rules of the game is simple:\nJust like every other game of rock paper scissors,\nyou will choose to play rock paper scissors against me,\nusing strings that you will input. After every round,\nyou will be able to choose to play again, end the game, or graph the statistics of the game!\n\nWith the rules of the game out of the way, let's play!")

    #Round counter:
    counter = 1
    print("\n======Round " + str(counter) + "======")

    #The First Round:
    
    #Player's choice:
    choice0 = input('Pick your play! Rock (rock or r), Paper (paper or p), or Scissors (scissors or s)\n ')

    #Computer's choice:
    #The following probabilities will be generated based on a random choice from this list,
    #with a total of 101 terms to represent the probabilities (37.7, 34.5, 27.8)
    #each of them are rounded to the nearest whole number
    round1choices = []
    for i in range(38):
        round1choices.append('paper')
    for i in range(35):
        round1choices.append('scissors')
    for i in range(28):
        round1choices.append('rock')
    
    mychoice0 = random.choice(round1choices)
    
    #Rule conditions
    viable_rock = ['rock', 'Rock', 'r', 'R']
    viable_paper = ['paper', 'Paper', 'p', 'P']
    viable_scissors = ['scissors', 'Scissors', 's', 'S']
    if choice0 in viable_rock:
        if mychoice0 == 'scissors':
            wins += 1
            rocks += 1
            rockwins += 1
            counter += 1
            last_result = 'win'
            last = 'rock'
            roundd += 1
            print('\nYou chose: Rock\nI chose: Scissors\nYou win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if mychoice0 == 'rock':
            ties += 1
            rocks += 1
            rockties += 1
            counter += 1
            last_result = 'tie'
            last = 'rock'
            roundd += 1
            print('\nYou chose: Rock\nI chose: Rock\nWe have tied.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if mychoice0 == 'paper':
            losses += 1
            rocks += 1
            rocklosses += 1
            counter += 1
            last_result = 'loss'
            last = 'rock'
            roundd += 1
            print('\nYou chose: Rock\nI chose: Paper\nI win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
    if choice0 in viable_paper:
        if mychoice0 == 'rock':
            wins += 1
            papers += 1
            paperwins += 1
            counter += 1
            last_result = 'win'
            last = 'paper'
            roundd += 1
            print('\nYou chose: Paper\nI chose: Rock\nYou win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if mychoice0 == 'paper':
            ties += 1
            papers += 1
            paperties += 1
            counter += 1
            last_result = 'tie'
            last = 'paper'
            roundd += 1
            print('\nYou chose: Paper\nI chose: Paper\nWe have tied.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if mychoice0 == 'scissors':
            losses += 1
            papers += 1
            paperlosses += 1
            counter += 1
            last_result = 'loss'
            last = 'paper'
            roundd += 1
            print('\nYou chose: Paper\nI chose: Scissors\nI win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
    if choice0 in viable_scissors:
        if mychoice0 == 'paper':
            wins += 1
            scissors += 1
            scissorwins += 1
            counter += 1
            last_result = 'win'
            last = 'scissors'
            roundd += 1
            print('\nYou chose: Scissors\nI chose: Paper\nYou win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if mychoice0 == 'scissors':
            ties += 1
            scissors += 1
            scissorties += 1
            counter += 1
            last_result = 'tie'
            last = 'scissors'
            roundd += 1
            print('\nYou chose: Scissors\nI chose: Scissors\nWe have tied.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if mychoice0 == 'rock':
            losses += 1
            scissors += 1
            scissorlosses += 1
            counter += 1
            last_result = 'loss'
            last = 'scissors'
            roundd += 1
            print('\nYou chose: Scissors\nI chose: Rock\nI win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
    if (((choice0 not in viable_rock) and (choice0 not in viable_paper)) and (choice0 not in viable_scissors)):
        roundd = 8
    
    
#Round 2: Play again?
if roundd == 2:
    again = input('\nWould you like to start the second round? y/n\n ' )
    
    if again == 'y':
        roundd += 1
    if again == 'n':
        roundd = 7
    if ((again != 'y') and (again != 'n')):
        roundd = 8
    
    
    
#Building a markov dictionary:
#The two items that we will be using will be if the last game was a win/loss and the last played thing
#I'm going to semi-manually put in these values... because... there's no way to justify the amount of time this took.
#In the beginning, it will start out with the statistics and ideas set by the website:
#How To Win At Rock Paper Scissors (Using Data From 120,000 Games), linked in the project proposal
d = {}

#FOR TIES:
#Rock Ties:
d['rock tie'] = ['scissors']
for i in range(27):
    d['rock tie'] += ['scissors']
for i in range(35):
    d['rock tie'] += ['paper']
for i in range(37):
    d['rock tie'] += ['rock']
#Paper Ties:
d['paper tie'] = ['rock']
for i in range(29):
    d['paper tie'] += ['paper']
for i in range(36):
    d['paper tie'] += ['scissors']
for i in range(34):
    d['paper tie'] += ['rock']
#Scissor Ties:
d['scissors tie'] = ['scissors']
for i in range(27):
    d['scissors tie'] += ['scissors']
for i in range(37):
    d['scissors tie'] += ['paper']
for i in range(35):
    d['scissors tie'] += ['rock']
    
#FOR WINS:
#Rock wins:
d['rock win'] = ['paper']
for i in range(29):
    d['rock win'] += ['paper']
for i in range(37):
    d['rock win'] += ['scissors']
for i in range(33):
    d['rock win'] += ['rock']
#Paper wins:
d['paper win'] = ['paper']
for i in range(36):
    d['paper win'] += ['paper']
for i in range(29):
    d['paper win'] += ['scissors']
for i in range(34):
    d['paper win'] += ['rock']
#Scissors wins:
d['scissors win'] = ['paper']
for i in range(37):
    d['scissors win'] += ['paper']
for i in range(36):
    d['scissors win'] += ['scissors']
for i in range(26):
    d['scissors win'] += ['rock']

#FOR LOSSES:
#Rock losses:
d['rock loss'] = ['paper']
for i in range(36):
    d['rock loss'] += ['paper']
for i in range(32):
    d['rock loss'] += ['scissors']
for i in range(31):
    d['rock loss'] += ['rock']
#Paper losses:
d['paper loss'] = ['paper']
for i in range(32):
    d['paper loss'] += ['paper']
for i in range(33):
    d['paper loss'] += ['scissors']
for i in range(28):
    d['paper loss'] += ['rock']
#Scissor losses:
d['scissors loss'] = ['paper']
for i in range(33):
    d['scissors loss'] += ['paper']
for i in range(35):
    d['scissors loss'] += ['scissors']
for i in range(31):
    d['scissors loss'] += ['rock']

lastlast = last
lastlastresult = last_result
#lastlast & lastlastresult will be for keeping track of things later on.

#Round 3: Things get smarter
if roundd == 3:
    counter = 2
    print("\n======Round " + str(counter) + "======")
    #Making a marker to pull from our Markov Dictionary
    key = last + ' ' + last_result
    lastlast = last
    lastlastresult = last_result
    
    #Copying and pasting round 1, but adding in the markov dictionary
    choice1 = input('Pick your play! Rock (rock or r), Paper (paper or p), or Scissors (scissors or s)\n ')
    
    #Using the Markov Dictionary to make the computer's choice:
    mychoice1 = random.choice(d[key])
    
    #Adding (copy and pasting) in the rules:
    viable_rock = ['rock', 'Rock', 'r', 'R']
    viable_paper = ['paper', 'Paper', 'p', 'P']
    viable_scissors = ['scissors', 'Scissors', 's', 'S']
    if choice1 in viable_rock:
        if mychoice1 == 'scissors':
            wins += 1
            rocks += 1
            rockwins += 1
            counter += 1
            last_result = 'win'
            last = 'rock'
            roundd += 1
            print('\nYou chose: Rock\nI chose: Scissors\nYou win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if mychoice1 == 'rock':
            ties += 1
            rocks += 1
            rockties += 1
            counter += 1
            last_result = 'tie'
            last = 'rock'
            roundd += 1
            print('\nYou chose: Rock\nI chose: Rock\nWe have tied.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if mychoice1 == 'paper':
            losses += 1
            rocks += 1
            rocklosses += 1
            counter += 1
            last_result = 'loss'
            last = 'rock'
            roundd += 1
            print('\nYou chose: Rock\nI chose: Paper\nI win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
    if choice1 in viable_paper:
        if mychoice1 == 'rock':
            wins += 1
            papers += 1
            paperwins += 1
            counter += 1
            last_result = 'win'
            last = 'paper'
            roundd += 1
            print('\nYou chose: Paper\nI chose: Rock\nYou win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if mychoice1 == 'paper':
            ties += 1
            papers += 1
            paperties += 1
            counter += 1
            last_result = 'tie'
            last = 'paper'
            roundd += 1
            print('\nYou chose: Paper\nI chose: Paper\nWe have tied.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if mychoice1 == 'scissors':
            losses += 1
            papers += 1
            paperlosses += 1
            counter += 1
            last_result = 'loss'
            last = 'paper'
            roundd += 1
            print('\nYou chose: Paper\nI chose: Scissors\nI win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
    if choice1 in viable_scissors:
        if mychoice1 == 'paper':
            wins += 1
            scissors += 1
            scissorwins += 1
            counter += 1
            last_result = 'win'
            last = 'scissors'
            roundd += 1
            print('\nYou chose: Scissors\nI chose: Paper\nYou win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if mychoice1 == 'scissors':
            ties += 1
            scissors += 1
            scissorties += 1
            counter += 1
            last_result = 'tie'
            last = 'scissors'
            roundd += 1
            print('\nYou chose: Scissors\nI chose: Scissors\nWe have tied.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if mychoice1 == 'rock':
            losses += 1
            scissors += 1
            scissorlosses += 1
            counter += 1
            last_result = 'loss'
            last = 'scissors'
            roundd += 1
            print('\nYou chose: Scissors\nI chose: Rock\nI win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
    if (((choice1 not in viable_rock) and (choice1 not in viable_paper)) and (choice1 not in viable_scissors)):
        roundd = 8

#Round 4: The loop
#Since there's not much else to do, round 4 will just be a loop that goes as long as the player wants.

counter = 3

while roundd == 4:
    
    #Play Again? Graph? Stop?
    future = input('\nWould you like to start the next round? y(play again)/ n(stop the game)/ g(graph)\n ')
    
    stopp = ['no', 'No', 'n', 'N', 'stop the game', 'Stop the game']
    if future in stopp:
        roundd = 7
    
    graphh = ['graph', 'Graph', 'g', 'G']
    if future in graphh:
        roundd += 1
    
    
    againn = ['yes','Yes', 'y', 'Y', 'play again', 'Play again']
    
    if ((future not in stopp) and (future not in graphh)) and (future not in againn):
        roundd = 8
    
    if future in againn:
        print("\n======Round " + str(counter) + "======")
        
        #Making a marker to pull from our Markov Dictionary
        updatingkey = lastlast + ' ' + lastlastresult
        key = last + ' ' + last_result
        
        #Here, we'll be adding in a "learning" aspect to this game.
        
        #Edit from the last version: The model didn't really learn until someone player 10-20
        #games with the program. In response to this, I have changed the model to add in the item 15 items,
        #which will affect the probabilities closer by 13% every time, instead of the original 4% change.
        
        if last == 'rock':
            for i in range(15):
                d[updatingkey] += ['paper']
        if last == 'paper':
            for i in range(15):
                d[updatingkey] += ['scissors']
        if last == 'scissors':
            for i in range(15):
                d[updatingkey] += ['rock']
        
        #Copying and pasting round 1, but adding in the markov dictionary
        choice = input('Pick your play! Rock (rock or r), Paper (paper or p), or Scissors (scissors or s)\n ')
        
        #Using the Markov Dictionary to make the computer's choice:
        mychoice = random.choice(d[key])
        
        lastlast = last
        lastlastresult = last_result
        
        #Copying in the rules:
        viable_rock = ['rock', 'Rock', 'r', 'R']
        viable_paper = ['paper', 'Paper', 'p', 'P']
        viable_scissors = ['scissors', 'Scissors', 's', 'S']
        if choice in viable_rock:
            if mychoice == 'scissors':
                wins += 1
                rocks += 1
                rockwins += 1
                counter += 1
                last_result = 'win'
                last = 'rock'
                print('\nYou chose: Rock\nI chose: Scissors\nYou win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
            if mychoice == 'rock':
                ties += 1
                rocks += 1
                rockties += 1
                counter += 1
                last_result = 'tie'
                last = 'rock'
                print('\nYou chose: Rock\nI chose: Rock\nWe have tied.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
            if mychoice == 'paper':
                losses += 1
                rocks += 1
                rocklosses += 1
                counter += 1
                last_result = 'loss'
                last = 'rock'
                print('\nYou chose: Rock\nI chose: Paper\nI win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if choice in viable_paper:
            if mychoice == 'rock':
                wins += 1
                papers += 1
                paperwins += 1
                counter += 1
                last_result = 'win'
                last = 'paper'
                print('\nYou chose: Paper\nI chose: Rock\nYou win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
            if mychoice == 'paper':
                ties += 1
                papers += 1
                paperties += 1
                counter += 1
                last_result = 'tie'
                last = 'paper'
                print('\nYou chose: Paper\nI chose: Paper\nWe have tied.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
            if mychoice == 'scissors':
                losses += 1
                papers += 1
                paperlosses += 1
                counter += 1
                last_result = 'loss'
                last = 'paper'
                print('\nYou chose: Paper\nI chose: Scissors\nI win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if choice in viable_scissors:
            if mychoice == 'paper':
                wins += 1
                scissors += 1
                scissorwins += 1
                counter += 1
                last_result = 'win'
                last = 'scissors'
                print('\nYou chose: Scissors\nI chose: Paper\nYou win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
            if mychoice == 'scissors':
                ties += 1
                scissors += 1
                scissorties += 1
                counter += 1
                last_result = 'tie'
                last = 'scissors'
                print('\nYou chose: Scissors\nI chose: Scissors\nWe have tied.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
            if mychoice == 'rock':
                losses += 1
                scissors += 1
                scissorlosses += 1
                counter += 1
                last_result = 'loss'
                last = 'scissors'
                print('\nYou chose: Scissors\nI chose: Rock\nI win.\nScore: ' + name + ':' + str(wins) +'  computer:' + str(losses))
        if (((choice not in viable_rock) and (choice not in viable_paper)) and (choice not in viable_scissors)):
            roundd = 8

#Round 5: The graphing
if roundd == 5:
    
    ccounter = counter - 1
    #Adding this in, because the counter added one extra, but the round has not been played.
    
    #Edit from last version again: instead of counting by the actual numbers,
    #I changed it to account for percentages instead and scale out of 100%
    #To see the numbers of each stat, it will be printed as the graph is requested.
    
    #Prepping the data sets
    geninfo = ['Rock', 'Paper', 'Scissors']
    gendata = [(rocks / ccounter) * 100, (papers / ccounter) * 100, (scissors / ccounter) * 100]
    
    if rocks > 0:
        rockdata = [(rockwins / rocks) * 100, (rocklosses / rocks) * 100, (rockties / rocks) * 100]
    if rocks == 0:
        rockdata = [0, 0, 0]
    rockinfo = ['Wins', 'Losses', 'Ties']
    
        
    if papers > 0:
        paperdata = [(paperwins / papers) * 100, (paperlosses / papers) * 100, (paperties / papers) * 100]
    if papers == 0:
        paperdata = [0, 0, 0]
    paperinfo = ['Times won', 'Times lost', 'Times tied']
    
    
    if scissors > 0:
        scissorsdata = [(scissorwins / scissors) * 100, (scissorlosses / scissors) * 100, (scissorties / scissors) * 100]
    if scissors == 0:
        scissorsdata = [0, 0, 0]
    scissorsinfo = ['Times won', 'Times lost', 'Times tied']
    
    
    winsvlosses = ['Wins', 'Losses', 'Ties']
    winsvlossesdata = [(wins / ccounter) * 100, (losses / ccounter) * 100, (ties / ccounter) * 100]
    
    #Bar Graph Request
    request = input('\nWhat data do you want graphed?\n\n• Typing gen will return the percent value that you played rock, paper, or scissors\n• Typing rock, paper, or scissors will show your information on your wins, losses, and ties for each individual item\n• Finally, wvlvt gives you a ratio of your wins to losses to ties in a bar graph.\nMultiple inputs allowed as long as they are spaced apart.\n ')
    
    #Graphing the Requests
    print("\nThe data:")
    if 'gen' in request:
        plt.title('Percent of Each Choice Played')
        plt.ylabel('Frequency of each of your choices (%)')
        plt.xlabel('Type of Item (Rock, Paper, Scissors)')
        plt.bar(geninfo, gendata, width = 0.4)
        plt.ylim([0, 100])
        print("\nOf the " + str(ccounter) + " rounds played, you have played:\nRock " + str(rocks) + " time(s), Paper " + str(papers) + " time(s), and Scissors " + str(scissors) + " time(s).")
        plt.show()
        roundd = 6
    
    if 'rock' in request:
        plt.title('Rock Info')
        plt.ylabel('Frequency of the Event (%)')
        plt.xlabel('Outcome (Win, Loss, or Tie)')
        plt.bar(rockinfo, rockdata, width = 0.4)
        plt.ylim([0, 100])
        print("\nOf the " + str(rocks) + " times you played rock, it has resulted in:\n" + str(rockwins) + " win(s), " + str(rocklosses) + " loss(es), and " + str(rockties) + " tie(s).")
        plt.show()
        roundd = 6
    
    if 'paper' in request:
        plt.title('Paper Info')
        plt.ylabel('Frequency of the Event (%)')
        plt.xlabel('Outcome (Win, Loss, or Tie)')
        plt.bar(paperinfo, paperdata, width = 0.4)
        plt.ylim([0, 100])
        print("\nOf the " + str(papers) + " times you played paper, it has resulted in:\n" + str(paperwins) + " win(s), " + str(paperlosses) + " loss(es), and " + str(paperties) + " tie(s).")
        plt.show()
        roundd = 6
    
    if 'scissors' in request:
        plt.title('Scissors Info')
        plt.ylabel('Frequency of the Event (%)')
        plt.xlabel('Outcome (Win, Loss, or Tie)')
        plt.bar(scissorsinfo, scissorsdata, width = 0.4)
        plt.ylim([0, 100])
        print("\nOf the " + str(scissors) + " times you played scissors, it has resulted in:\n" + str(scissorwins) + " win(s), " + str(scissorlosses) + " loss(es), and " + str(scissorties) + " tie(s).")
        plt.show()
        roundd = 6
    
    if 'wvlvt' in request:
        plt.title('Wins vs. Losses vs. Ties Data')
        plt.ylabel('Ratio of Wins/Losses/Ties (%)')
        plt.xlabel('Outcome (Win, Loss, or Tie)')
        plt.bar(winsvlosses, winsvlossesdata, width = 0.4)
        plt.ylim([0, 100])
        print("\nOf the " + str(ccounter) + " rounds played, you have:\nWon " + str(wins) + " time(s), lost " + str(losses) + " time(s), and tied " + str(ties) + " time(s).")
        plt.show()
        roundd = 6

#Round 6: The original data set
if roundd == 6:
    
    print("\nAfter Graphing your data, let's look at the original data values \nthat were put into the dictionary. The file will be read in and graphed.\nEach bar will represent the item likely to be played based on the last item played,\nand will be stacked with percentages based on the likeliness after an outcome of\na win, loss, or tie:")
    print("""\nTo learn more about the data, check out the website's How does this Project Work? tab.\nThere may also be some content in the Resources paragraph!""")
    
    #prepping the data set to be graphed
    
    text = text.strip()
    
    headers = list(text.split('\n'))[0]
    headers = headers.split(',')
    
    semi_prep_text = list(text.split('\n'))
    
    prep_text = []
    for e in semi_prep_text:
        prep_text.append(e.split(','))
    prep_text.remove(headers)
    
    #Labels will be the legend
    prelabels = []
    
    #Further separating the data,
    after_win = []
    after_loss = []
    after_tie = []
    
    for e in prep_text:
        if 'after rock' in e[0]:
            prelabels.append(e[0])
            after_win.append(int(float(e[1]) // 1))
            after_loss.append(int(float(e[2]) // 1))
            after_tie.append(int(float(e[3]) // 1))
        if 'after paper' in e[0]:
            prelabels.append(e[0])
            after_win.append(int(float(e[1]) // 1))
            after_loss.append(int(float(e[2]) // 1))
            after_tie.append(int(float(e[3]) // 1))
        if 'after scissors' in e[0]:
            prelabels.append(e[0])
            after_win.append(int(float(e[1]) // 1))
            after_loss.append(int(float(e[2]) // 1))
            after_tie.append(int(float(e[3]) // 1))
    
    #Cleaning up the labels:
    
    labels = []
    
    for e in prelabels:
        split = e.split()
        first = split[0][0]
        last = split[2][0]
        after = split[1]
        newlabel = first + ', ' + last
        labels.append(newlabel)    
    
    #Stacked Bar Plot:
    wins = np.array(after_win)
    losses = np.array(after_loss)
    ties = np.array(after_tie)
    width = 0.50       # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()

    ax.bar(labels, wins, width, label='Wins')
    ax.bar(labels, losses, width, bottom=wins, label='Losses')
    ax.bar(labels, ties, width, bottom=wins+losses, label='Ties')

    ax.set_ylabel('Percentage of likeliness to happen, based on the last outcome')
    ax.set_xlabel('Based on the last game, the item to be played followed by the item played last round')
    ax.set_title('Original Data, Based on the Online Resource')
    ax.legend()

    plt.show()
    
    roundd = 7
    
#Round 7: the end
if roundd == 7:
    print('\nThanks for playing!')
    exit()
    
#Round 8: ??? confusion
if roundd == 8:
    print("\nYou must have put in a wrong input... \nto avoid issues, this program will now end. \nMake sure to be a bit more careful next time.")
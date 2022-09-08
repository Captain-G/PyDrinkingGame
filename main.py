import time
import random

print("Welcome to the Python Drinking Game :)")
time.sleep(2)
print("Answer the question you are given or take a SHOT!")
time.sleep(2)
no_of_participants = int(input("Enter the number of participants in the game : "))
names = []

for i in range(no_of_participants):
    if i == 0:
        name = input("Enter the name of the first participant : ")
        names.append(name)
    elif i == 1:
        name = input("Enter the name of the second participant : ")
        names.append(name)
    elif i == 2:
        name = input("Enter the name of the third participant : ")
        names.append(name)
    else:
        name = input("Enter the name of the other participant : ")
        names.append(name)

zero_to_max = []
print("The order of participation will be randomized . . . . . ")
time.sleep(2)

rand_order = random.sample(names, len(names))
for j in range(no_of_participants):
    print(f"{j + 1} : {rand_order[j]}")

print("Let the games begin!")
time.sleep(3.5)

lightweight_questions = [
"What's the most embarrassing thing you've ever done?",
"Have you ever broken the law? If so, why?",
"What is your biggest pet peeve?",
"What's the worst date you've been on?",
"What's the best date you've been on?",
"What is your favourite movie that you secretly know is actually terrible?",
"What was the last time you’ve laughed the hardest?",
"What’s the most childish thing you still do?",
"What is the grossest thing you have done today?",
"What was your best moment in life so far?",
"Who has the best sense of humour in this room?",
"What’s your favourite song that you secretly know is awful?",
"What’s the most embarrassing music you listen to?",
"What is the weirdest trend you've ever participated in?",
"What’s the last thing you Googled?",
"What’s the most adventurous thing you’ve ever done?",
"Who was your first real celebrity crush?",
"Who's the last person you searched on Instagram?",
"What's the drunkest you've ever been?",
"Do you ever talk to yourself in the mirror?",
"What’s your go-to karaoke song?",
"What is the weirdest thing you’ve ever bought?",
"What’s your favourite TV show that you secretly know is awful?"]

deep_questions = [
"When was the last time you lied and what was it?",
"What's the worst thing you've ever done at work?",
"What's something you're glad your family doesn't know about you?",
"Have you ever cheated on someone?",
"Have you ever been cheated on?",
"What’s the biggest misconception about you?",
"What’s the worst piece of advice you’ve given someone?",
"What was the worst mistake that you’ve made in your life?",
"When was the last time you cried and why?",
"What's your biggest fear in life?",
"What's your relationship dealbreaker?",
"What's a secret you've never told anyone?",
"What's the worst thing you've ever done?",
"What do most people think is true about you but isn’t?",
"What is the one thing you dislike about yourself?",
"What is the one thing you really like about yourself?",
"What makes a relationship toxic in your opinion?",
"What’s the best piece of advice you’ve given someone?",
"What’s the best piece of advice you’ve gotten from someone else?",
"What is your greatest weakness?",
"What is your greatest strength?",
"What’s your biggest regret so far?",
"What is your biggest insecurity?",
"Do you believe in soul mates?",
"What is the most disgusting thing you’ve ever done?",
"Do you have any anonymous social media accounts?",
"What is your worst habit?",
"What is something you wish people knew about you?",
"Have you ever re-gifted a present?",
"What’s the meanest thing you’ve ever said to someone?",
"What’s the best compliment you’ve ever given?",
"What is your biggest relationship/dating ick?",
"What’s the one thing you would do if you knew there were no consequences?",
]

naughty_questions = [
"What's your biggest fantasy?",
"Where's the weirdest place you've had sex?",
"Do you enjoy dirty talk?",
"Have you ever had a ‘friends with benefits’ situation? If so, who with?",
"What's the best intimate experience you've ever had?",
"Do you have any fetishes?",
"What's your biggest turn-on?",
"Who would you most like to kiss in this room?",
"What’s your favourite body part on another person?",
"Have you ever read erotic fiction?",
"When did you lose your virginity?",
"What’s the longest you’ve gone without sex?",
"Have you ever fallen asleep during sex?",
"What was your most embarrassing sexual experience?",
"What is your favourite sex position?",
"What is your least favourite sex position?",
"What’s your biggest turn off?",
"Have you ever slept with someone then immediately regretted it?",
"Have you ever hooked up with a friend?",
"If you could only do one sex act for the rest of your life, what would it be?",
"What is the dirtiest text you’ve received?",
"What is the dirtiest text you’ve sent?",
"Who did you last have a sexual fantasy/dream about?",
"Have you faked an orgasm?",
"Describe your best orgasm. How long did it last?",
]


for m in range(3):
    print(f"{rand_order[0]} : ")
    time.sleep(1.5)
    question_asked = random.choice(lightweight_questions)
    print(question_asked)
    index = lightweight_questions.index(question_asked)
    lightweight_questions.pop(index)
    key = input("Press any key to continue : ")
    if key != "~>~/":
        print(f"{rand_order[1]} : ")
        time.sleep(1.5)
        question_asked = random.choice(lightweight_questions)
        print(question_asked)
        index = lightweight_questions.index(question_asked)
        lightweight_questions.pop(index)
        key = input("Press any key to continue : ")

for o in range(4):
    print(f"{rand_order[0]} : ")
    time.sleep(1.5)
    question_asked = random.choice(deep_questions)
    print(question_asked)
    index = deep_questions.index(question_asked)
    deep_questions.pop(index)
    key = input("Press any key to continue : ")
    if key != "~>~/":
        print(f"{rand_order[1]} : ")
        time.sleep(1.5)
        question_asked = random.choice(deep_questions)
        print(question_asked)
        index = deep_questions.index(question_asked)
        deep_questions.pop(index)
        key = input("Press any key to continue : ")

for w in range(5):
    print(f"{rand_order[0]} : ")
    time.sleep(1.5)
    question_asked = random.choice(naughty_questions)
    print(question_asked)
    index = naughty_questions.index(question_asked)
    naughty_questions.pop(index)
    key = input("Press any key to continue : ")
    if key != "~>~/":
        print(f"{rand_order[1]} : ")
        time.sleep(1.5)
        question_asked = random.choice(naughty_questions)
        print(question_asked)
        index = naughty_questions.index(question_asked)
        naughty_questions.pop(index)
        key = input("Press any key to continue : ")


print(" . \n . \n . \nThe game is Over!")
print("Hope you had fun and definitely took some wild shots!")
print("You are welcome to play again. Cheers!")
import random

name = "Suares"
question = "Is this real life?"

magic8 = random.randint(1, 9)

answers = [
  "Yes - definitely",
  "It is decidedly so",
  "Without a doubt",
  "Reply hazy, try again",
  "Ask again later",
  "Better not tell you now",
  "My sources say no",
  "Outlook not so good",
  "Very doubtful"
]

magic8 = random.randint(0, 8)
answer = answers[magic8]

if name == "" and question != "":
    print(f"Question: {question}")
elif question == "":
    print("You must ask a question!")
else:
    print(f"{name} asks: {question}")

print(f"Magic 8-Ball's answer: {answer}")
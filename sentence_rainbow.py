# In this code we def a fuction to change the color of output text
def colorchange(color):
  if color=='r':
    print("\033[31m", end="")
  elif color==" ":
    print("\033[0m", end="")
  elif color=="b":
    print("\033[34m", end="")
  elif color=='y':
    print("\033[33m", end="")
  elif color== 'g':
    print("\033[32m", end="")
  elif color == 'p':
    print("\033[35m", end="")

sentence = input("What sentence do you want rainbow-ising?\n")
for letter in sentence:
  colorchange(letter.lower())
  print(letter, end="")
print()

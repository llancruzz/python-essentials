# If you want to use any variable global scope , you have
# to use the keyword "global".

def outer():
    global animal
    animal = "Spider Crab"


outer()

print(animal)

# The first score update the second score inside of def func
# and then score is printed out updated with new score.
score = 100


def double_score():
    global score
    score = score * 2


double_score()
print(score)

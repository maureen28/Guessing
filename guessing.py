import random 

WORDS = ['python', 'apple', 'car']
guessed = set()

scores = {
    'player': 0
}

def update_score(func):
    def x(word):
        result = func(word)
        if result:
            scores['player'] +=1
        return result
    return x

hint = lambda word: random.sample(word, len(word))

@update_score
def check_guess(word):
    guess = input(f"Guess the word?{hint(word)} \n")
    if guess == word:
        print('Okay')
        guessed.add(word)
        return True
    else:
        print('no')
        return False
        
def game():
    while len(guessed) < len(WORDS):
        word = random.choice([a for a in WORDS if a not in guessed])
        check_guess(word)
        print(f"Final score {scores['player']}")
game()

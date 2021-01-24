# Doppelkopf
Track, store and evaluate your games of the german card game classic 'Doppelkopf'

A program that allows you to input the result of each round of Doppelkopf. The points as well as card values each player scores can be stored so that some pretty in-depth data analysis i spossible - who scores the most points on average, who has the best score overall, who plays best with whom...

This is the first project I ever started in Python. It started before I had any formal education on programming or Python, and the code quality definitely reflects that. It is also wirtten in Python 2, but the transfer should be straight-forward. Given the quality of the code, there are many simple but big improvements that could be made, starting with unnecessary function definitions (sign), way too complicated exception handling and the data is stored in .txt files (yea, I know).

Once I (or you?) got around to fixing up these basics there are a lo of fancy ways this project could take. Some ideas include:
-Take a photo of your game nights' score card, that is then analyzed by an image classification algorithm that automatically enters the scores
-Predict a winner of each round (probably need to collect many more features for this)
-GUI

If you're a Doppelkopf enthusiast feel free to merge and PR, as I plan on reviving this sooner than later.

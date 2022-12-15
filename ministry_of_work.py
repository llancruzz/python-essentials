from textblob import TextBlob
import pyttsx3

engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

print(input("Enter your employee wellness statement: "))
phrase = input("> ")
blob = TextBlob(phrase)

while blob.sentiment.polarity < 0.5:
    print("More positive please: ")
    phrase = input("> ")
    blob = TextBlob(phrase)

print("We appreciate you too!")
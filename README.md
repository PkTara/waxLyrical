# Intro
Hey! This is an application made with electron, made for learning languages from songs. You can input the name of a song you'd like to learn, which will then search on Genius for the lyrics. A frequency graph will be made from the lyrics, where you can hover over the words to see translations.

It will also hopefully be able to turn these into Anki graphs (done, but not in the GUI) that you can quiz yourself on.

# File Structure

npm start
-> main.js
-> loads index.html      -> controls shortcuts
-> loads index.js 
-> uses songInfo.json

lyricAnalyser.py:
-> opens lyrics.txt
-> cleans punctuation
-> counts words
-> imports from translateWord
-> writes "songGraph.json" with this data

songToAnki
-> uses songGraph.json
-> makes anki flashcards

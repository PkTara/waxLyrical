# ** Intro**
Hey! This is an application made with electron, made for learning languages from songs. You can input the name of a song you'd like to learn, which will then search on Genius for the lyrics. A frequency graph will be made from the lyrics, where you can hover over the words to see translations.

It will also hopefully be able to turn these into Anki graphs (done, but not in the GUI) that you can quiz yourself on.

# ** File Structure**

**npm start**

_-> main.js_

_-> loads index.html      -> controls shortcuts_

_-> loads index.js _

_-> uses songInfo.json_


**lyricAnalyser.py:**

_-> opens lyrics.txt_

_-> cleans punctuation_

_-> counts words_

_-> imports from translateWord_

_-> writes "songGraph.json" with this data_

**songToAnki**

_-> uses songGraph.json_

_-> makes anki flashcards_

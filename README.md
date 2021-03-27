# acacia-regex
Many regular expressions python search engine

## File Engine/EngineRun.py 
Code to run two regular expressions together

```
    engine = Engine()
    engine.dRegEx["RegExWord"] = RegExWord()
    engine.dRegEx["RegExApostrophe"] = RegExApostroph()
    engine.sFile = 'RegExWord.py'
    engine.run()
```

Create Engine

Add regular expression class RegExWord

Add regular expression class RegExApostroph

Specify file to search

Run engine


Command output:
```
"C:\Program Files\Python38\python.exe" C:/Work/RegEx/EngineRun.py
<re.Match object; span=(106, 107), match=b"'">
<re.Match object; span=(107, 116), match=b'Something'>
<re.Match object; span=(116, 117), match=b"'">

Process finished with exit code 0
```

## File Engine/RegExWord.py
Regular expression class

```
class RegExWord(RegEx):
    def __init__(self):
        regEx=br'Something'
        recomp = re.compile(regEx)
        super().__init__(regEx, recomp)

    def hit(self, engine):
        print(self.x)
```

Class inherited from RegEx class

`__init__` specifies regular expression

`hit` is executed, when regular expression is found

## File Engine/Engine.py

Searches in file `sFile` occurences of regular expressions `dRegEx`

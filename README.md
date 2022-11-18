## **🛡️ Stoic**

A lightweight, data-saving library that provides an easy and simple way for python developers to store data in a file.

Stoic is characterized by having a hidden object oriented but superficially function-based, intuitive, and simple to use access-syntax, and by classifying data by tabs instead of braces.

My code hath compiled and i committed and pushed to github

## **📚 Installation**

Stoic is not in pyPi, so you cannot download it by pip. Instead, download the main.py file and the package and import into your project.

## **📖 Usage**

Stoic currently has:
- Adding Subsections
- Subtracting Subsections
- Retrieving Subsections
- Changing Subsections
- Changing Values
- Moving Subsections
- Retrieving Values
- Swapping Subsections
- Shorthand
- Saving
- Loading
Stoic is still in development; I am looking to add things like lists, dictionaries, classes (support for these in stoic files), as well as schemas and more.

In Stoic, you can store data in a file by creating a new instance of the stoicFile class. You can then use a function based syntax to find subsections and process or add them as you please.

For example, if you have a stoic file called "languages.stoic" with the following contents:

```
languages:
    python:
        type: interpreted
        typing: dynamic
        year: 1991
        level: high level
    nim:
        type: compiled
        typing: static
        year: 2009
        level: high level
```
and you wanted to fetch the typing of python, you could do so by doing the following:

```python
from stoic import stoicFile

langs = stoicFile("languages.stoic")
print(langs.getSubsection("languages").getSubsection("python").getValue("typing"))
```
or, obviously
```python
from stoic import stoicFile
langs = stoicFile("languages.stoic")
subS = langs.getSubsection("languages").getSubsection("python")
#obviously, since you can get the object by using the getSubsection func, and then set it to a variable, and then use that variable to get set aor fethc vlaues
print(subS.getValue("typing"))
```

This would print "dynamic" to the console, or whatever you wrote in the field.
If this seems like a lot, you can use the shorthand syntax, which is noy only a bit more intuitive but also quicker and easier to use. The shorthand syntax and more is explained in the documentation, which you can find here.



## **📖 Docs**

Stoic has two ways of documentation: 
- An inrepo wiki
- A command line interface for the docs.
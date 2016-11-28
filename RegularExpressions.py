#Fill find and replace a string
#Needed for Regular Expression use
import re
#from string or var you want to replace 
fromString = "Bunch of text you want to search for a specific entry"
#String you want to look in
findString = "Bunch"
#string you want to replace it with
replaceWith = "Grapes"
#Do the substitute and create a new String
newString = re.sub(findString,replaceWith,fromString)
#outputting the result
print "Orignal String:",fromString,"\n \n"
print "After Substitution:",newString

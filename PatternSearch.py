import re

#Paragraph provided for search and replace

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''


#Regex Variable asking to count all characters in string besides letters and numbers
#/d is digit character meaning any alphabetic or numeric characters
#This creates a variable to assign all
regex = "[^a-zA-Z\d]"


#assign the outcome to a variable called result using findall function
#this result variable catches all instances a character other than a alphanumeric 
#that are used inside the paragraph including spaces
result = re.findall(regex,lorem_ipsum)

#output to the console prints the number of non-alphanumeric characters using len function
print(len(result))

# regular expression to findall occurances; 
#creates a variable that includes all instances of 'sit dash' or 'sit colen' before amet
regex = "sit[-:]amet"

#This assigns the outcome to a variable named occurrance_sit_amet
occurrance_sit_amet = re.findall(regex,lorem_ipsum)

#Prints number of occurences that the dash/colon appear between sit amet
print(len(occurrance_sit_amet))

#Finds and or replaces each occurence that the sit - and or : amet appear without punctuation to sit amet
regex = "sit[-:]amet"
replace_results = re.sub(regex,"sit amet",lorem_ipsum)


#Findall function this finds all instances of sit amet within the paragraph
occurrance_sit_amet = re.findall(regex,lorem_ipsum)

#prints number of occurences sit amet appear in the paragraph 
print(len(occurrance_sit_amet))

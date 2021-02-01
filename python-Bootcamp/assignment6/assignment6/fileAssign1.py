#Shreeji Patel
#105151171

words = open('dictionary.txt', 'r')
story = open('story.txt', 'r')
a = []

temp = words.read()
words_list = temp.strip().split('\n')
temp2 = story.read()
story_list = temp2.split()

def checkword(a, temp_list):
    for i in range(len(temp_list)):
        if(a==temp_list[i]):
            return True
    return False

for i in range(len(story_list)):
    if checkword(story_list[i], words_list):
        pass
    else:
        a.append(story_list[i])

print(a)
print(len(a))
story.close()
words.close()
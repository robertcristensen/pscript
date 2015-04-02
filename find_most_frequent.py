def find_most_frequent(text):
    separs=",.:;!?-"
    words_stats={}
    result=[]
    for s in separs: 
        if s in text: text = text.replace(s, " ")
    text = text.lower().split(" ")
    for word in text:
        if word != "":
            words_stats[word]=int(text.count(word))
    for item in words_stats:
        if words_stats[item] == max(words_stats.values()):
            result.append(item)
    result.sort()        
    return result




print(find_most_frequent('Hello,Hello, my dear!'))
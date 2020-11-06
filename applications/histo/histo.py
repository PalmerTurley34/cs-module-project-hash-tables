def word_count(s):
    chars = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
    
    words = s.split()
    for i in range(len(words)):
        words[i] = words[i].strip('" : ; , . - + = / \ | [ ] { } ( ) * ^ &')
        words[i] = words[i].lower()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            if word:
                counts[word] = 1

    return counts

with open("applications\histo\robin.txt") as f:
    words = f.read()
words = words.split()
counts = word_count(words)
counts.sort()
# unfinished

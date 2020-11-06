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



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))

import re

def word_frequency(text):
    word_count = {}
    for word in text:
	       words =re.sub(r'[,.!-?0-9A-Za-z]', "", text).lower().split()
    for word in word_count:
               word_count[word]+=1
	       else:
               word_count[word]=1
    return word_count


def main():
    text=open('sample.txt')
    answer=sorted(word_frequency(text).items(), key=word_count, reverse=True)[:20]:
    print(answer)

if __name__ == '__main__':
    main()

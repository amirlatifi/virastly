import sys


def viraiesh(text):
    text = text.replace('ي', 'ی')
    text = text.replace('ك', 'ک')
    text = text.replace('ـ', '')
    text = text.replace(' می ', ' می‌')
    text = text.replace(' نمی ', ' نمی‌‌')
    text = text.replace(' هـای ', '‌هـای ')
    text = text.replace('میتوان', 'می‌توان')
    text = text.replace('میكنم', 'می‌كنم')
    text = text.replace('میدهن', 'می‌‌دهن')
    text = text.replace('میكند', 'می‌كند')
    text = text.replace('نمیگذارد', 'نمی‌گذارد')
    text = text.replace('میگوید', 'می‌گوید')
    text = text.replace(' تـرين ', ' تـرين‌')
    text = text.replace(' تـری ', ' تـری‌')
    return text.replace('ة', 'ه‌ی')


def main():
    file = open(sys.argv[1], "r")
    if file.mode != 'r':
        print(sys.argv[1] + ' is not readable')
    else:
        text = file.read()
        result = viraiesh(text)
        f = open("result.txt", "w+")
        f.write(result)
        print('Done! Check result.txt')


main()

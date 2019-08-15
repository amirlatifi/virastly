import sys


def viraiesh(text):
    return text.replace('ي', 'ی')


def execute():
    text = str(sys.argv[1])
    result = viraiesh(text)
    print(result)


execute()

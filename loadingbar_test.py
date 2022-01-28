from time import sleep


def load_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='>'):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * iteration / float(total))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()


items = list(range(0, 50))
l = len(items)

load_bar(0, l, prefix="Prefix", suffix="Complete", length=l)
for i, items in enumerate(items):
    sleep(0.1)
    load_bar(i + 1, l, prefix="Prefix", suffix="Complete", length=l)

import requests
from time import sleep


def load_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='>'):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * iteration / float(total))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()


class WordFinder:
    def __init__(self, rand_string, min_let):
        self.rand_string = rand_string
        self.min_let = min_let
        self.child_strings = []
        self.all_strings = []
        self.results = []

    def string_setter(self, rand_string):
        self.rand_string = rand_string

    def min_let_setter(self, min_let):
        self.min_let = min_let

    def permutations(self, rand_string):
        if len(rand_string) == 1:
            return [rand_string]
        perms = self.permutations(rand_string[1:])
        char = rand_string[0]
        result = []
        for perm in perms:
            for i in range(len(perm) + 1):
                if not perm[:i] + char + perm[i:] in result:
                    result.append(perm[:i] + char + perm[i:])
                else:
                    pass
        return result

    def child_string_finder(self, input_string, acc, minim_letters):
        if len(input_string) < minim_letters:
            return
        if input_string not in self.child_strings:
            self.child_strings.append(input_string)
        spit_1 = input_string[acc]
        spit_2 = input_string[:acc] + input_string[acc + 1:]
        self.child_string_finder(spit_1, 0, minim_letters)
        self.child_string_finder(spit_2, 0, minim_letters)

        acc += 1
        if acc != len(input_string):
            self.child_string_finder(input_string, acc, minim_letters)

    def calc_all_strings(self):
        for word in self.child_strings:
            for word2 in self.permutations(word):
                if word2 not in self.all_strings:
                    self.all_strings.append(word2)
        i = 0
        load_bar(i, len(self.all_strings), prefix="Prefix", suffix="Complete", length=50)
        for word in self.all_strings:
            response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/' + word)
            status = response.status_code
            if status != 429:
                if status == 200:
                    self.results.append(word)
                load_bar(i + 1, len(self.all_strings), prefix="Prefix", suffix="Complete", length=50)
                i += 1
            elif status == 429:
                while status == 429:
                    x = 30
                    while x >= 0:
                        print(f"{x} seconds remaining")
                        sleep(1)
                        x -= 1

                    response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/' + word)
                    status = response.status_code
                    print(f"{status}\n")

                if status == 200:
                    self.results.append(word)
                load_bar(i + 1, len(self.all_strings), prefix="Prefix", suffix="Complete", length=50)


if __name__ == '__main__':
    user_exit = 0
    while user_exit == 0:
        try:
            user_string = input("What is the string?: ")

            minim_let = int(input("What is the minimum number of letters?: "))

            string_object = WordFinder(user_string, minim_let)
            string_object.child_string_finder(string_object.rand_string, 0, string_object.min_let)
            string_object.calc_all_strings()
            print(string_object.results)

            user_exit = int(input("Would you like to continue? \n0 = Yes, 1-9 = No\n"))
        except ValueError:
            print("Please input a valid number")

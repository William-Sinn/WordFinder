tested_strings = []


def string_test(string, acc, space, total_str):
    if len(string) < 3:
        return
    if string not in tested_strings:
        tested_strings.append(string)
    elif string == total_str:
        pass
    else:
        return
    space += ' '
    print(string, "<-parent string")
    spit_1 = string[acc]
    spit_2 = string[:acc] + string[acc + 1:]
    print(space + spit_1)
    print(space + spit_2)
    string_test(spit_1, 0, space, total_str)
    string_test(spit_2, 0, space, total_str)

    acc += 1
    if acc != len(string):
        string_test(string, acc, space, total_str)


string_test('doggy', 0, '', 'doggy')
print(tested_strings)

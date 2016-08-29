code = input('Please enter the ISBN-13 number with or with \'-\'s: ')

codex = ''

for each in code:
    if each is '-':
        pass
    else:
        codex = codex + each

code = codex
code = code[::-1]
code_even = code[1::2]
code_odd = code[::2]

total = 0

for x in code_odd:
    y = int(x)
    total = total + (y * 3)

for z in code_even:
    z = int(z)
    total = total + z

check = abs((total % 10) - 10)

print('Checksum is equal to ' + str(check))
print('The ISBN-13 total before adding the checksum is equal to ' + str(total))

input('')
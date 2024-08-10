
alphabets='abcdefghijklmnopqrstuvwxyz'
numbers ='1234567890'
symbols='!@#$%^&*(){}[]"\|?/.,<>'

user_input = input("Give your input to convert:").lower()
try:
    shift = int(input('give shift:'))
except ValueError:
    print('Wrong Input only Integers are accepted!')

u = user_input.split()

letters = [i for i in user_input]
alphabets = [a for a in alphabets]
ans = []

for lets in letters:
    for alphs in alphabets:
        if lets in alphs:
             index = (alphabets.index(alphs) + shift) % len(alphabets)
             ans.append(alphabets[index])
        if lets == ' ':
            ans.append('_')
        
print(''.join(ans))
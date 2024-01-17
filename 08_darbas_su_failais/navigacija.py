import os

print(os.getcwd())
os.chdir('PTU20_live')
print(os.getcwd())

if os.path.exists('labas.txt'):
    with open('labas.txt', 'r') as labas_f:
        for line in labas_f:
            print(line, end='')
    print()
else:
    print('file is not there')

if not os.path.exists('siuskles'):
    os.makedirs('siuksles')
    with open('siuksles/siuksle', 'w') as siuksle:
        siuskle.write('xxx')
else:
    if os.path.exists('siuskles/siuksle'):
        os.remove('siuksle/siuksle')
    os.rmdir('siuskles')
os.chdir('..')
print(os.getcwd())
import os
#1°modo
#os.remove('teste.txt')

#2° modo
if os.path.exists('teste.txt'):
    os.remove('teste.txt')
else:
    print('arquivo não existe!!!')



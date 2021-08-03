import os
names = os.listdir('screenshots')
os.chdir('screenshots')
for i in names:
    os.rename(i, '0' * (4 - i.index('.')) + i)

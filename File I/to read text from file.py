#to check weather poem.txt contains twinkle or not
f = open(f'File I/poem.txt')
t=f.read()
if 'twinkle' in t:
    print("Twinkle is present")
else:
    print("twinkle is not present")
f.close()
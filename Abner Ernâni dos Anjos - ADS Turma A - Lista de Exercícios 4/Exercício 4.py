statement= 'The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you'
a= statement.split(' ')
b= []
for i in range(int(len(a))):
    if (a[i].lower())[:1:] in 'python':
        b.append(a[i])
    elif (a[i].lower())[-1::] in 'python':
        b.append(a[i])
print('No texto:\n\n', statement)
print('\n')
print('Palavras que começam com uma das letras da palavra ´python´ são:\n\n', b)

frase = str(input())
print('1', frase[2]) #Сначала выведите третий символ этой строки
print('2', frase[-2]) #Во второй строке выведите предпоследний символ этой строки.
print('3', frase[:5]) #В третьей строке выведите первые пять символов этой строки.
print('4', frase[:-2]) #В четвертой строке выведите всю строку, кроме последних двух символов.
print('5', frase[::2]) #В пятой строке выведите все символы с четными индексами
print('6', frase[1::2]) #В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
print('7', frase[::-1]) #В седьмой строке выведите все символы в обратном порядке.
print('8', frase[-1::-2]) #В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
print('9', len(frase)) #В девятой строке выведите длину данной строки.
print(len(frase.split()))#cколько слов в строке, разделённых пробелами
frase = frase.replace('1', 'one')#заменить 1 на one
print(frase)

frasedel3 = ''.join([c for i, c in enumerate(frase) if i % 3]) #удалить все символы, чьи индексы делятся на три
print(frasedel3)
frase2 = ' '.join(input().split(' ')[::-1]) #поменять слова местами
print(frase2)
print('*'.join(frase2)) #вставить * между двух символов




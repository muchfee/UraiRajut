def urai(kata):
    translation = "" #mebuat string kosong agar ditambah dengan kata
    for huruf in kata:
        translation+=kata #setiap huruf yang ada di kata maka = transalaition +kata
    return translation
urai("code")
urai('Python')
urai('Purwhadika')


def rajut(string):
    temp = ''#membuat string kosong

    for i in string: #setiap i yang ada di string akan dimasukan ke temp
        if i not in temp: #kalau i tidak ada temp
            temp += i #makaa tempnya akan ditambah dengan huruf yang tidak ada di i

    return temp

print(rajut('CCoCodCode'))
print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))
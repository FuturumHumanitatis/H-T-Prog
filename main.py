# Theory of Nicomah
def nicomah_func(start, n):
    return int((start + n) * (n - 1) / 2) ** 2


n = 16 ** 9
start = 2

print(sum(map(int, list(str(nicomah_func(start, n))))))

#Mne pofig
for x in range(72,63,-1):
    if sum(map(int, list(bin(x)[2:]))) == 4:
        print(x)

#Shto-to eshe
a = '0.B6DB6DB6DB6D'
# ответ: 48
print(sum(map(int, list('10010010010010010010010010010010010010101011011010101101101101001010110100111110000010101010101101101'))))

#dalshe
# ответ: 3

#eshe

# print(pow(0.001953125,13) + pow(0.015625,7) + pow(0.125,2))
#0.0400000000400005FCAD0E837EF97E39FD7D26074FADF306D45E659F518616A23719F6F1BA4EB944EBC5727B72662A50C427
S = 0
s = '00400000000400005FCAD0E837EF97E39FD7D26074FADF306D45E659F518616A23719F6F1BA4EB944EBC5727B72662A50C427'
for l in s:
    if l == 'A':
        S += 10
    elif l == 'B':
        S += 11
    elif l == 'C':
        S += 12
    elif l == 'D':
        S += 13
    elif l == 'E':
        S += 14
    elif l == 'F':
        S += 15
    else:
        S += int(l)
print(S)
#ответ 661
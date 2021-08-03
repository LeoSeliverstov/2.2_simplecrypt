from simplecrypt import decrypt, DecryptionException

pwd = []  # пароли храним в списке
with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()  # при with закрывать не нужно

f = open('passwords.txt', 'r')
for line in f:
    s = line.strip()
    pwd.append(s)
f.close()  # а вот здесь нужно. Зато удобно - построчно сразу читаем в список

for i in range(len(pwd)):
    try:
        plaintext = decrypt(pwd[i], encrypted).decode('utf8')  # декодирует в байтах, переводим в текст
        print(plaintext)
    except DecryptionException:
        pass

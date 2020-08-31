number = input("Bir sayi yazin, amstrong bir sayi mı görelim:")


if not number.isdecimal():
    print('Lutfen pozitif tam sayi degeri giriniz')
else:
    total = 0
    power = len(number)
    for num in list(number):
        total += int(num) ** power
    if total == int(number):
        print(f'{number} sayisi amstrong bir sayidir.')
    else:
        print(f'{number} sayisi amstrong bir sayi degildir.')
import random as ra
print('Assalomu alaykum')
print('Bu dastur sizni matematika bo`yich bilimingizni sinaydi')
name=str(input('Iltimos,  ismingizni kiritng:  ')).upper()
print(name,'  , siz quyidagi yo`nalishlardan birini tanlashingiz kerak')
print('1: sonlarni qo`shish ')
print('2: sonlarni ayirish ')
while True:
    tanlov=int(input('Kerakli yo`nalishning raqamini kiriting va enter tugmasini bosing. '))
    if tanlov==1:
        print('Siz qo`shishni tanladingiz ')
        break
    elif tanlov==2:
        print('Siz ayirishni tanladingiz ')
        break
    else:
        print('Siz 1 yoki 2 sonlarini kiritishingiz mumkin ')
savolSon=int(input('Nechta savolga  javob bermoqchisiz? '))
topildi=0
for i in range(1,savolSon+1):
    a=ra.randint(1,100)
    b=ra.randint(1,100)
    if tanlov==1:
        result=a+b
        print(a,'+',b,'=')
        sizResult=int(input())
        if result==sizResult:
            print('Ofarin siz to`g`ri topdingiz...')
            topildi=topildi+1
        else:
            print('Xato, aslida javob ',result,' bo`ladi ')
    else:
        tanlov== 2
        result=a-b
        print(a,'-',b,'=')
        sizResult=int(input())
        if result==sizResult:
            print('Ofarin siz to`g`ri topdingiz...')
            topildi=topildi+1
        else:
            print('Xato, aslida javob ',result,' bo`ladi ')
print('Hurmatli ',name,' savollar soni tugadi...')
print('Siz ',savolSon,' ta savoldan ',topildi,' tasini topdingiz')
foiz=topildi/savolSon*100
print('Bu esa ',foiz,' % ni tashkil qiladi')
##56-2, 56-70-3, 71-85-4, 86-5
if foiz<56:
    print('Afsuski bahoingiz 2...')
elif foiz>=56 and foiz<71:
    print('Afsuski bahoingiz 3...')
elif foiz>=71 and foiz<86:
    print('Yomon emas, bahoingiz 4...')
else:
    print('Barakalla siz  5 baho oldingiz...')

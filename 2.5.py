import math

leiv = float(input('Anna leiviskät: '))
naula = float(input('Anna naulat: '))
luoti = float(input('Anna luodit: '))

massa = 13.3 * luoti + naula * 32 * 13.3 + leiv * 20 * 32 * 13.3
massakg = math.floor(massa / 1000)
massag = massa - massakg * 1000

print(f'Massa nykymittojen mukaan: {massakg} kilogrammaa ja {massag:.2f} grammaa.')
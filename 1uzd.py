"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

1)Kādus ciparus jūs ziniet? - Arābu.                    21
2)Kādus romiešu ciparus ziniet? I, V, C, M, X, L, D     XXI
3)Kas ir klase? Klase ir programmēšanas struktūra, kas var definēt datu uzvedību un metodes.
4)Klase sastāv no konstruktora/destruktora un metodem (iekšējām funkcijām)
5)Patrametri ir iekšējie klases mainīgie
6)Kādas datu struktūras zinat? 
-list(saraksts) tukšs - a=""
-arry(masīvs)
-dict(vārdnīca) tukšs a={} a=dict()
7)Vārdnīcu var saprast kā kollonu ar divām kollonām.
Kollonai nav nosaukumu, taču viena ir atslēga un otra tās vērtība.
"""
class AAA:
    #jādefinē konstruktors
    def __init__(self):
        self.roma.sk={
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10: 'X', 
            40: 'XL', 
            50: 'L', 
            90: 'XC', 
            100: 'C', 
            400: 'CD', 
            500: 'D', 
            900: 'CM', 
            1000: 'M'
        }
    # definē nepieciešamās metodes
    def to_roman(self, num): 
        result = "" 
        for value, numeral in sorted(self.roma_sk.items(), key=lambda x: x[0], reverse=True): 
            while num >= value: 
                result += numeral 
                num -= value  #num=num-value
        return result

# piemērs
skaitlis=21
 # definējam objektu
kk=AAA()
# jaunajam objektam jāizsauc klases metode
romiesu=kk.to_roman(skaitlis)

#noformēt izdruku
print(f"[{skaitlis} ar romiešu cipariem ir {romiesu}.")
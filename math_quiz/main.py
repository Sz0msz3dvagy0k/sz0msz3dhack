from sympy import symbols, Eq, solve
import math
# Vonat hossza
def vonat_hossza(alagut_hossza, atjutasi_ido, lampa_ido):
    v = (alagut_hossza + (atjutasi_ido * lampa_ido)) / atjutasi_ido
    vonat_hossz = v * lampa_ido
    return vonat_hossz

alagut_hossza = 300
atjutasi_ido = 20
lampa_ido = 5

vonat_hossz = vonat_hossza(alagut_hossza, atjutasi_ido, lampa_ido)
print(f'1.: {vonat_hossz}')


# Marcipántégla térfogata
def legnagyobb_marcipan_terfogat(kockak):
    kockak.sort()
    return kockak[1] * kockak[2] * kockak[3]

kockak = [2, 2, 6, 8]
terfogat = legnagyobb_marcipan_terfogat(kockak)
print(f'2.: {terfogat}')


# Jancsi és Juliska
def biciklitavolsag(jancsi_gyalog, jancsi_bicikli, juliska_gyalog, juliska_bicikli, tavolsag):
    x = symbols('x')
    t_juliska = x / juliska_bicikli + (tavolsag - x) / juliska_gyalog
    t_jancsi = (tavolsag - x) / jancsi_gyalog + x / jancsi_bicikli
    egyenlet = Eq(t_juliska, t_jancsi)
    megoldas = solve(egyenlet, x)
    return megoldas[0]

jancsi_gyalog = 5
jancsi_bicikli = 12
juliska_gyalog = 4
juliska_bicikli = 10
tavolsag = 20

bicikli_tavolsag = biciklitavolsag(jancsi_gyalog, jancsi_bicikli, juliska_gyalog, juliska_bicikli, tavolsag)
print(f'3.: {bicikli_tavolsag}')

# Rácspontok a körvonalon
def rácspontok_korvonalon(sugar):
    rácspontok = []
    for x in range(-sugar, sugar + 1):
        y2 = sugar**2 - x**2
        y = int(math.sqrt(y2))
        if y**2 == y2:
            rácspontok.append((x, y))
            if y != 0:
                rácspontok.append((x, -y))
    return len(rácspontok)

sugar = 5
rácspontok_szama = rácspontok_korvonalon(sugar)
print(f'4.: {rácspontok_szama}')


def haromszog_csucspontja(A, B, C, terulet):
    # A háromszög csúcspontjának x koordinátájának kiszámítása
    x_A, y_A = A
    x_B, y_B = B
    x_C, y_C = C

    # A terület alapján meghatározzuk az egyik oldal hosszát
    oldal_hossz = 2 * terulet / abs(x_A - x_B)

    # Az x koordináta a terület és az oldal hossza alapján
    csucspont_x = min(x_A, x_B) + oldal_hossz

    return csucspont_x


A = (0, 4)
B = (3, 0)
C = (0, 6)
terulet = 7

csucspont_x = haromszog_csucspontja(A, B, C, terulet)
print(f'5.: {csucspont_x}')


# Paintball lövések
def paintball_lovesek(tavolsagok):
    return len(tavolsagok)

tavolsagok = [1, 2, 3, 4, 5]
max_lovesek_szama = paintball_lovesek(tavolsagok)
print(f'6.: {max_lovesek_szama}')


# Golyók színe
def golyok_szine():
    piros_golyok = 30 - (23 - 2)
    return piros_golyok

piros_golyok = golyok_szine()
print(f'7.: {piros_golyok}')


# Nagy négyzet területe
def nagy_negyzet_terulete(atlo_terulete):
    oldal = math.sqrt(atlo_terulete / 2)
    return oldal**2

atlo_terulete = 85
terulet = nagy_negyzet_terulete(atlo_terulete)
print(f'8.: {terulet}')


# Elköszönés
E, M = symbols('E M')

# Egyenletek felírása
equation1 = E * (E + M - 1) - 198
equation2 = M * (E + M - 1) - 308

# Egyenletek megoldása
solution = solve((equation1, equation2), (E, M))

# Csak pozitív egész megoldások szűrése
valid_solutions = [(e, m) for e, m in solution if e > 0 and m > 0 and e.is_integer and m.is_integer]

# Eredmény kiírása
for e, m in valid_solutions:
    print(f'9.: {valid_solutions[0][0]}')






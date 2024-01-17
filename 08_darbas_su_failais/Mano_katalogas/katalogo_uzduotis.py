import os

failo_kelias = 'tekstas.txt'
with open(failo_kelias, 'w') as f:
    f.write('Tai yra testinis failas')

if os.path.exists(failo_kelias):
    os.remove(failo_kelias)
    print(f'failas "{failo_kelias}" istrintas')
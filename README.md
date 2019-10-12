# Metoda d'Hondta w praktyce


## 54 głosy zmieniają wynik wyborów parlametarnych w 2015

W okręgu **23 Rzeszów** oddano **507 257** głosów ważnych i **12 363** głosów nieważnych.
Gdyby oddano **54** głosy więcej na PSL, to PSL miałby w o jeden mandat więcej (kosztem PIS).


## Każdy głos się liczy
W wyborach parlamentarnych 2015, oddano niemal #400 tys. głosów nieważnych# i
ponad #2,5 miliona# oddane na partie, które nie weszły do parlamentu.

# Cel
Niniejszy program ma na celu pokazanie, że każdy głos się liczy, w szczególności w wyborach, w których mandaty
są przyznawane za pomocą metody d'Hondta.


## Działanie

Program dhondt.py czyta plik (domyślnie) results2015.json i pokazuje:

1. Dane dla każdego z okręgów wyborczych w postaci:

```
33	Kielce	16	468690
	Last: PSL	22287.0	2
	>>>>: KUK	22057.5	2
Decyduje: 459 głosów
```

Gdzie (dane odczytane z pliku json):

- **33** to numer okręgu
- **Kielce** - nazwa
- **16** - liczba mandatów do obsadzenia
- **468 690** - liczba oddanych głosów ważnych

Następnie pokazuje wyliczenia:

- Last - jest to nazwa partii, która jako ostatnia otrzymała miejsce, wraz z "dzielnikiem" (22287) i liczbą otrzymanych mandatów (2)
- Lost - jest to nazwa (innej) partii, na którą gdyby oddano więcej głosów to ona otrzymałaby ostatnie do obsadzenia miejsce w tym okręgu.
- Decyduje 459 głosów -- liczba głosów, które zmieniłyby wynik wyborów w tym okręgu.





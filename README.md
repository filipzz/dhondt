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

## Więcej

Tu znajdują się pełne tabele: [tabele.md](tabele.md)

## Działanie

Program dhondt.py czyta plik (domyślnie) results2015.json i pokazuje:

1. Dane dla każdego z okręgów wyborczych w postaci:

```
33	Kielce	16	468690
	Last: PSL	22287.0	2
	Lost: KUK	22057.5	2
Decyduje: 459 głosów
```

Gdzie (dane odczytane z pliku json):

- **33** to numer okręgu
- **Kielce** - nazwa
- **16** - liczba mandatów do obsadzenia
- **468 690** - liczba oddanych głosów ważnych

Następnie pokazuje wyliczenia:

- **Last** - jest to nazwa partii, która jako ostatnia otrzymała miejsce, wraz z "dzielnikiem" (22287) i liczbą otrzymanych mandatów (2)
- **Lost** - jest to nazwa (innej) partii, na którą gdyby oddano więcej głosów to ona otrzymałaby ostatnie do obsadzenia miejsce w tym okręgu.
- **Decyduje 459 głosów** -- liczba głosów, które zmieniłyby wynik wyborów w tym okręgu (Lost +1 mandat, Last -1 mandat).


## Output

```

1	Legnica	11	356779
	Last: PO	22515.0	4
	Lost: PIS	21228.333333333332	6
Decyduje: 5147 głosów

2	Wałbrzych	8	234095
	Last: PO	19106.0	4
	Lost: PIS	18232.25	4
Decyduje: 3495 głosów

3	Wrocław	14	523371
	Last: PIS	27220.5	6
	Lost: PO	26597.0	6
Decyduje: 3741 głosów

4	Bydgoszcz	12	374277
	Last: PIS	22604.8	5
	Lost: PO	22189.6	5
Decyduje: 2077 głosów

5	Toruń	13	362510
	Last: PIS	20283.833333333332	6
	Lost: PO	18686.4	5
Decyduje: 7988 głosów

6	Lublin	15	487720
	Last: PIS	23201.4	10
	Lost: KUK	22724.0	2
Decyduje: 955 głosów

7	Chełm	12	339686
	Last: PIS	20390.25	8
	Lost: PSL	19344.5	2
Decyduje: 2092 głosów

8	Zielona Góra	12	346218
	Last: PO	19535.2	5
	Lost: PSL	17743.0	1
Decyduje: 1793 głosów

9	Łódź	10	359064
	Last: KUK	25992.0	1
	Lost: PO	22466.6	5
Decyduje: 3526 głosów

10	Piotrków Trybunalski	9	285721
	Last: PO	22086.5	2
	Lost: PSL	21364.0	1
Decyduje: 723 głosów

11	Sieradz	12	369745
	Last: PIS	21089.0	7
	Lost: PET	19681.0	1
Decyduje: 1408 głosów

12	Kraków I (południe)	8	271577
	Last: KUK	23551.0	1
	Lost: PIS	22202.166666666668	6
Decyduje: 1349 głosów

13	Kraków II (północ)	14	542768
	Last: PO	26711.6	5
	Lost: PET	26411.0	2
Decyduje: 602 głosów

14	Nowy Sącz	10	310461
	Last: PIS	23501.25	8
	Lost: PO	21654.5	2
Decyduje: 3694 głosów

15	Tarnów	9	291641
	Last: PSL	23552.0	1
	Lost: PIS	21660.428571428572	7
Decyduje: 1892 głosów

16	Płock	10	300202
	Last: PIS	21905.166666666668	6
	Lost: PET	15451.0	1
Decyduje: 6455 głosów

17	Radom	9	275342
	Last: KUK	23149.0	1
	Lost: PIS	21793.0	6
Decyduje: 1356 głosów

18	Siedlce	12	375240
	Last: PIS	23966.625	8
	Lost: PET	17386.0	1
Decyduje: 6581 głosów

19	Warszawa I (miasto)	20	1095215
	Last: PIS	40917.75	8
	Lost: PET	36657.25	4
Decyduje: 17042 głosów

20	Warszawa II (okręg)	12	490616
	Last: PO	30806.75	4
	Lost: PSL	18666.0	1
Decyduje: 12141 głosów

21	Opole	12	338248
	Last: PIS	18785.2	5
	Lost: PO	17746.2	5
Decyduje: 5195 głosów

22	Krosno	11	326865
	Last: PO	22485.5	2
	Lost: PIS	21862.5	8
Decyduje: 1246 głosów

23	Rzeszów	15	507257
	Last: PIS	23720.166666666668	12
	Lost: PSL	23667.0	1
Decyduje: 54 głosów

24	Białystok	14	435368
	Last: PET	23361.0	1
	Lost: PIS	21952.777777777777	9
Decyduje: 1409 głosów

25	Gdańsk	12	427131
	Last: PIS	25293.2	5
	Lost: PO	24717.5	6
Decyduje: 2879 głosów

26	Gdynia	14	466708
	Last: PIS	24283.0	6
	Lost: PSL	15064.0	1
Decyduje: 9219 głosów

27	Bielsko0Biała	9	337288
	Last: PIS	27266.0	5
	Lost: PO	26502.0	3
Decyduje: 2292 głosów

28	Częstochowa	7	236634
	Last: PIS	21193.25	4
	Lost: PET	15942.0	1
Decyduje: 5252 głosów

29	Gliwice	9	293667
	Last: PIS	22396.0	4
	Lost: PO	21282.5	4
Decyduje: 4454 głosów

30	Rybnik	9	289963
	Last: PIS	22959.8	5
	Lost: PET	18341.0	1
Decyduje: 4619 głosów

31	Katowice	12	411190
	Last: PO	23331.6	5
	Lost: PIS	22561.166666666668	6
Decyduje: 3853 głosów

32	Sosnowiec	9	284643
	Last: PIS	21102.5	4
	Lost: PO	18188.75	4
Decyduje: 11655 głosów

33	Kielce	16	468690
	Last: PSL	22287.0	2
	Lost: KUK	22057.5	2
Decyduje: 459 głosów

34	Elbląg	8	200362
	Last: PIS	15809.0	4
	Lost: PSL	13411.0	1
Decyduje: 2398 głosów

35	Olsztyn	10	266166
	Last: PET	18141.0	1
	Lost: PO	18013.75	4
Decyduje: 128 głosów

36	Kalisz	12	363184
	Last: PO	22417.0	4
	Lost: PSL	19937.0	2
Decyduje: 4960 głosów

37	Konin	9	277384
	Last: PET	19237.0	1
	Lost: PSL	19027.0	1
Decyduje: 210 głosów

38	Piła	9	270273
	Last: PSL	20712.0	1
	Lost: PET	18859.0	1
Decyduje: 1853 głosów

39	Poznań	10	409886
	Last: PO	29228.2	5
	Lost: KUK	24825.0	1
Decyduje: 4404 głosów

40	Koszalin	8	217017
	Last: PET	17488.0	1
	Lost: PO	16315.5	4
Decyduje: 1173 głosów

41	Szczecin	12	380499
	Last: PIS	22139.4	5
	Lost: PSL	14776.0	1
Decyduje: 7364 głosów


Wyniki wyborów
PIS	235
PO	138
PSL	16
KUK	42
PET	28



Co by było gdyby...
okręg wyborczy	partia	liczba głosów
23	Rzeszów	PSL	54
6	Lublin	KUK	955
11	Sieradz	PET	1408
4	Bydgoszcz	PO	2077
7	Chełm	PSL	2092
27	Bielsko0Biała	PO	2292
8878

```





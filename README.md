# Election_Scraper
Projekt slouží k získání dat z výsledků parlamentních voleb v roce 2017. [Zdroj](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)

### Instalace knihoven
Použité knihovny jsou obsaženy v souboru requirements.txt. Pro instalaci doporučuji nové virtuální prostředí a s nainstalovaným manažerem následně spustit:
```
$ pip3 --versions
$ pip3 install -r requirements.txt
```
### Spuštění programu
Pro spuštění programu scraper.py v příkazovém řádku jsou vyžadovány 2 argumenty:
```
py scraper.py <URL územního celku> <název souboru výstupu s příponou .csv>
```
### Ukázka
1. argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
2. argument: prostejov_vysledky.csv

```
py scraper.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103' 'prostejov_vysledky.csv'
```

#### Částečný výstup
```
Code	Location	Registered	Envelopes	Valid	Občanská demokratická strana	Řád národa - Vlastenecká unie	CESTA ODPOVĚDNÉ SPOLEČNOSTI
506761	Alojzov	205	145	144	29	0	0
589268	Bedihošť	834	527	524	51	0	0
589276	Bílovice-Lutotín	431	279	275	13	0	0
589284	Biskupice	238	132	131	14	0	0
```

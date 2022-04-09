# DPG
## Semaphore
Vaším úkolem je napsat program, který ze standardního vstupu načte čísla N a M. Program následně vytvoří N vláken a sdílený prostředek, ke kterému může přistupovat maximálně M vláken v jednu chvíli.

Po získání sdíleného prostředku vypíše vlákno i na výstup Hello from Thread-{i}!, kde {i} je index vlákna (indexováno od jedničky). Po výpisu zprávy se vlákno uspí na 300 ms.

Pokud vlákno nezíská sdílený prostředek do 100 ms, vypíše na výstup zprávu Thread-{i} is waiting... a bude pokračovat v čekání na sdílený prostředek.
## MPI
Vaším úkolem je vyzkoušet si MPI operace Scatter a Gather v jazyce Python za použití knihoven mpi4py a numpy.

Program bude dělat následující:

Procesor 0 vygeneruje numpy sekvenci od 0 do N*100-1, kde N je počet MPI procesů.

Procesor 0 rozdělí pole na N částí, každému procesoru tedy pošle pole o 100 prvcích. (tzn., že Procesor 1 obrží čísla 100 až 2*100-1, Procesor 2 pak obrží čísla 2*100 až 3*100-1, apod.)

Každý procesor následně zjistí, která čísla jsou prvočísla a která ne. Obržené pole transformuje na pole typu boolean, kde hodnota True značí prvočíslo a pošle na Procesor 0.

Příklad:
Procesor 1 obrží pole [100, 101, 102, 103, ..., 199]
Procesor 1 pošle pole [False, True, False, True, ..., True]

Procesor 0 obrží pole booleanů od ostatních procesorů, zkombinuje do matice (shape bude (N, 100)) a zapíše jej do binárního souboru true-false.npy

Soubor mpi_test.py asi bude začínat přibližně takto:
```
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
```
## REST
Vaším úkolem je vyzkoušet si REST API, na fake API serveru jsonplaceholder.

Na serveru je několik kolikcí, na kterých je možné si vyzkoušet přístup a manipulaci s daty pomocí definováného API.

Vstupem do programu budou dvě slova oddělená mezerou. Slova budeme dále nazývat jako klíč a slovo.

Program načte dvě slova ze vstupu a provede následující:

Načte všechny položky v kolekci posts.
Zjistí, které položky obsahují slovo slovo v hodnotě klíče klíč Tzn., že pokud klíč=title, budu hledat pouze slovo slovo v klíčí title.
Z filtrovaných položek zachytí všechny hodnoty userId a vytvoří tak pole povolených userId.
Načte pouze uživatele z kolekce users, kde se hodnota id vyskytuje v poli povolených userId.
Ze seznamu uživatelů zachytí hodnotu username.

Poznámky:
Slovo klíč může nabývat pouze hodnot title nebo body.
Při dotazování kolekce users je nutné předat všechny hodnoty jako url parametr.
např.: https://jsonplaceholder.typicode.com/users?id=3&id=10
### Ukázka vstupu
```
title blanditiis
```
### Ukázka výstupu
```
title with word 'blanditiis': 2
User Ids: 7, 9
Query params: id=7&id=9
Usernames: Elwyn.Skiles, Delphine
```

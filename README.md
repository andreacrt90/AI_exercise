# AI_exercise
Repository per l'elaborato relativo all'esame di Intelligenza Artificiale di Andrea Corti


PROGETTO INTELLIGENZA ARTIFICIALE
Andrea Corti, m. 4943389

L'esercizio prevede la risoluzione tramite euristica min-conflicts di due problemi di ricerca locale: 
n-queens e map-coloring.

Gli algoritmi sono stati implementati in python utilizzando Pycharm. 
I file pronti per l'esecuzione si trovano nelle relative cartelle "n_queens" e "map_coloring":

- n_queens -> min_conflicts.py
- map_coloring -> min_conflicts_min_colors.py

I file prevedono input da tastiera per le dimensioni del problema solo se presente la nomenclatura "nomefile_input.py"; 
negli altri file occorre modificare manualmente le dimensioni dei problemi nelle chiamate delle funzioni "main" per effettuare nuovi test. 
Le dimensioni per i due problemi sono settate di default a:

- n_queens: 20 regine
- map_coloring: 10 stati

Le cartelle "others" di entrambi i progetti contengono diverse soluzioni ai suddetti problemi utilizzando tecniche meno efficienti (eccetto la tabu-search per n-queens) e altre soluzioni reperite online, qui di seguito le repository dei codici:

- n_queens -> others -> min_confllicts_alternative.py (reperito a: https://gist.github.com/vedantk/747203/revisions)
- n_queens -> others -> min_confllicts_alternative2.py (reperito a: https://github.com/calcelli/Min-Conflict-nQueens/blob/master/QueenSolver.py)

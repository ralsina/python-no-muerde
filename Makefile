DOC=libro.pdf

FIGURAS=dependencias.graph.pdf loop-n-y-medio.graph.pdf
CAPITULOS=1.txt 2.txt 3.txt 4.txt 5.txt 6.txt 7.txt 8.txt 9.txt 10.txt 11.txt 12.txt licencia.txt
LISTADOS=gaso1.py\
         gaso2.py\
         gaso3.py\
         buscaacento1.py

%.graph.pdf: %.dot
	dot -Tpdf $< > $@

libro.pdf: cover.tmpl indice.txt ${CAPITULOS} ${FIGURAS} Makefile estilo.style ${LISTADOS}
	rst2pdf -e inkscape -l es_ES -b1 --smart-quotes=1 -s eightpoint,bw,estilo indice.txt -o libro.pdf --custom-cover=cover.tmpl

commit:
	touch indice.txt ; make libro.pdf
	hg commit
	hg push

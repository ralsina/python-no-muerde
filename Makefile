DOC=libro.pdf

FIGURAS=dependencias.graph.pdf
CAPITULOS=1.txt 2.txt 3.txt 4.txt 5.txt 6.txt 7.txt 8.txt 9.txt 10.txt 11.txt 12.txt

%.graph.pdf: %.dot
	dot -Tpdf $< > $@

libro.pdf: indice.txt ${CAPITULOS} ${FIGURAS} Makefile estilo.style
	rst2pdf -l es -b1 --smart-quotes=1 -s eightpoint,bw,estilo indice.txt -o libro.pdf

commit:
	hg kwexpand
	touch indice.txt ; make libro.pdf
	hg kwshrink
	hg commit
	hg push

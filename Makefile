DOC=libro.pdf

FIGURAS=dependencias.graph.pdf
CAPITULOS=1.txt 2.txt 3.txt 4.txt 5.txt 6.txt 7.txt 8.txt 9.txt 10.txt 11.txt 12.txt

%.graph.pdf: %.dot
	dot -Tpdf $< > $@

libro.pdf: indice.txt ${CAPITULOS} ${FIGURAS} Makefile
	rst2pdf -b1 --smart-quotes=1 -s bw,estilo indice.txt -o libro.pdf


DOC=python_no_muerde.pdf

FIGURAS=dependencias.graph.pdf loop-n-y-medio.graph.pdf
FIGURAS_WEB=dependencias.graph.png loop-n-y-medio.graph.png
SCREENSHOTS=pyurl1-1.print.png\
	 pyurl2-1.print.png\
	 pyurl2-2.print.png\
	 pyurl2-3.print.png\
	 pyurl2-4.print.png

CAPITULOS=intro.txt 1.txt 2.txt 3.txt 4.txt 5.txt 6.txt 7.txt 8.txt 9.txt 10.txt 11.txt 12.txt licencia.txt gracias.txt
CAPITULOS_PDF=intro.pdf 1.pdf 2.pdf 3.pdf 4.pdf 5.pdf 6.pdf 7.pdf 8.pdf 9.pdf 10.pdf 11.pdf 12.pdf licencia.pdf gracias.pdf
LISTADOS=codigo/4/gaso1.py\
         codigo/4/gaso2.py\
         codigo/4/gaso3.py

%.graph.pdf: %.dot
	dot -Tpdf $< > $@

%.graph.png: %.dot
	dot -Tpng $< > $@

%.print.png: %.screen.png
	convert -resize 1500 $< $@

%.pdf: %.txt estilo.style Makefile tapa-capitulo.tmpl
	rst2pdf -e inkscape -l es_ES -b1 --smart-quotes=1 -s eightpoint,bw,estilo $< -o $@ --custom-cover=tapa-capitulo.tmpl

python_no_muerde.pdf: tapa.tmpl indice.txt ${CAPITULOS} ${FIGURAS} Makefile estilo.style ${LISTADOS} ${SCREENSHOTS}
	rst2pdf -e dotted_toc -e inkscape -l es_ES -b1 --smart-quotes=1 -s eightpoint,bw,estilo,tapa indice.txt -o python_no_muerde.pdf --custom-cover=tapa.tmpl

sitio: .phony ${FIGURAS_WEB} 
	(cd web ; ln -sf ../codigo .)
	(cd sitio ; ln -sf ../*.graph.png ../*.pdf ../*screen.png .)
	python r2w.py rst2web.ini
	(cd sitio; sed --in-place 's/graph\.pdf/graph\.png/g' *html)
	(cd sitio; sed --in-place 's/print\.png/screen\.png/g' *html)

commit: sitio
	touch indice.txt ; make python_no_muerde.pdf
	hg commit python_no_muerde.pdf -m "PDF actualizado"
	hg commit
	hg push
        rsync -rvL --delete sitio/* ralsina@lateral.netmanagers.com.ar:/srv/www/nomuerde

commit-web: sitio ${CAPITULOS_PDF}
	hg commit
	hg push
	rsync -rvL --delete sitio/* ralsina@lateral.netmanagers.com.ar:/srv/www/nomuerde

.phony:
	true

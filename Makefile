DOC=python_no_muerde.pdf

FIGURAS=dependencias.graph.pdf\
	 loop-n-y-medio.graph.pdf\
         middleware1.graph.pdf\
         middleware2.graph.pdf\
	 by.svg.pdf\
         cc.svg.pdf\
         cover.svg.pdf\
         nc.svg.pdf\
         remix.svg.pdf\
         sa.svg.pdf\
         share.svg.pdf\
         gaso3-api.pdf         

FIGURAS_WEB=dependencias.graph.png\
            loop-n-y-medio.graph.png\
            middleware1.graph.png\
            middleware2.graph.png\
	    by.svg.png\
            cc.svg.png\
            cover.svg.png\
            nc.svg.png\
            remix.svg.png\
            sa.svg.png\
            share.svg.png\
            gaso3-api.png

SCREENSHOTS=pyurl1-1.print.jpg\
	 pyurl2-1.print.jpg\
	 pyurl2-2.print.jpg\
	 pyurl2-3.print.jpg\
	 pyurl2-4.print.jpg\
	 pyurl3-1.print.jpg\
	 pyurl3-2.print.jpg\
	 pyurl3-3.print.jpg\
         pyurl-production.print.jpg\
         radio-1.print.jpg\
         radio-2.print.jpg\
         radio-3.print.jpg\
         radio-4.print.jpg\
         radio-5.print.jpg\
         radio-6.print.jpg\
         radio-7.print.jpg\
         radio-8.print.jpg\
         radio-9.print.jpg\
         radio-10.print.jpg\
         radio-11.print.jpg\
         radio-12.print.jpg\
         radio-13.print.jpg\
         radio-14.print.jpg\
         radio-15.print.jpg\
         radio-16.print.jpg\
         radio-17.print.jpg\
         radio-18.print.jpg\
         radio-19.print.jpg\
         radio-20.print.jpg\
         radio-21.print.jpg\
         radio-22.print.jpg\
         radio-23.print.jpg\
         radio-24.print.jpg\
         radio-25.print.jpg\
         linguist-1.print.jpg\
         linguist-2.print.jpg\
         linguist-3.print.jpg
       

CAPITULOS=intro.txt 1.txt 2.txt 3.txt 4.txt 5.txt 6.txt 7.txt 8.txt 9.txt 10.txt 11.txt 12.txt licencia.txt gracias.txt metalibro.txt
CAPITULOS_PDF=intro.pdf 1.pdf 2.pdf 3.pdf 4.pdf 5.pdf 6.pdf 7.pdf 8.pdf 9.pdf 10.pdf 11.pdf 12.pdf licencia.pdf gracias.pdf metalibro.pdf
LISTADOS=codigo/4/gaso1.py\
         codigo/4/gaso2.py\
         codigo/4/gaso3.py\
	 codigo/2/pyurl1.py\
	 codigo/2/pyurl2.py\
	 codigo/2/pyurl3.py\
	 codigo/2/views/usuario.tpl


%.print.jpg: %.screen.png
	convert -resize 1600 $< $@

%.svg.pdf: %.svg
	inkscape $< --export-pdf=$@ 

%.svg.png: %.svg
	inkscape $< --export-png=$@ 

%.pdf: %.txt estilo.style Makefile tapa-capitulo.tmpl
	rst2pdf -l es_ES -b0 --smart-quotes=1 -s eightpoint,bw,estilo $< -o $@ --custom-cover=tapa-capitulo.tmpl --fit-literal-mode=shrink --inline-footnotes --date-invariant

python_no_muerde.pdf: tapa.tmpl indice.txt ${CAPITULOS} ${FIGURAS} Makefile estilo.style ${LISTADOS} ${SCREENSHOTS}
	rst2pdf -l es_ES -b1 --smart-quotes=1 -s eightpoint,bw,estilo,tapa indice.txt -o python_no_muerde.pdf --custom-cover=tapa.tmpl --inline-footnotes --date-invariant

sitio: .phony ${FIGURAS_WEB} fuentes.zip ${CAPITULOS}
	(cd web ; ln -sf ../codigo .)
	(cd sitio ; ln -sf ../*.graph.png ../*.pdf ../*screen.png ../fuentes.zip ../*api.png ../concord.jpg .)
	(for C in ${CAPITULOS}; do touch -r $$C web/$$C ; done)
	python2 r2w.py rst2web.ini
	(cd sitio; sed --in-place 's/graph\.pdf/graph\.png/g' *html)
	(cd sitio; sed --in-place 's/print\.jpg/screen\.png/g' *html)
	(cd sitio; sed --in-place 's/api\.pdf/api\.png/g' *html)
	(cd sitio; sed --in-place 's/filenew\.pdf/filenew\.png/g' *html)

commit:
	touch indice.txt ; make python_no_muerde.pdf
	hg commit python_no_muerde.pdf -m "PDF actualizado"
	hg commit
	hg push
        rsync -rvL --delete sitio/* ralsina@lateral.netmanagers.com.ar:/srv/www/nomuerde

commit-web: sitio ${CAPITULOS_PDF}
	hg commit || true
	hg push
	rsync -rvL --delete sitio/* ralsina@lateral.netmanagers.com.ar:/srv/www/nomuerde

fuentes.zip: .phony
	find codigo -name "*~" -exec rm {} \;
	zip -r fuentes.zip codigo/ -x "codigo/2/nonces/*" "codigo/2/associations/*"\
	 "codigo/2/*sqlite" "*pyc" "*~" "temp" ".tox"

dependencias.graph.pdf: dependencias.dot
	neato -Tpdf $< > $@ -Efontname="DejaVu Sans" -Nfontname="DejaVu Sans"

dependencias.graph.png: dependencias.dot
	neato -Tpng $< > $@ -Efontname="DejaVu Sans" -Nfontname="DejaVu Sans"

middleware1.graph.pdf: middleware1.dot
	dot -Tpdf $< > $@ -Efontname="DejaVu Sans" -Nfontname="DejaVu Sans"

middleware1.graph.png: middleware1.dot
	dot -Tpng $< > $@ -Efontname="DejaVu Sans" -Nfontname="DejaVu Sans"

middleware2.graph.pdf: middleware2.dot
	dot -Tpdf $< > $@ -Efontname="DejaVu Sans" -Nfontname="DejaVu Sans"

middleware2.graph.png: middleware2.dot
	dot -Tpng $< > $@ -Efontname="DejaVu Sans" -Nfontname="DejaVu Sans"

%.graph.pdf: %.dot
	dot -Tpdf $< > $@ -Efontname="DejaVu Sans" -Nfontname="DejaVu Sans"

%.graph.png: %.dot
	dot -Tpng $< > $@ -Efontname="DejaVu Sans" -Nfontname="DejaVu Sans"

.phony:
	true

2.pdf: 2.txt estilo.style codigo/2/pyurl1.py\
       codigo/2/pyurl2.py codigo/2/pyurl3.py\
       codigo/2/views/atajo.tpl\
       codigo/2/views/usuario.tpl\
       pyurl-production.print.jpg\

1.pdf: 1.txt estilo.style codigo/1/deco1.py\
       codigo/1/deco2.py \
       codigo/1/deco.py \
       codigo/1/esnumero.py \
       codigo/1/singleton1.py

4.pdf: 4.txt estilo.style \
	codigo/4/gaso1.py \
	codigo/4/gaso2.py \
	codigo/4/gaso3.py \
	codigo/4/gaso4.py \
	codigo/4/mock1.py \
	codigo/4/mock2.py \
        codigo/4/req.txt \
        codigo/4/tox.ini \
        codigo/4/setup.py\
        codigo/4/jack1.py\
        codigo/4/jack2.py\
        codigo/4/jack3.py


5.pdf: 5.txt\
       radio-1.print.jpg\
       radio-2.print.jpg\
       radio-3.print.jpg\
       radio-4.print.jpg\
       radio-5.print.jpg\
       radio-6.print.jpg\
       radio-7.print.jpg\
       radio-8.print.jpg\
       radio-9.print.jpg\
       radio-10.print.jpg\
       radio-11.print.jpg\
       radio-12.print.jpg\
       radio-13.print.jpg\
       codigo/5/radio1.py\
       codigo/5/radio2.py\
       codigo/5/radio3.py\
       codigo/5/radio4.py\
       codigo/5/plsparser.py

6.pdf: 6.txt\
       concord.jpg\
       radio-14.print.jpg\
       radio-15.print.jpg\
       radio-16.print.jpg\
       radio-17.print.jpg\
       radio-18.print.jpg\
       radio-19.print.jpg\
       radio-20.print.jpg\
       radio-21.print.jpg\
       radio-22.print.jpg\
       radio-23.print.jpg\
       radio-24.print.jpg\
       radio-25.print.jpg\
       filenew.svg\
       codigo/6/radio6.py\
       codigo/6/radio7.py\
       codigo/6/radio8.py\
       codigo/6/radio9.py\
       codigo/6/radio_es.ts\
       codigo/6/Makefile\
       linguist-1.print.jpg\
       linguist-2.print.jpg\
       linguist-3.print.jpg


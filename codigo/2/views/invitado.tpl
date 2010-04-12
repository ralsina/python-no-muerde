<html>
<head>
    <title>Bienvenido a PyURL</title>
    <link rel="stylesheet" href="/static/screen.css" type="text/css" media="screen, projection">
    <link rel="stylesheet" href="/static/print.css" type="text/css" media="print">
    <!--[if IE]>
        <link rel="stylesheet" href="/static/ie.css" type="text/css" media="screen, projection">
    <![endif]-->
    <link rel="stylesheet" href="/static/style.css" type="text/css" media="screen, projection">
</head>
<body style="width: 768px; margin: auto auto auto auto; font-size: 10pt;">
<div style="text-align: center; ">
<h1 class="thin">PyURL - Acorta URLs</h1>
<hr>
</div>
<p>PyURL es un servicio de inmortalizaci&oacute;n de URLs. Es parecido a un
acortador, pero con algunas diferencias:</p>

<ul>
<li> Permite cambiar el destino del atajo.
<li> Avisa si la p&aacute;gina deja de funcionar.
</ul>

<p>Para poder utilizar este servicio, debe autenticarse. No hace falta
abrir una cuenta, utilice cualquier proveedor OpenID.</p>

<div class="$css_class">$message</div>

    <form action="$action" method="post">
    <fieldset>
        Su URL de identificaci&oacute;n OpenID:
        <input type="text" name="openid" value="$value">
      <button type="button positive" style="float right;">Ingresar</button>
    </fieldset>
    </form>
<!-- Falta agregar botones para yahoo/google -->
</body>
</html>

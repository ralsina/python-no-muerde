<html>
<head>
    <title>Bienvenido a PyURL</title>
    <link rel="stylesheet" href="/static/screen.css" type="text/css" media="screen, projection">
    <link rel="stylesheet" href="/static/print.css" type="text/css" media="print">
    <!--[if IE]>
        <link rel="stylesheet" href="/static/ie.css" type="text/css" media="screen, projection">
    <![endif]-->
    <link rel="stylesheet" href="/static/style.css" type="text/css" media="screen, projection">

	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
	<!-- Simple OpenID Selector -->
	<link type="text/css" rel="stylesheet" href="static/css/openid.css" />
	<script type="text/javascript" src="static/js/jquery-1.2.6.min.js"></script>
	<script type="text/javascript" src="static/js/openid-jquery.js"></script>
	<script type="text/javascript" src="static/js/openid-en.js"></script>
        <script type="text/javascript">
                $$(document).ready(function() {
                        openid.init('openid');
                });
        </script>
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
<div>
    <form action="$action" method="post" id="openid_form">
<input type="hidden" name="action" value="verify" />

    <fieldset style="border: 0px;">
	<div id="openid_input_area">
 <input id="openid" name="openid" type="text" value="$value" />
                                <input id="openid_submit" type="submit" value="Sign-In"/>
	</div>
			<div id="openid_choice">
				<p>Entrar usando:</p>
				<div id="openid_btns"></div>
			</div>
			<noscript>
				<p>OpenID is service that allows you to log-on to many different websites using a single indentity.
				Find out <a href="http://openid.net/what/">more about OpenID</a> and <a href="http://openid.net/get/">how to get an OpenID enabled account</a>.</p>
			</noscript>
    </fieldset>
    </form>
</div>
</body>
</html>







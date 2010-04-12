<html>
<head>
    <link rel="stylesheet" href="/static/screen.css" type="text/css" media="screen, projection">
    <link rel="stylesheet" href="/static/print.css" type="text/css" media="print">
    <!--[if IE]>
        <link rel="stylesheet" href="/css/ie.css" type="text/css" media="screen, projection">
    <![endif]-->
    <link rel="stylesheet" href="/css/style.css" type="text/css" media="screen, projection">
</head>
<body style="width: 768px; margin: auto auto auto auto; font-size: 10pt;">

<div style="text-align: center; margin-bottom: 16px;">
    <h1 class="thin">PyURL - Acorta URLs</h1>
    %if mensaje:
        <p class="{{clasemensaje}}">
        {{!mensaje}}
        </p>
    %end
    <h2>Propiedades del atajo {{atajo.slug()}}</h2>

<form method="POST">
<fieldset style="width:650px; text-align:left;">
    <div>
        <label for="url">URL:</label><br/>
        <input type="text" id="url" name="url" size=80 value="{{atajo.url}}">
    </div>
    <div>
        <label for="activo">Activo:</label><br/>
        <input type="checkbox" id="activo" name="activo" value="{{atajo.activo}}">
    </div>
    <div>
        <label for="test">Test:</label><br/>
        <textarea name="test" rows=15 cols=80>
{{atajo.test}}
        </textarea>
    </div>
        <button class="button positive">Guardar</button>
</fieldset>
</form>
<div style="clear: both; text-align: center;">
    <a href="/logout">Cerrar sesión</a>
</div>
</div>
</body>
</html>
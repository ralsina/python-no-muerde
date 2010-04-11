<html>
<head>
    <link rel="stylesheet" href="/static/screen.css" type="text/css" media="screen, projection">
    <link rel="stylesheet" href="/static/print.css" type="text/css" media="print">
    <!--[if IE]>
        <link rel="stylesheet" href="/css/ie.css" type="text/css" media="screen, projection">
    <![endif]-->
    <link rel="stylesheet" href="/css/style.css" type="text/css" media="screen, projection">
</head>
<body style="width: 768px; margin: auto auto auto auto;">
<div>
Bienvenido a PyURL! - <a href="/logout">Cerrar sesión</a>
</div>
<div style="text-align: center;">
<h1 class="thin">PyURL - Acorta URLs</h1>
<hr>

%if mensaje:
    <p class="{{clasemensaje}}">
    <!-- Que no escape los <> del mensaje -->
    {{!mensaje}}
    </p>
%end
<form>
    URL a acortar:&nbsp;
    <input type="text" name="url">
    <input type="submit" class="button positive">
</form>
</div>
<table>
    <th>Atajo
    <th>Acciones
    </th>
% for atajo in atajos:
    <tr>
    <td><a href="{{atajo.url}}">{{atajo.slug()}}</a>
    <td><a href="/{{atajo.slug()}}/edit">Editar</a>
        <a href="/{{atajo.slug()}}/del">Eliminar</a>
        <a href="/{{atajo.slug()}}/test">Probar</a>
%end
</table>

</body>
</html>
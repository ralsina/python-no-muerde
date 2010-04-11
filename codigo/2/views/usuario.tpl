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
</div>

<div style="float: left; text-align: right; width: 350px;">
    <form>
        URL a acortar:&nbsp;
        <input type="text" name="url">
        <input type="submit" class="button positive">
    </form>
    <a href="/logout">Cerrar sesión</a>
</div>

<div style="float:right;text-align: left; width: 350px;">
    <table>
        <th>Atajo
        <th>Acciones
        </th>
        % for atajo in atajos:
            <tr>
            <td><a href="{{atajo.url}}">{{atajo.slug()}}</a>
            <td><a href="/{{atajo.slug()}}/edit">Editar</a>&nbsp;/&nbsp;
                <a href="/{{atajo.slug()}}/del">Eliminar</a>&nbsp;/&nbsp;
                <a href="/{{atajo.slug()}}/test">Probar</a>
        %end
    </table>
</div>
</body>
</html>

<html>
<head>
    <link rel="stylesheet" href="/static/screen.css" type="text/css" media="screen, projection">
    <link rel="stylesheet" href="/static/print.css" type="text/css" media="print">
    <!--[if IE]>
        <link rel="stylesheet" href="/css/ie.css" type="text/css" media="screen, projection">
    <![endif]-->
    <link rel="stylesheet" href="/css/style.css" type="text/css" media="screen, projection">
</head>
<body style="text-align: center; width: 768px; margin: auto auto auto auto;">
<div>
Bienvenido a PyURL! - <a href="/logout">Cerrar sesión</a>
</div>
<h1 class="thin">PyURL - Acorta URLs</h1>
<hr>

%if url:
    <p class="success">
    La URL <a href="{{url}}">{{url}}</a> se convirtió en:
    <a href="{{baseurl}}{{short}}">{{baseurl}}{{short}}</a>
    </p>
%end
<form>
    URL a acortar:&nbsp;
    <input type="text" name="url">
    <input type="submit" class="button positive">
</form>

<ul>
% for atajo in atajos:
    <li><a href="{{atajo.url}}">{{atajo.slug()}}</a><a href="/{{atajo.slug())}}/edit">Editar</a></li>
%end
</ul>

</body>
</html>
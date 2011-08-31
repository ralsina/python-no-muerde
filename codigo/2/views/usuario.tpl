<html>
<head>
    <link rel="stylesheet" href="/static/screen.css" type="text/css" media="screen, projection">
    <link rel="stylesheet" href="/static/print.css" type="text/css" media="print">
    <!--[if IE]>
        <link rel="stylesheet" href="/static/ie.css" type="text/css" media="screen, projection">
    <![endif]-->
    <link rel="stylesheet" href="/static/style.css" type="text/css" media="screen, projection">
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

<div style="float: right; text-align: left; width: 350px;">
    <form method="POST">
    <fieldset>
        <legend>Crear nuevo atajo:</legend>
        <div>
        <label for="url">URL a acortar:</label>
        <input type="text" name="url" id="url"></div>
        <button class="button positive">Crear</button>
    </fieldset>
    </form>
</div>

<div style="float:left;text-align: right; width: 350px;">
 <table style="width:100%;">
  <caption>Atajos Existentes</caption>
   <thead>
    <tr> <th>Atajo</th> <th>Acciones</th> </tr>
   </thead>
   % for atajo in atajos:
    <tr>
     % if atajo.status:
      <td><img src="/static/weather-clear.png" alt="Success"
        align="MIDDLE"/>
      <a href="{{atajo.url}}">{{atajo.slug()}}</a>
     % else:
      <td><img src="/static/weather-storm.png" alt="Failure"
        align="MIDDLE"/>
      <a href="{{atajo.url}}">{{atajo.slug()}}</a>
     % end
     <td><a href="/{{atajo.slug()}}/edit">Editar</a>&nbsp;/&nbsp;
     <a href="/{{atajo.slug()}}/del">Eliminar</a>&nbsp;/&nbsp;
     <a href="/{{atajo.slug()}}/test">Probar</a>
    </tr>
   %end
 </table>
</div>
<div style="clear: both;text-align: center;"">
    <a href="/logout">Cerrar sesión</a>
</div>
</body>
</html>

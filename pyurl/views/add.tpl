<html>
<head>
    <link rel="stylesheet" href="/css/screen.css" type="text/css" media="screen, projection">
    <link rel="stylesheet" href="/css/print.css" type="text/css" media="print">
    <!--[if IE]>
        <link rel="stylesheet" href="/css/ie.css" type="text/css" media="screen, projection">
    <![endif]-->
    <link rel="stylesheet" href="/css/style.css" type="text/css" media="screen, projection">
</head>
<body style="text-align: center; width: 768px; margin: auto auto auto auto;">
<h1 class="thin">PyURL - Acorta URLs</h1>
%if url:
<p class="success">
La URL <a href="{{url}}">{{url}}</a> se convirtió en:
<a href="{{baseurl}}{{short}}">{{baseurl}}{{short}}</a>
</p>
%end
<hr>
<form>
URL a acortar:&nbsp;
<input type="text" name="url">
<input type="submit" class="button positive">
</form>
</body>
</html>
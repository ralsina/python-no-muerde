<html>
<head>
</head>
<body>

%if url:
La URL {{url}} se convirtió en: {{baseurl}}{{short}}
%end

<form>
URL a acortar:<br>
<input type="text" name="url">
<input type="submit">
</form>
</body>
</html>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta http-equiv="refresh" content="5; url=01it.html" />
<title>test per PARI</title>

<link rel="stylesheet" href="bootstrap.min.css"  crossorigin="anonymous">
<link rel="stylesheet" href="stile_ch.css">
<script type='text/javascript' src='jquery.min.js'>
</script>
</head>
<script type="text/javascript">
	
	$('input[name=pianto]').change(function(){
     $('form').submit();

});

	$("#pianto").change(function(){
alert("test");
});
</script>

<?php


 //Query 
$DB_host     = 'localhost';
$DB_user     = 'root';
$DB_password = '';
$DB_name     = 'pari';
$link = mysqli_connect('localhost', 'root', '', 'pari');
$codice = $_POST['codice'];
$cmaius = strtoupper($codice);
$max = strlen($codice);
if ( $max != 4)
{
 echo $max;
 header("Location: index.php");
}


$code = mysqli_real_escape_string($link, $codice);
list($genere, $eta) = explode("2", $code, 2);

if ($genere==1) {
  $genere="maschio";
}
else if ($genere==0){
  $genere="femmina";
}
else if ($eta==06){
  $eta="6 anni";
}
else if ($eta==08){
  $eta="8 anni";
}
else if ($eta==10){
  $eta="10 anni";
}




// Check connection
if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }


$query2 = "INSERT INTO utente (`genere`, `eta`, `tempo`, `note`) VALUES ('$genere', '$eta', '', 'ok');";
$result2 = mysqli_query($link,$query2);
if (!$result2) {
    die("Errore nella query $query2: " . mysqli_error());}
  else {

  }







?>


<body id="main_body" >
<a href="01it.html"><img src="images/02.jpg"  border="0"></a>

</map>
</body>

</html>
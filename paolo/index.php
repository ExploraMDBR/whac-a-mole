<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta name="viewport" content="width=device-width, user-scalable=no">
<meta http-equiv="refresh" content="3; url=index.php" />
<title>Immagini</title>

<link rel="stylesheet" href="bootstrap.min.css"  crossorigin="anonymous">
<link rel="stylesheet" href="stile_ch.css">
<script type='text/javascript' src='jquery.min.js'>
</script>

</head>
<script type="text/javascript">
window.onload=function(){
document.forms[0].codice.focus(); 
}
</script>




	<body id="main_body" >
		<img src="images/01.jpg" usemap="#Map" border="0">
        <map name="Map" id="Map">
          <area shape="rect" coords="81,1689,280,1884" href="en/index.php" />
        </map>
<div id="codices">
  <form action="conferma.php" method="post" name="fcodice">
<label for="codice"></label>
<input type="text" name="codice" id="codice"  placeholder="Scrivi qui il codice segreto"  style="position: absolute; left: -1200px"  required/>
</form>
</div>


</body>

</html>
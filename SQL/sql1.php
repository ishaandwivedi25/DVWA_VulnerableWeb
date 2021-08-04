<!DOCTYPE html>
<html>

<head>
	<title>SQL Injection</title>
	<link rel="shortcut icon" href="../Resources/hmbct.png" />
	<style>
		button {
			background-color: lightyellow;
			border-radius: 0px;
			font-size: large;
			margin: 5px;
			padding: 5px;
		}
	</style>
</head>

<body bgcolor="#ffffff" style="margin: 0; padding: 0; box-sizing: border-box; ">
	<link rel="stylesheet" href="Resources/button.css">
	<div style="background-color:lightcoral;padding:15px;">
		<button type="button" name="homeButton" onclick="location.href='../homepage.html';">Home Page</button>
		<button type="button" name="mainButton" onclick="location.href='sqlmainpage.html';">Main Page</button>
	</div>

	<div style="padding:20px;" align="center">
		<form action="<?php $_SERVER['PHP_SELF']; ?>" method="post">
			<p>John -> Doe</p>
			First name : <input type="text" name="firstname">
			<input type="submit" name="submit" value="Submit">
		</form>
	</div>


	<?php
	$servername = "localhost";
	$username = "root";
	$password = "";
	$db = "1ccb8097d0e9ce9f154608be60224c7c";

	// Create connection
	$conn = mysqli_connect($servername, $username, $password, $db);

	// Check connection
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
	//echo "Connected successfully";

	if (isset($_POST["submit"])) {
		$firstname = $_POST["firstname"];
		$sql = "SELECT lastname FROM users WHERE firstname='$firstname'"; //String
		$result = mysqli_query($conn, $sql);

		if (mysqli_num_rows($result) > 0) {
			// output data of each row
			while ($row = mysqli_fetch_assoc($result)) {
				echo $row["lastname"];
				echo "<br>";
			}
		} else {
			echo "0 results";
		}
	}

	?>
</body>

</html>
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

	<div style="background-color:lightcoral;padding:15px;">
		<button type="button" name="homeButton" onclick="location.href='../homepage.html';">Home Page</button>
		<button type="button" name="mainButton" onclick="location.href='sqlmainpage.html';">Main Page</button>
	</div>

	<div style="padding:20px;" align="center">
		<form action="<?php $_SERVER['PHP_SELF']; ?>" method="post">
			<p>Give me book's number and I give you book's name in my library.</p>
			Book's number : <input type="text" name="number">
			<input type="submit" name="submit" value="Submit">
			<!--<p>Im learning something, I think?
		    I will sanitize query this time!!
		    //I'm the best web developer.
		     //number is too dangerous. I have to do something.</p>
		-->
		</form>
	</div>

	<?php
	$servername = "localhost";
	$username = "root";
	$password = "";
	$db = "1ccb8097d0e9ce9f154608be60224c7c";

	// Create connection
	$conn = new mysqli($servername, $username, $password, $db);

	// Check connection
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	}
	//echo "Connected successfully";
	if (isset($_POST["submit"])) {
		$number = $_POST['number'];
		//I'm the best web developer.
		//number is too dangerous. I have to do something.
		if (strchr($number, "'")) {
			echo "Please Stop Trying to hack me!<br>";

			exit;
		}

		$query = "SELECT bookname,authorname FROM books WHERE number = $number";
		$result = mysqli_query($conn, $query);

		if (!$result) { //Check result
			$message  = 'Invalid query: ' . mysql_error() . "\n";
			$message .= 'Whole query: ' . $query;
			die($message);
		}

		while ($row = mysqli_fetch_assoc($result)) {
			echo "<hr>";
			echo $row['bookname'] . " ----> " . $row['authorname'];
		}

		if (mysqli_num_rows($result) <= 0)
			echo "0 result";
	}
	?>

</body>

</html>
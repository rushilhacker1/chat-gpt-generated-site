<?php
require 'autoload.php';
require 'automailer/PHPMailer.php';
require 'automailer/Exception.php';
require 'automailer/SMTP.php';


use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// Get the form fields, removes whitespace and newlines
$name = strip_tags(trim($_POST["name"]));
$name = str_replace(array("\r","\n"),array(" "," "),$name);
$email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
$message = trim($_POST["message"]);

// Set the recipient email address
$to = "rushiling121@hotmail.com, rushiling121@gmail.com, rushiling123@gmail.com";

// Set the email subject
$subject = "New message from $name";

// Build the email content
$email_content = "Name: $name\n";
$email_content .= "Email: $email\n\n";
$email_content .= "Message:\n$message\n";

// Send the email using SMTP with STARTTLS
$mail = new PHPMailer(true);
try {
    //Server settings
    $mail->SMTPDebug = 0;
    $mail->isSMTP();
    $mail->SMTPAuth = true;
    $mail->Username = 'rushiling121@hotmail.com';
    $mail->Password = 'ankurrushil1';
    $mail->SMTPSecure = 'tls';

    //Recipients
    $mail->setFrom($email, $name);
    $mail->addAddress('rushiling121@hotmail.com');
    $mail->addAddress('rushiling121@gmail.com');
    $mail->addAddress('rushiling123@gmail.com');

    //Content
    $mail->isHTML(false);
    $mail->Subject = $subject;
    $mail->Body = $email_content;

    $mail->send();
} catch (Exception $e) {
    // Error handling
}

// Send SMS notification using Twilio
require_once 'autoload.php';

use Twilio\Rest\Client;

$sms_body = "You have received a new message from $name: $message";

$account_sid = 'AC76e6123ec8d3545780747792691c05fa';
$auth_token = '398c6baa357299b61b24628390bbb949';
$twilio_number = 'YOUR_TWILIO_PHONE_NUMBER';
$recipient_number = '8104314282';

$client = new Client($account_sid, $auth_token);
$message = $client->messages->create(
    $recipient_number,
    array(
        'from' => $twilio_number,
        'body' => $sms_body
    )
);

// Redirect back to the contact page
header("Location: contact.php?success=true");
?>```

Remember to replace the placeholders with your actual credentials before using it.

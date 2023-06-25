<?php

if (isset($_POST["senha"]) && isset($_POST["email"])) {
    $email = $_POST['email'];
    $senha = $_POST['senha'];

    if ($email == "leonardo@gmail.com" && $senha == "senha123") {
        echo json_encode(['status' => 'sucess', 'message' => "../index.html"]);
        
    } else {
        echo json_encode(['status' => 'error', 'message' => "errado"]);
       
    }
}
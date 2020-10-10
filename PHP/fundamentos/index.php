<?php
    
    //For Básico
    for ($i = 0; $i < 15;) {
        $i++;
        if($i == $i ) 
            echo 'Número: ' . $i .'<br/>';
        else break;
    } echo "Laço finalizado";

    // While Básico
    $i = 0;
    while($i != 10){
        $i++;
        echo "<h1>'$i'</h1>";
    };

    // For para vetores
    $pessoas = array('Oscar', 'Nana', 'Neguinho', 'Dinorá');
    foreach($pessoas as $index => $pessoa){
        echo "<h2> Índice: '$index'</h2> \n";
        echo "<h2> Nome: '$pessoa' </h2> \n";
    };

    //Matriz 
    $empresas = array();

    array_push($empresas, array(
        "nome" => "OscarEnterprise",
        "cnpj" => "071673216354653",
        array('teste' => 'dasdasd'),
        array('teste1' => 'dasdasasdasdasdd')
    ));

    print_r($empresas[0][1]['teste1']);

?>

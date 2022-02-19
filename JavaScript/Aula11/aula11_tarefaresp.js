// --------------------------------------------------
// Cria o banco de dados
// --------------------------------------------------
var bd = openDatabase("bdTarefas","1.0","Tarefas",2*1024*1024);
// --------------------------------------------------
// Cria a tabela de objetos e cores no banco de dados
// --------------------------------------------------
bd.transaction( function(tr) {
    var comandoSQL = 'CREATE TABLE IF NOT EXISTS '+
                        'Tarefas (tarefas)';
    tr.executeSql(comandoSQL);
});
exibirBD();

// --------------------------------------------------
// Insere novo objeto e cor 
// na tabela do banco de dados
// --------------------------------------------------
function incluir() {
    var tarefa = document.getElementById("novatarefa").value;
    if(tarefa != "") {
        bd.transaction( function(tr) {
            var comandoSQL = 
                'INSERT INTO Objetos (tarefa) VALUES (?)';
            tr.executeSql(comandoSQL,[tarefa]);
        });
        exibirBD();
     } else {
        alert("Informe a tarefa!");
    }
}
// --------------------------------------------------
// Exibe todos os registros  
// existentes na tabela
// --------------------------------------------------
function exibirBD() {
    // esvazia o <div>
    document.getElementById("conteudo").innerHTML = "";
    // formato: bd.transaction(function(transacao){ comandos });
    bd.transaction( function(tr) {        
        // recupera os dados
        var comandoSQL = 'SELECT * FROM Tarefas';
        // formato: tr.executeSQL( cmdSQL,[param],func_tratamento_dados);
        tr.executeSql(comandoSQL, [],
            function(tr, resultados) {
                var qtd = resultados.rows.length;
                var linhaTab;
                var resp = "<table>";
                for (let i=0;i<qtd;i++) {
                    linhaTab = resultados.rows.item(i);
                    resp +=  "<td>"+(i+1)+"</td>";
                    resp +=  "<td>"+linhaTab.tarefa+"</td>";
                    resp +=  "</tr>";
                };
                resp += "</table>";
                document.getElementById("conteudo").innerHTML = 
                        resp;
                },console.log('Executou SELECT'));
    });
}
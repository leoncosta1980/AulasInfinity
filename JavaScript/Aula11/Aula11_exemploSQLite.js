// --------------------------------------------------
// Cria o banco de dados
// --------------------------------------------------
var bd = openDatabase("bdObjetos","1.0","Objetos e cores",2*1024*1024);
// --------------------------------------------------
// Cria a tabela de objetos e cores no banco de dados
// --------------------------------------------------
bd.transaction( function(tr) {
    var comandoSQL = 'CREATE TABLE IF NOT EXISTS '+
                        'Objetos (nomeObj, corObj)';
    tr.executeSql(comandoSQL);
});
exibirBD();

// --------------------------------------------------
// Insere novo objeto e cor 
// na tabela do banco de dados
// --------------------------------------------------
function inserir() {
    var nomeObj = document.getElementById("formNome").value;
    var corObj = document.getElementById("formCor").value;
    if((nomeObj != "") & (corObj != "")) {
        bd.transaction( function(tr) {
            var comandoSQL = 
                'INSERT INTO Objetos (nomeObj, corObj) VALUES (?,?)';
            tr.executeSql(comandoSQL,[nomeObj,corObj]);
        });
        exibirBD();
    } else {
        alert("Informe o nome do objeto e sua cor!");
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
        var comandoSQL = 'SELECT * FROM Objetos';
        // formato: tr.executeSQL( cmdSQL,[param],func_tratamento_dados);
        tr.executeSql(comandoSQL, [],
            function(tr, resultados) {
                var qtd = resultados.rows.length;
                var linhaTab;
                var resp = "<table>";
                for (let i=0;i<qtd;i++) {
                    linhaTab = resultados.rows.item(i);
                    resp +=  "<td>"+(i+1)+"</td>";
                    resp +=  "<td>"+linhaTab.nomeObj+"</td>";
                    resp +=  "<td>"+linhaTab.corObj+"</td>";
                    resp +=  "</tr>";
                };
                resp += "</table>";
                document.getElementById("conteudo").innerHTML = 
                        resp;
                },console.log('Executou SELECT'));
    });
}

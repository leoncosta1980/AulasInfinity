// --------------------------------------------------
// Cria o banco de dados
// --------------------------------------------------
var bd = openDatabase("bdTarefas","1.0","Banco de dados de tarefas",2*1024*1024);

// --------------------------------------------------
// Cria a tabela de objetos e cores no banco de dados>>>>>>>
// --------------------------------------------------
bd.transaction( function(tr) {
    // var comandoSQL = 'drop TABLE Tarefas';
    // tr.executeSql(comandoSQL);
    var comandoSQL = 'CREATE TABLE IF NOT EXISTS '+
                        'Tarefas(descTrf);';
    tr.executeSql(comandoSQL);
});
exibir();

function exibir(){
    document.getElementById("conteudo").innerHTML="";

    bd.transaction( function(tr) {
        var comandoSQL = 'SELECT rowid, descTrf FROM Tarefas;';
        tr.executeSql(comandoSQL,[], function (tr,resposta) {
            var saida = document.getElementById("conteudo");
            var qtdLinhas = resposta.rows.length;
            for (let i=0;i<qtdLinhas;i++) {
                let rowid = resposta.rows.item(i).rowid;
                let trf = resposta.rows.item(i).descTrf;
                saida.innerHTML += "<div class='item'>"+
                    "<input type='checkbox'>"+
                    "<div>" + trf + "</div>"+
                    "<button onclick=excluir("+rowid+ ")>X</button>"+
                    "</div>";
                };
        });
    });
}

function incluir(){
console.log("incluindo...");
    var descTarefa = document.getElementById("desc");
    bd.transaction( function(tr) {
        var comandoSQL = 'INSERT INTO Tarefas(descTrf) VALUES(?);';
        tr.executeSql(comandoSQL,[descTarefa.value]);
        descTarefa.value = "";
    });
    exibir();
}

function excluir(tarefa){
console.log(tarefa);
    var comandoSQL = 'DELETE FROM Tarefas WHERE rowid=?;';    
    bd.transaction( function(tr) {
        tr.executeSql(comandoSQL,[tarefa]);
    });
    exibir();
}
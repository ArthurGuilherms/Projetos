function pesquisar() {
    let section = document.getElementById("resultados-pesquisa");

    let resultados = ""

    //Para cada dadod dentro da lista de dados:
    for (let dado of dados) {
        resultados += `
    <div class="item-resultado">
                    <h2>
                        <a href="#" target="_blank">${dado.nome}</a>
                    </h2>
                    <p class="descricao-meta">${dado.descricao}</p>
                    <a href="${dado.siteOficial}" target="_blank">Site Oficial</a>
                </div> 
    `
    }

section.innerHTML = resultados

}
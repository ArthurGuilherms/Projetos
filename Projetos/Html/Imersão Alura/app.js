function pesquisar() {
    // Obtém a seção HTML onde os resultados serão exibidos
    let section = document.getElementById("resultados-pesquisa");

    // Inicializa uma string vazia para armazenar os resultados da pesquisa
    let resultados = "";

    // Flag para indicar se algum resultado foi encontrado
    let encontrouResultados = false;

    // Obtém o valor do campo de pesquisa
    let campoPesquisa = document.getElementById("campo-pesquisa").value;

    // Itera sobre cada dado na lista da array dados
    for (let dado of dados) {
        // Se o campo de pesquisa estiver vazio, exibe uma mensagem e retorna da função
        if (!campoPesquisa) {
            section.innerHTML = "<p>Nenhum jogo encontrado.</p>";
            return;
        }

        // Converte o valor do campo de pesquisa para minúsculas para facilitar a comparação
        campoPesquisa = campoPesquisa.toLowerCase();

        // Verifica se o nome ou a tag do dado contém o termo de pesquisa (em minúsculas)
        if (dado.nome.toLowerCase().includes(campoPesquisa.toLowerCase()) || dado.tag.toLowerCase().includes(campoPesquisa.toLowerCase())) {
            // Se encontrou um resultado, atualiza a flag e adiciona o resultado à string de resultados
            encontrouResultados = true;
            resultados += `
                <div class="item-resultado">
                    <h2>
                        <a href="#" target="_blank">${dado.nome}</a>
                    </h2>
                    <p class="descricao-meta">${dado.descricao}</p>
                    <a href="${dado.siteOficial}" target="_blank">Site Oficial</a>
                </div> 
            `;
        }
    }

    // Se nada for encontrado na pesquisa, exibe uma mensagem e retorna da função
    if (encontrouResultados == false) {
        section.innerHTML = "<p>Nenhum jogo encontrado.</p>";
            return;
    }

    // Atualiza o conteúdo da seção com os resultados da pesquisa
    section.innerHTML = resultados;
}
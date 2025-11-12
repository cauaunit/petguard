document.addEventListener("DOMContentLoaded", () => {
    fetch("/api/animais/")
        .then(response => {
            if (!response.ok) throw new Error("Erro ao buscar animais");
            return response.json();
        })
        .then(animais => {
            const corpo = document.getElementById("animalList");
            corpo.innerHTML = "";

            animais.forEach(animal => {
                corpo.innerHTML += `
                    <tr>
                        <td>${animal.especie}</td>
                        <td>${animal.raca}</td>
                        <td>${animal.idade}</td>
                        <td>${animal.status}</td>
                        <td>
                            <a href="/add_animal/${animal.id}/">
                                <button class="btn-editar">Editar</button>
                            </a>
                        </td>
                    </tr>
                `;
            });
        })
        .catch(error => console.error(error));
});


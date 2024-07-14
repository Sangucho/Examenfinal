document.addEventListener("DOMContentLoaded", function() {
    fetch('http://127.0.0.1:8000/api/productos')
        .then(response => response.json())
        .then(data => {
            const productosDiv = document.getElementById('container_productos');
            data.forEach(producto => {
                const productoDiv = document.createElement('div');
                productoDiv.innerHTML = `
                
                    <div class="card">
                        <img src="${producto.imagen}" alt="${producto.nombreart}">
                        <h2>${producto.nombreart}</h2>
                    <p>Marca: ${producto.marca}</p>
                    <p>Descripción: ${producto.descripcion}</p>
                    <p>Precio: $${producto.precio}</p>
                    <p>Stock: ${producto.stock}</p>
                    </div>
                `;
                productosDiv.appendChild(productoDiv);
            });
        })
        .catch(error => console.error('Error:', error));
});
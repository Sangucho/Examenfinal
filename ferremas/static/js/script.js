// script.js

document.addEventListener("DOMContentLoaded", function() {
  // Función para agregar un producto al carrito
  function addToCart() {
    const cart = document.getElementById('cart');
    let itemCount = parseInt(cart.textContent.match(/\d+/)[0]);
    itemCount++;
    cart.textContent = `Carrito (${itemCount})`;
  }
  
  // Event listeners para los botones de agregar al carrito
  const addToCartButtons = document.querySelectorAll('.addToCartBtn');
  addToCartButtons.forEach(button => {
    button.addEventListener('click', addToCart);
  });

  // Event listener para el botón del icono del usuario
  const userBtn = document.getElementById('userBtn');
  const userDropdown = document.getElementById('userDropdown');

  userBtn.addEventListener('click', function() {
    toggleDropdown(userDropdown);
  });

  // Ocultar el menú del usuario cuando se hace clic en cualquier lugar fuera de él
  document.addEventListener('click', function(event) {
    if (!userBtn.contains(event.target) && !userDropdown.contains(event.target)) {
      hideDropdown(userDropdown);
    }
  });

  // Función para alternar la visibilidad del menú desplegable
  function toggleDropdown(dropdown) {
    dropdown.style.display = (dropdown.style.display === 'block') ? 'none' : 'block';
  }

  // Función para ocultar el menú desplegable
  function hideDropdown(dropdown) {
    dropdown.style.display = 'none';
  }
  
  // Ocultar el menú del usuario al cargar la página
  hideDropdown(userDropdown);

  $('.slick-carousel').slick({
    autoplay: true, // Activar la reproducción automática
    autoplaySpeed: 2000, // Cambiar de imagen cada 4 segundos
    infinite: true, // Permitir que el carrusel se repita infinitamente
    fade: true, // Utilizar efecto de fundido entre las imágenes (opcional)
    cssEase: 'linear' // Tipo de transición entre las imágenes (opcional)
  });
  
});
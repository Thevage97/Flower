// Agregar interactividad al ramo de flores
const flowers = document.querySelectorAll('.flower');

flowers.forEach((flower) => {
  flower.addEventListener('mouseover', () => {
    // Animar la flor cuando se pasa el mouse sobre ella
    flower.classList.add('animated');
  });

  flower.addEventListener('mouseout', () => {
    // Quitar la animación cuando se sale del mouse sobre la flor
    flower.classList.remove('animated');
  });

  flower.addEventListener('click', () => {
    // Abrir una ventana emergente con información sobre la flor
    alert(`Flor ${flower.dataset.flowerName} clickeada!`);
  });
});
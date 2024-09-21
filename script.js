// Seleccionamos el contenedor del ramo de flores
const ramoDeFlores = document.querySelector('.ramo-de-flores');

// Seleccionamos todas las flores individuales
const flores = document.querySelectorAll('.flor');

// Agregamos un evento de click a cada flor
flores.forEach((flor) => {
  flor.addEventListener('click', (e) => {
    // Cambiamos el color de la flor al hacer click
    flor.style.backgroundColor = getRandomColor();
  });
});

// Función para generar un color aleatorio
function getRandomColor() {
  const letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

// Agregamos un evento de mouseover a cada flor
flores.forEach((flor) => {
  flor.addEventListener('mouseover', (e) => {
    // Cambiamos el tamaño de la flor al pasar el mouse por encima
    flor.style.transform = 'scale(1.5)';
  });
});

// Agregamos un evento de mouseout a cada flor
flores.forEach((flor) => {
  flor.addEventListener('mouseout', (e) => {
    // Regresamos el tamaño de la flor al original al salir del mouse
    flor.style.transform = 'scale(1)';
  });
});

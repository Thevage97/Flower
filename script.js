const canvas = document.getElementById('tulipanes-canvas');
const ctx = canvas.getContext('2d');

// Configuración del ramo de tulipanes
const tulipanes = [
    { x: 100, y: 100, color: 'red' },
    { x: 200, y: 150, color: 'yellow' },
    { x: 300, y: 200, color: 'pink' },
    { x: 400, y: 250, color: 'purple' },
    { x: 500, y: 300, color: 'blue' }
];

// Dibujar el ramo de tulipanes
ctx.clearRect(0, 0, canvas.width, canvas.height);
tulipanes.forEach((tulipan) => {
    ctx.fillStyle = tulipan.color;
    ctx.beginPath();
    ctx.arc(tulipan.x, tulipan.y, 20, 0, 2 * Math.PI);
    ctx.fill();
});

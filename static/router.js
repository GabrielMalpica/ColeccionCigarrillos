document.getElementById('lista-cigarrillos').addEventListener('click', function() {
    window.location.href = 'cigarrillos';
});

document.getElementById('lista-supuestos').addEventListener('click', function() {
    window.location.href = '';
});

document.getElementById('lista-estancos').addEventListener('click', function() {
    window.location.href = 'http://127.0.0.1:5000/api/lista-de-estancos';
});

document.getElementById('lista-almacenes').addEventListener('click', function() {
    window.location.href = 'http://127.0.0.1:5000/api/lista-de-almacenes';
});

document.getElementById('lista-compras').addEventListener('click', function() {
    window.location.href = 'http://127.0.0.1:5000/api/lista-de-compras';
});

document.getElementById('lista-fabricantes').addEventListener('click', function() {
    window.location.href = 'fabricantes';
});

document.getElementById('lista-manufactura').addEventListener('click', function() {
    window.location.href = 'manufactura';
});
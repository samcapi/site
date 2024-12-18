// script.js

function moveLeft() {
    const carousels = document.querySelectorAll('.product-carousel-container .product-row');
    carousels.forEach(carousel => {
        const scrollAmount = carousel.offsetWidth; // Tamanho do carrossel
        carousel.scrollLeft -= scrollAmount; // Move para a esquerda
    });
}

function moveRight() {
    const carousels = document.querySelectorAll('.product-carousel-container .product-row');
    carousels.forEach(carousel => {
        const scrollAmount = carousel.offsetWidth; // Tamanho do carrossel
        carousel.scrollLeft += scrollAmount; // Move para a direita
    });
}

document.addEventListener('DOMContentLoaded', function () {
    const messages = [
        "Bem-vindo à nossa loja online!",
        "Confira nossas ofertas especiais de hoje!",
        "Frete grátis para compras acima de R$ 200!",
        "Novos produtos chegaram! Confira agora."
    ];
    const messageElement = document.getElementById('message-text');
    let currentIndex = 0;

    setInterval(() => {
        currentIndex = (currentIndex + 1) % messages.length;
        messageElement.textContent = messages[currentIndex];
    }, 3000); // Muda a cada 3 segundos
});


// Attēlu saraksts
const headerImages = ['Header_01.jpg', 'Header_02.jpg', 'Header_03.jpg', 'Header_04.jpg', 'Header_05.jpg', 'Header_06.jpg', 'Header_07.jpg', 'Header_08.jpg', 'Header_09.jpg', 'Header_00.jpg'];

// Funkcija nejaušas bildes izvēlei
function getRandomImage() {
    return headerImages[Math.floor(Math.random() * headerImages.length)];
}

// Nomainām fona attēlu
function setRandomHeaderImage() {
    const randomImage = getRandomImage();
    const header = document.getElementById('header');
    if (header) {
        const currentBg = getComputedStyle(header).backgroundImage;
        const bgArray = currentBg.split(',');
        bgArray[2] = `url("images/${randomImage}")`;
        header.style.backgroundImage = bgArray.join(',');
    }
}

// Izsaucam funkciju, kad lapa ir ielādējusies
window.addEventListener('load', setRandomHeaderImage);
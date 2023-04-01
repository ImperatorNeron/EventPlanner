const loginButton = document.querySelector('.login');
const regButton = document.querySelector('.register');
const closeButton = document.querySelectorAll('.close-btn');
const submitButton = document.querySelector('.form-btn');

regButton.addEventListener('click', function () {
    const block = document.querySelector('.block');
    const container = document.querySelector('.container');
    const reg_block = document.querySelector('.reg-block');
    block.style.display = 'block';
    container.style.filter = 'blur(5px)';
    reg_block.style.display = 'block';
});

loginButton.addEventListener('click', function () {
    const block = document.querySelector('.block');
    const container = document.querySelector('.container');
    const log_block = document.querySelector('.login-block');
    block.style.display = 'block';
    container.style.filter = 'blur(5px)';
    log_block.style.display = 'block';
});

function close() {
    const block = document.querySelector('.block');
    const container = document.querySelector('.container');
    const reg_block = document.querySelector('.reg-block');
    const log_block = document.querySelector('.login-block');
    block.style.display = 'none';
    container.style.filter = 'none';
    reg_block.style.display = 'none';
    log_block.style.display = 'none';
}


closeButton[0].addEventListener('click', close);
closeButton[1].addEventListener('click', close);
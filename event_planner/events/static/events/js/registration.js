const loginButton = document.querySelector('.login');
const regButton = document.querySelector('.register');

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
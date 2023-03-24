const loginButton = document.querySelector('.login');

loginButton.addEventListener('click', function () {
    const regForm = document.querySelector('.reg-form');
    const container = document.querySelector('.container');
    const reg_block = document.querySelector('.reg-block');
    regForm.style.display = 'block';
    container.style.filter = 'blur(5px)';
    reg_block.style.display = 'block';
});

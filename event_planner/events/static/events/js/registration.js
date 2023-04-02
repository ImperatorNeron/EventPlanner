// Усі кнопки
const loginButton = document.querySelector('.login');
const regButton = document.querySelector('.register');
const closeButton = document.querySelectorAll('.close-btn');
const submitButton = document.querySelector('.form-btn');

/* Додати затемнення */

function get_blocks(){
    const block = document.querySelector('.block');
    const container = document.querySelector('.container');
    const reg_block = document.querySelector('.reg-block');
    const log_block = document.querySelector('.login-block');
    return [block, container, reg_block, log_block]
}

function display(){
    const arr = get_blocks()
    arr[0].style.display = 'block';
    arr[0].style.backgroundColor  = 'black';
    arr[0].style.opacity = 0.3;
    arr[1].style.filter = 'blur(1px)';
    return arr
}

regButton.addEventListener('click', function () {
    const arr = display()
    arr[2].style.display = 'block';
});

loginButton.addEventListener('click', function () {
    const arr = display()
    arr[3].style.display = 'block';
});

function close() {
    const arr = get_blocks()
    arr[0].style.display = 'none';
    arr[1].style.filter = 'none';
    arr[2].style.display = 'none';
    arr[3].style.display = 'none';
}


closeButton[0].addEventListener('click', close);
closeButton[1].addEventListener('click', close);
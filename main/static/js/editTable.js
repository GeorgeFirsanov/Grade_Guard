const postButton = document.querySelector('.form__save');
const form = document.querySelector('.content__form');
const table = document.querySelector('.form__table');

postButton.addEventListener('click', ()=>{
    console.log('test');
})
setTimeout(function(){
    window.location.reload(1);
 }, 4000);
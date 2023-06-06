const postButton = document.querySelector('.form__save');
const form = document.querySelector('.content__form');
const table = document.querySelector('.form__table');
const cancelButt = document.querySelector('.form__cancel');
const scores = document.querySelectorAll('.js-score');

//подсчет баллов
for (let i = 1; i < table.children.length; i++) {
    const student = table.children[i];
    let totalScore = 0;
    const scores = student.querySelectorAll('.js-score');
    for (const score of scores) {
        totalScore += +score.textContent;
    }
    const generalScore = student.querySelector('.js-general_score');
    generalScore.textContent =  totalScore;

    //расчет оценки
    const generalBall = student.querySelector('.js-general_ball');
    
    if (totalScore < 51){
        generalBall.textContent = 2;
    } else if (totalScore < 65){
        generalScore.textContent = 3;
    } else if (totalScore < 85){
        generalScore.textContent = 4;
    } else{
        generalScore.textContent = 5;
    }
}

//Изменение баллов
table.addEventListener('click', (event)=>{
    const trigger = event.target;
    if(trigger.className != 'js-score') return;
    trigger.classList.toggle('hidden');
    const input = trigger.nextElementSibling;
    input.classList.toggle('hidden');
    input.addEventListener('focusout', ()=>{
        input.style.color = 'yellow';
    })

    const parent = event.target.parentElement;
    console.log(parent);
})
//Отправка данных на сервак
postButton.addEventListener('click', ()=>{
    console.log('test');
})
cancelButt.addEventListener('click', ()=>{
    for (let i = 1; i < table.children.length; i++) {
        const student = table.children[i];

        const scores = student.querySelectorAll('.js-score');
        for (const score of scores) {
            score.classList.remove('hidden');
        }
        const inputs = student.querySelectorAll('input');
        for (const input of inputs) {
            input.classList.add('hidden');
        }
    }
})
const postButton = document.querySelector('.form__save');
const form = document.querySelector('.content__form');
const table = document.querySelector('.form__table');
const generalScores = document.querySelectorAll('.js-general_score');
const generalBalls = document.querySelectorAll('.js-general_ball');
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
    console.log(generalScore.textContent);
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

table.addEventListener('click', (event)=>{
    console.log(event.target);
    const parent = event.target.parentElement;
    console.log(parent);
})
postButton.addEventListener('click', ()=>{
    console.log('test');
})
setTimeout(function(){
    window.location.reload(1);
 }, 18000);

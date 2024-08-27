let input = document.querySelector('#info')
let result = document.querySelector('#result')
let btn = document.querySelector('#btn')

function sendToPython() {
  let {PythonShell} = require('python-shell')
  let options = {
    mode: 'text'
  };
  
  PythonShell.run("main.py", options, function (err, results) {
    if (err) throw err;
    // результаты - это массив, состоящий из сообщений, собранных во время выполнения
    console.log('response: ', results);
    result.textContent = results[0];
    console.log(result)
  });
}

function onclick1(){
  fetch(`http://127.0.0.1:5001/${input.value}`).then((data)=>{      
      return data.text();
      
  }).then((text)=>{
    console.log("data: ", text);
    result.textContent = text;
  }).catch(e=>{
    console.log(e);
  })

}

window.onload = sendToPython;

btn.addEventListener('click', onclick1);

btn.dispatchEvent(new Event('click'))
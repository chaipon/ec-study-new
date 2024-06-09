
// HTML画面から特定のElementを取得する。
const number = document.querySelector('#number');
const plusBtn = document.querySelector("#plus");
const minusBtn = document.querySelector("#minus");
const logclearBtn = document.querySelector("#logclear");
const logsaveBtn = document.querySelector("#logsave");
const logText = document.querySelector("#logarea")
const targetEl = document.querySelector("body");

let count = 0;

let logFunc = function(event){
    let date = new Date();
    month = ('0' + (date.getMonth()+1)).slice(-2)
    day = ('0' + date.getDate()).slice(-2)
    hour = ('0' + date.getHours()).slice(-2)
    min = ('0' + date.getMinutes()).slice(-2)
    sec = ('0' + date.getSeconds()).slice(-2)
    date_str = '['+month+'/'+day+' '+hour+':'+min+':'+sec+'] '
    let log = '\r' + date_str + count

    console.log(log);
    logText.value += log;
    logText.scrollTop = logText.scrollHeight;
};

plusBtn.onclick = function(event){
    count++;
    number.textContent = count;
    logFunc();
};
minusBtn.onclick = function(event){
    count--;
    number.textContent = count;
    logFunc();
};
logclearBtn.onclick = function(event){
    logText.value = "";
};

logsaveBtn.onclick = function(event){
    let content = logText.value; 
    let link = document.createElement( 'a' );
    link.href = window.URL.createObjectURL( new Blob( [content] ) );
    link.download = "test.log";
    link.click();
};
/**
* _app.js
* @author Merubokkusu
* @description 
* @created Sat Mar 30 2019 00:40:08 GMT-0400 (Eastern Daylight Time)
* @copyright 2018 - 2019
* @license CC BY-NC-ND 3.0 US | https://creativecommons.org/licenses/by-nc-nd/3.0/us/
* @website https://github.com/Merubokkusu/discord-spam-bots/
* @email liam@merubokkusu.com
* @last-modified Sun Mar 31 2019 18:42:42 GMT-0400 (Eastern Daylight Time)
*/

rewireLoggingToElement(
    () => document.getElementById("log"),
    () => document.getElementById("log-container"), true);

function rewireLoggingToElement(eleLocator, eleOverflowLocator, autoScroll) {
    fixLoggingFunc('log');
    fixLoggingFunc('debug');
    fixLoggingFunc('warn');
    fixLoggingFunc('error');
    fixLoggingFunc('info');

    function fixLoggingFunc(name) {
        console['old' + name] = console[name];
        console[name] = function(...arguments) {
            const output = produceOutput(name, arguments);
            const eleLog = eleLocator();

            if (autoScroll) {
                const eleContainerLog = eleOverflowLocator();
                const isScrolledToBottom = eleContainerLog.scrollHeight - eleContainerLog.clientHeight <= eleContainerLog.scrollTop + 1;
                eleLog.innerHTML += output + "<br>";
                if (isScrolledToBottom) {
                    eleContainerLog.scrollTop = eleContainerLog.scrollHeight - eleContainerLog.clientHeight;
                }
            } else {
                eleLog.innerHTML += output + "<br>";
            }

            console['old' + name].apply(undefined, arguments);
        };
    }

    function produceOutput(name, arguments) {
        return arguments.reduce((output, arg) => {
            return output +
                "<span class=\"log-" + (typeof arg) + " log-" + name + "\">" +
                    (typeof arg === "object" && (JSON || {}).stringify ? JSON.stringify(arg) : arg) +
                "</span>&nbsp;";
        }, '');
    }
}


function writeToFile(d1){
    var fso = new ActiveXObject("Scripting.FileSystemObject");
    var fh = fso.OpenTextFile("t.txt", 8, true, 0);
    console.log(fh)
    fh.WriteLine(d1);
    fh.Close();
}
var submit = document.getElementById("add_token_button");
submit.onclick = function () {
    var token_text = document.getElementById("token_add").value;
    eel.save_token(token_text);
    console.error(token_text)
}

document.getElementById("test_button").onclick = function () {
    eel.sv_textSpam(document.getElementById('text_spam').value);
    
}
eel.expose(test);
function test(){
    eel.tokenRun();
}

eel.expose(log);
function log(s){
    console.warn(s);
}

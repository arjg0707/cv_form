document.addEventListener('DOMContentLoaded',()=>{
    document.querySelector('#submit').disabled = true;

    document.querySelector('#task').onkeyup = () =>{
        if(document.querySelector('#task').value.length > 0)
            document.querySelector('#submit').disabled = false;
        else
            document.querySelector('#submit').disabled = true;
    };
});

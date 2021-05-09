$(function () {
    var canvas = $('.whiteboard')[0];
    var context = canvas.getContext('2d');
    var prediction = "";
    context.fillStyle = "white";
    context.fillRect(0, 0, canvas.width, canvas.height);
    var current = {
        color: 'black'
    };
    
    var drawing = false;
    var clearBtn = $('#clear-btn');
    var drawBtn = $('#draw-btn');
    var predictBtn = $('#predict-btn');
    const myCanvas = document.querySelector('#myCanvas');
    
    function takeshot() {
        var dataURI = canvas.toDataURL("image/png");
        var form = document.getElementById('myForm');
        var formData = new FormData(form);
         
            
        $.post( "/predict", {
            url: dataURI 
        },function(data) {
            prediction = $.parseJSON(data)
            id1.innerText = "Prediction is: "+prediction;
        });
    }
    
    
    
    function drawLine(x0, y0, x1, y1, color) {
        context.beginPath();
        context.moveTo(x0, y0);
        context.lineTo(x1, y1);
        context.strokeStyle = color;
        context.lineWidth = 2;
        context.stroke();
        context.closePath();
    }

    function onMouseDown(e) {
        drawing = true;
        current.x = e.clientX;
        current.y = e.clientY;
    }

    function onMouseUp(e) {
        if (!drawing) { return; }
        drawing = false;
        drawLine(current.x, current.y, e.clientX, e.clientY, current.color);
    }

    function onMouseMove(e) {
        if (!drawing) { return; }
        drawLine(current.x, current.y, e.clientX, e.clientY, current.color);
        current.x = e.clientX;
        current.y = e.clientY;
    }
    
    function onResize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    };
    function clearBoard() {
        context.clearRect(0, 0, canvas.width, canvas.height);
    };
    function drawShape(){
        var shape = prediction;
        clearBoard()
        //line 
        if(shape=="line"){
        drawLine(500,300 ,800,300,current.color)
        }
        //rectangle
        else if(shape=="rectangle"){
        context.strokeRect(400,200,500,300);
        }
        //square
        else if(shape=="square"){
        context.strokeRect(400,200,200,200);
        }
        //circle
        else if(shape=="circle"){
        context.beginPath();
        context.arc(500, 300, 100, 0, 2 * Math.PI);
        //context.stroke()
        }
        
        //triangle
        else if(shape=="triangle"){
        context.beginPath();
        context.moveTo(600, 250);
        context.lineTo(400, 500);
        context.lineTo(800, 500);
        context.closePath();
        //context.stroke()
        }
        //scalene
        else if(shape=="scalene"){
        context.beginPath();
        context.moveTo(400, 250);
        context.lineTo(600, 500);
        context.lineTo(450, 500);
        context.closePath();
        //context.stroke();
        }
        
        //oval
        else if(shape=="oval"){
        context.scale(0.75, 1);
        context.arc(800, 300, 100, 0, Math.PI*2, false);
        }
        context.stroke();
        
    }
    
    canvas.addEventListener('mousedown', onMouseDown);
    canvas.addEventListener('mouseup', onMouseUp);
    canvas.addEventListener('mouseout', onMouseUp);
    canvas.addEventListener('mousemove', onMouseMove);
    
    clearBtn.on('click', clearBoard);
    predictBtn.on('click', takeshot);
    drawBtn.on('click', drawShape);
    
    window.addEventListener('resize', onResize);
    onResize();
});

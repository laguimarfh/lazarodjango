var canvas;
var ctx;
var refImage;

$(document).ready(function() {
  canvas = document.getElementById('drawing-canvas');
  ctx = canvas.getContext('2d');
  refImage = document.getElementById('reference-img');
  drawImageScaled(refImage, ctx);
  
  $(canvas).click(function(e) {
    const offset = $(this).offset();
    const x = (e.pageX - offset.left) - 5;
    const y = (e.pageY - offset.top) + 10;
    ctx.font = '22px normal'
    ctx.fillStyle = 'red';
    ctx.fillText('X', x, y);
    // console.log(x, y);
    document.getElementById('coorx').value = x;
    document.getElementById('coory').value = y;
  });
});

function drawImageScaled(img, ctx) {
  var canvas = ctx.canvas;
  var hRatio = canvas.width / img.width;
  var vRatio = canvas.height / img.height;
  var ratio  = Math.min ( hRatio, vRatio );
  var centerShift_x = ( canvas.width - img.width*ratio ) / 2;
  var centerShift_y = ( canvas.height - img.height*ratio ) / 2;  
  ctx.clearRect(0,0,canvas.width, canvas.height);
  ctx.drawImage(img, 0,0, img.width, img.height,
                      centerShift_x,centerShift_y,img.width*ratio, img.height*ratio);  
}







// $('#post-form').on('submit', function(event){
//     event.preventDefault();
//     console.log("form submitted!")  // sanity check
//     create_post();
// });





// // $("#canvas").click(function(e){
// //     getPosition(e); 
// // });

// // var pointSize = 3;

// // function getPosition(event){
// //     var rect = canvas.getBoundingClientRect();
// //     var x = event.clientX - rect.left;
// //     var y = event.clientY - rect.top;
       
// //     drawCoordinates(x,y);
// // }

// // function drawCoordinates(x,y){	
// //      var ctx = document.getElementById("canvas").getContext("2d");


// //      ctx.fillStyle = "#ff2626"; // Red color

// //    ctx.beginPath();
// //    ctx.arc(x, y, pointSize, 0, Math.PI * 2, true);
// //    ctx.fill();
// //    console.log(x)
// // }


        
        // function download() {
        //   const atag = document.createElement('a');
        //   atag.href = canvas.toDataURL('image/png');
        //   atag.download = 'defects.png';
        //   atag.click();
        // }

        // function clearCanvas() {
        //   ctx.clearRect(0, 0, canvas.width, canvas.height);
        //   drawImageScaled(refImage, ctx);
        // }
    
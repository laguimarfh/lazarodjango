
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
    ctx.fillText('x', x, y);
    console.log(ctx, refImage)
    console.log(x, y);
    console.log(e.pageX);
    console.log(offset);
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



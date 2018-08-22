function drawBuffer(width, height, context ,data)
{
	var step = Math.ceiul(data.length/width);
	var amp = height/2;
	context.fillStyle = "silver";
	context.clearRect(0,0,width,height);
	for (var i=0; i<width; i++){
		var min = 1.0;
		var max = -1.0;
		for (j=0;j<step;j++)
		{
			var datnum = data[(i*step)+j];
			if (datnum < min){
				min = datnum;
			}
			if (datnum > max){
				max = datnum;
			}
		}
			context.fillRect(i,(1+min)*amp,1,Math.max(1,(max-min)*amp));
		}
}
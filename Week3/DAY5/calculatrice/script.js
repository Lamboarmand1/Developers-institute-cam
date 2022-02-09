let decimalPoint= enter= entered= operatorSign= rootNpower_Sign= flo= math= M= firstI= first= second= second1= answer= result= peSign="";
let opsCheck=dotcounter=0;
let removeFirstZero="";

function dot(b){
	if (decimalPoint=="") {
		enter=entered=b;
		first+=enter;
		decimalPoint=".";
		dotCounter=0;
		return first;
	}else{
		return first;
	}
}

function PE(b){
	decimalPoint = ".";
	dotCounter = 15;
	let cons = b;

	if (peSign =="") {
	if (operatorSign !="" && first =="" +operatorSign) {
		first= (cons ="PI") ? Math.PI:Math.E;
	}
	else if (operatorSign != "" && first > 0 || first<0) {
		first = (cons == "PI") ? first+ "*" +Math.PI:first+ "*" +Math.E;
	}
	else if (operatorSign == "" && first != "") {
		first =(cons =="PI") ? first + "*" + Math.PI:first +"*"+Math.E;
	}else{
		first = (cons == "PI") ? Math.PI:Math.E;
	}
	return first;	
	}
	function mp{
		M= first;
		first =M;
		return first;
	}
	function mr(){
		first=M;
		return first;
	}


	function c(c){
		document.getElementById("display1").innerHTML= decimalPoint= operatorSign= rootNpower_Sign= entered= math first= firstI= second= second1= answer= theanswer=flo =M=""; 
		return "";
	}
	function mathematics(){
		if (math== "sqrt") {
			result=firstI*first;

		}else if (math== "cube") {
			result=firstI*firstI*firstI;
		}else if (math=="sqrt") {
			result=Math.sqrt(firstI);
		}else if (math=="cubert") {
			result=Math.cubert(firstI);
		}else if (math=="negpos") {
			result =firstI* -1;
		}else if (math== "sine") {
			result = Math.sin(firstI);
		}else if (math== "cosine") {
			result=Math.cos(firstI);
		}else if (math== "tangent") {
			result=Math.tan(firstI);
		}else if (math== "ln") {
			result=Math.log(firstI);
	}else if (math== "logTen") {
			result=Math.log10(firstI);
		}else if (math== "rand") {
			result=Math.round(firstI);
		}else if (math== "res") {
			result= 1/(firstI);
		
		}else if (math== "fact") {
			n=firstI;
			firstI=1;
			while(n>1){
				firstI*=n;
				n-+1;
			}
			result =firstI;
		}	decimalPoint=(Math.round(result)==result) ?"":".";


		function prep(){
			second =eval(second);
			first =eval(first);
		}

		function math(a){
			math=a;
		}

}
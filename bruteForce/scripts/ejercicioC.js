export function ejercicioC(password){

	let currentAtempt=Array(password.length).fill(0);
	const nums = '123456789';
        const alphabetLower = 'abcdefghijklmnopqrstuvwxyz';
        const mix=nums+alphabetLower;
	let counter = 1;
	let start=new Date().getTime();
	let divC=document.querySelector('.ejercicioC');
	const attempt=(currentIndex)=>{
		if(currentIndex>=password.length){
			if(currentAtempt.join('')===password){   
				let end = new Date().getTime();
				let timePassed = end - start;
				divC.innerHTML=`
					<p>match encontrado: ${currentAtempt.join('')}</p>
					<p>numero de intentos: ${counter}</p>
					<p>tiempo transcurrido: ${timePassed}</p>
				`
				return true
			}
			return false
		}
		for(let char of mix){
			currentAtempt[currentIndex]=char;
			counter++;
			if (attempt(currentIndex + 1)) return true;
		}
		return false;
	}
	attempt(0)
};
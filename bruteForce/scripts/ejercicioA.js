export function ejercicioA(password){

	let currentAtempt=Array(password.length).fill(0);
	const alphabetLower = 'abcdefghijklmnopqrstuvwxyz';
	let counter = 1;
	let start=new Date().getTime();
	let divA=document.querySelector('.ejercicioA');

	divA.innerHTML="<p>Buscando coincidencia</p>"

	const attempt=(currentIndex)=>{
		if(currentIndex>=password.length){
			if(currentAtempt.join('')===password){
				let end = new Date().getTime();
				let timePassed = end - start;
				divA.innerHTML=`
					<p>match encontrado: ${currentAtempt.join('')}</p>
					<p>numero de intentos: ${counter}</p>
					<p>tiempo transcurrido: ${timePassed}</p>
				`
				return true
			}
			return false
		}
		for(let char of alphabetLower){
			currentAtempt[currentIndex]=char;
			counter++;
			if (attempt(currentIndex + 1)) return true;
		}
		return false;
	}
	attempt(0)
};
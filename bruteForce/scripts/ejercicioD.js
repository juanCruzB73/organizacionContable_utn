export function ejercicioD(password){

	let currentAtempt=Array(password.length).fill(0);
	const nums = '123456789';
    const alphabetLower = 'abcdefghijklmnopqrstuvwxyz';
    const alphabetUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    const mix=nums+alphabetLower+alphabetUpper;
	let counter = 1;
	let start=new Date().getTime();
	let divD=document.querySelector('.ejercicioD');
	const attempt=(currentIndex)=>{
		if(currentIndex>=password.length){
			if(currentAtempt.join('')===password){   
				let end = new Date().getTime();
				let timePassed = end - start;
				divD.innerHTML=`
					<p>match encontrado: ${currentAtempt.join('')}</p>
					<p>numero de intentos: ${counter}</p>
					<p>tiempo transcurrido: ${timePassed}</p>
				`
				return true
			}
			return false
		}
		const tryNextChar = (i) => {
            if (i >= mix.length) {
                return false;
            }
            
            currentAtempt[currentIndex] = mix[i];
            counter++;
            
            if (attempt(currentIndex + 1)) {
                return true;
            } else {
                setTimeout(() => tryNextChar(i + 1), 0);
            }
        };
        
        tryNextChar(0);
    };
    
    attempt(0);
};
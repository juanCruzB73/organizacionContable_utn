function ejercicioD(password){
    console.log("buscando coincidencia...")
	let currentAtempt=Array(password.length).fill(0);
	const nums = '123456789';
    const alphabetLower = 'abcdefghijklmnopqrstuvwxyz';
    const alphabetUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    const mix=nums+alphabetLower+alphabetUpper;
	let counter = 1;
	let start=new Date().getTime();
	const attempt=(currentIndex)=>{
		if(currentIndex>=password.length){
			if(currentAtempt.join('')===password){   
				let end = new Date().getTime();
				let timePassed = end - start;
				console.log(`
					<p>match encontrado: ${currentAtempt.join('')}</p>
					<p>numero de intentos: ${counter}</p>
					<p>tiempo transcurrido: ${timePassed}</p>
				`)
				return true
			}
			return false
		}
		const tryNextChar = (i) => {
            if (i >= mix.length) {
                return false;
            }
            console.log(counter+" "+currentAtempt.join(''))
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
ejercicioD("Hb5gr5A");
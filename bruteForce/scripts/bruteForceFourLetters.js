/*
 definir array con usuario y contraseña
 definir array con numeros del 0 al 9
 funcion vulnerarContraseña():recive contraseña-if(el digito es el correcto?}termina y pasa a siguiente posicion:prueba otro digito-muestra intento y contraseña incorrecta. 
  */

const user=["juan","alrn"];
const user2=["juan","9436"];
const user3=["juan","5k1a"]

const alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
const alphabetLower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
const numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];

let bruteForce=(password)=>{
	let aux=password.split('');
	let passwordFinded='';
	let counter=1;
	let start=new Date().getTime();
	for(i=0;i<aux.length+1;i++){
		alphabetLower.some(e=>{
			if(password==passwordFinded){
				let end=new Date().getTime();
				let timePassed=end-start;
				console.log("match encontrado: "+passwordFinded+"\n"+" numero de intentos: "+counter+"\n"+" tiempo transcurrido :"+timePassed);
				return true;
			}
			if(e==aux[i]){
				passwordFinded+=e;
				return true;
			}
		counter++
		})
	}
}
bruteForce(user[1]);

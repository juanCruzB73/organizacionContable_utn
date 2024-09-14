const user = ["juan", "b4L9!8%5"];
const alphabetLower = 'abcdefghijklmnopqrstuvwxyz';
const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
const numbers = '0123456789';
const symbols = '!#$%&/()=+*';

// Combine all character sets
const allCharacters = alphabetLower + alphabet + numbers + symbols;

const bruteForce = (password) => {
    console.log("Buscando coincidencia...");
    
    let passwordFinded = '';
    let counter = 0;
    let start = new Date().getTime();

    const attemptPassword = (currentIndex) => {
        if (currentIndex >= password.length) {
            if (password === passwordFinded) {
                let end = new Date().getTime();
                let timePassed = end - start;
                console.log(`Match encontrado: ${passwordFinded}`);
                console.log(`Número de intentos: ${counter}`);
                console.log(`Tiempo transcurrido: ${timePassed} ms`);
                return true;
            }
            return false;
        }

        for (let char of allCharacters) {
            passwordFinded = passwordFinded.slice(0, currentIndex) + char + passwordFinded.slice(currentIndex + 1);
            counter++;
            if (attemptPassword(currentIndex + 1)) return true;
        }
        return false;
    };

    attemptPassword(0);
};

bruteForce(user[1]);

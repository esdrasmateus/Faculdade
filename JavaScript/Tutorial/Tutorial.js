// add beginning == .unshift()
// .append == .push()
// remove first == .shift()
// remove last == .pop()
// delete object.property
// object["propertyInexistent"] = "propertyToAdd"
// object.hasOwnProperty(propertyToCheck) *returns true or false*
// convert to Int = parseInt(str)
// Radix = parseInt(str, 2) = binary
/* 

object1 = 
{
	object2 = 
	{
		someProperty : something
	}
}

console.log(object1.object2[someProperty]);

*/

/* var count = 0;

function cc(card)
{
    switch (card)
    {
		case 1,2,3,4,5,6:
			count++;
		break;
		case 10, "J", "Q", "K", "A":
			count--;
		break;
	}

	var holdbet = "Hold";
	if (count > 0) holdbet = "Bet";

    return count + " " + holdbet;
}

cc(2); cc("K"); cc(7); cc(10); cc("A");

console.log(cc(4)); */

/*
ternary operators

return num > 0 ? "positive" : num < 0 ? "negative" : "zero"
*/

// Object.freeze(object) makes an object to never change

/* let a = 3, b = 5;
(() =>
{
	[a, b] = [b, a];
}) */

/* let _name = "Hehe", _age = 6438;

const greetings = `Hello, my name is ${_name}!
and I'm ${_age} years old!`;

console.log(greetings); 
*/

// const createPerson = (name, age, gender) => ({name, age, gender});

/*

const bicycle = 
{
	gear : 2,
	setGear(newGear)
	{
		this.gear = newGear;
	}
};

bicycle.setGear(3);
console.log(bicycle.gear); */

/*

class SpaceShuttle
{
	constructor(targetPlanet)
	{
		this.targetPlanet = targetPlanet;
	}
}

var zeus = new SpaceShuttle("Jupiter");

console.log(zeus.targetPlanet);


class Thermostat
{
	constructor(temp)
	{
		this._temp = 5/9 * (temp - 32);
	}

	get temperature() 
	{
		return this._temp;
	}

	set temperature(updatedTemp)
	{
		this._temp = updatedTemp;
	}
}

const thermos= new Thermostat(74);
let temp = thermos.temperature;
thermos.temperature = 25;
temp = thermos.temperature;
console.log(temp);

*/

/*

import {someFunction} from "./filename"

import * as myObject from "./fileFolder"

import myFunction from "./myFunction";

*/

/* 
export const myFunction = (something) => {function}

or

const myFunction = (something) => {function}

export {myFunction};

export default function myFunction(something) {function}

*/
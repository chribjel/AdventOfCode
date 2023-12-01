import { input } from "./input";

function solve(input: string) {
  const lines = input.split("\n");

  let sum = 0;
  for (const line of lines) {
    if (line === "") break;
    const firstDigit = line.split("").find(char => !isNaN(parseInt(char)));
    const lastDigit = line.split("").reverse().find(char => !isNaN(parseInt(char)));
    const combined = firstDigit! + lastDigit!
    sum += parseInt(combined);
  }
  return sum;
}

console.log(solve(input))

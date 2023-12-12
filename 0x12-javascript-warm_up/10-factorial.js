#!/usr/bin/node
const argc = process.argv;
const n = (+argc[2]);
function factorialRecursion (n) {
  if (!n || !(+n)) {
    return 1;
  }
  if (n === 0 || n === 1) {
    return 1;
  }
  if (n > 1) {
    return n * factorialRecursion(n - 1);
  }
}
console.log(factorialRecursion(n));

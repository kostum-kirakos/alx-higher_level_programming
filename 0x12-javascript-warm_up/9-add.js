#!/usr/bin/node
const argc = process.argv;
function add (a, b) {
  a = (+argc[2]);
  b = (+argc[3]);
  const result = (+argc[2]) + (+argc[3]);
  return result;
}
console.log(`${add()}`);

#!/usr/bin/node
const argc = process.argv;
if (+(argc[2])) {
  console.log(`My number: ${+(argc[2])}`);
} else {
  console.log('Not a number');
}

#!/usr/bin/node
const argc = process.argv;
let index = 0;
if (+(argc[2])) {
  while (index < (+(argc[2]))) {
    let index2 = 0;
    while (index2 < (+(argc[2]))) {
      process.stdout.write('x');
      index2++;
    }
    index++;
    console.log();
  }
} else {
  console.log('Missing size');
}

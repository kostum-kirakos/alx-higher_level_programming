#!/usr/bin/node
const argc = process.argv;
let index;
if (+(argc[2])) {
  for (index = 0; index < (+(argc[2])); index++) {
    console.log('c is fun');
  }
} else {
  console.log('Missing number of occurrences');
}

#!/usr/bin/node
const number = Number(process.argv[2]);

if (Number.isNaN(number)) {
  console.log('Missing size');
} else {
  let output = '';
  for (let i = 0; i < (number * number); i++) {
    output += 'X';
    if ((i + 1) % number === 0) {
      console.log(output);
      output = '';
    }
  }
}

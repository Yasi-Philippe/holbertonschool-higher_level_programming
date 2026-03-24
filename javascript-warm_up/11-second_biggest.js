#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  let a = 0;
  let b = 0;
  for (let i = 1; i <= args.length; i++) {
    if (args[i] > a) {
      b = a;
      a = args[i];
    }
  }
  console.log(b);
}

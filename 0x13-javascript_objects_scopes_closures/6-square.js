#!/usr/bin/node

const SuperSquare = require('./5-square');

module.exports = class Square extends SuperSquare {
  charPrint (c) {
    if (c !== undefined) {
      const x = this.width;
      let y = this.height;
      while (y > 0) {
        console.log('C'.repeat(x));
        y--;
      }
    } else {
      return this.print();
    }
  }
};

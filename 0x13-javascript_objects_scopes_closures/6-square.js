#!/usr/bin/node

const SuperSquare = require('./5-square');

module.exports = class Square extends SuperSquare {
  charPrint (c) {
    if (c !== undefined) {
      const i = this.width;
      let j = this.height;
      while (j > 0) {
        console.log('C'.repeat(i));
        j--;
      }
    } else {
      return this.print();
    }
  }
};

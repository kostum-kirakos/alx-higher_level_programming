#!/usr/bin/node
exports.converter = function (base) {
  return function decimalConverter (decimal) {
    return decimal.toString(base);
  };
};

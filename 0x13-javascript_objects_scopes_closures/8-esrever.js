#!/usr/bin/node
exports.esrever = function (list) {
  const newL = [];
  for (let i = list.length - 1; i > -1; i--) {
    newL.push(list[i]);
  }
  return (newL);
};

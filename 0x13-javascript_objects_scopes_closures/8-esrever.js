#!/usr/bin/node

// returns the reversed version of a list

exports.esrever = function (list) {
    let array = [];
    list.forEach (item => array.unshift(item));
    return (array);
};

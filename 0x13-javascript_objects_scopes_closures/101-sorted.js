#!/usr/bin/node

const { dict } = require('./101-data');

const occurrencesDict = {};

// Grouping user IDs by occurrence count
Object.keys(dict).forEach(userId => {
  const occurrences = dict[userId];
  if (!occurrencesDict[occurrences]) {
    occurrencesDict[occurrences] = [userId];
  } else {
    occurrencesDict[occurrences].push(userId);
  }
});

console.log('New dictionary by occurrence:', occurrencesDict);


#!/usr/bin/node
const fs = require('fs');
const path = require('path');

function concatFiles(file1Path, file2Path, destinationPath) {
  const file1Content = fs.readFileSync(file1Path, 'utf8');
  const file2Content = fs.readFileSync(file2Path, 'utf8');

  const concatenatedContent = file1Content + file2Content;

  fs.writeFileSync(destinationPath, concatenatedContent, 'utf8');
  console.log(`Files ${file1Path} and ${file2Path} concatenated to ${destinationPath}`);
}

// Usage: node concatFiles.js sourceFile1.txt sourceFile2.txt destinationFile.txt
const [, , file1Path, file2Path, destinationPath] = process.argv;

if (!file1Path || !file2Path || !destinationPath) {
  console.log('Please provide file paths for source files and the destination file.');
} else {
  concatFiles(file1Path, file2Path, destinationPath);
}


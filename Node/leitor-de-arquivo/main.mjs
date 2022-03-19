import { readFile } from 'fs';
import { promisify } from 'util';

const fileReader = promisify(readFile);

class ReadFileError extends Error {
  constructor(message="Couldn't read file") {
    super(message);
    this.name = 'ReadFileError';
  }
}

const getFile = async () => {
  try {
    return await fileReader('./package.json', 'utf-8');
  } catch (e) {
    throw new ReadFileError();
  }
}

getFile().then(console.log).catch(console.log);

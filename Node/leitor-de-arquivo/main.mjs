import { readFile } from 'fs';
import { promisify } from 'util';

const fileReader = promisify(readFile);

const run = async () => {
  const file = await fileReader('./package.json', 'utf-8');
  console.log(file);
};

run();

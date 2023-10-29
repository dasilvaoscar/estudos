import fs from 'fs'
import { parse } from 'csv-parse';

const result = []

let counter = 1
let columms

const fileStream = fs.createReadStream('./files/test.csv')
  .pipe(parse({ delimiter: ",", from_line: 1 }))

fileStream
  .on('data', (chunk) => {
    const isHeaderRow = counter === 1
    const isDataRow = !isHeaderRow

    if (isHeaderRow) { 
      columms = chunk
    } 

    if (isDataRow) {
      const row = createRow(chunk)
      result.push(row)
    }

    counter += 1
  })
  .on("end", () => {
    console.log(result);
  })

function createRow(chunk) {
  const partialRow = {}
  columms.map((data, index) => { partialRow[data] = chunk[index] })
  return partialRow
}
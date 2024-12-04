const input = await getInput();

console.log("Part 1 (example):", part1(await getExampleInput()));
console.log("Part 1:", part1(input));
console.log("Part 2 (example):", part2(await getExampleInput()));
console.log("Part 2:", part2(input));

function reverseString(input: string) {
  return input.split("").toReversed().join("");
}
function getColumns(rows: string[]): string[] {
  const columns: string[] = [];
  for (let i = 0; i < rows.length; i++) {
    for (let j = 0; j < rows[i].length; j++) {
      if (!columns[j]) {
        columns[j] = rows[i][j];
      } else {
        columns[j] += rows[i][j];
      }
    }
  }
  return columns;
}

function getLeftToRightDownDiagonals(rows: string[]): string[] {
  const diagonals: string[] = [];
  for (let i = 0; i < rows.length; i++) {
    for (let j = 0; j < rows[i].length; j++) {
      if (!diagonals[i + j]) {
        diagonals[i + j] = rows[j][i];
      } else {
        diagonals[i + j] += rows[j][i];
      }
    }
  }
  return diagonals;
}

function findXmas(lineOfText: string) {
  const XMASOccurrences = lineOfText.match(/XMAS/g);
  if (XMASOccurrences) {
    return XMASOccurrences.length;
  }
  return 0;
}

function findXmasReversed(lineOfText: string) {
  return findXmas(reverseString(lineOfText));
}

function part1(input: string) {
  const rows = input.split("\n");
  const flippedRows = rows.map((row) => reverseString(row));
  const columns = getColumns(rows);
  const leftToRightDiagonals = getLeftToRightDownDiagonals(rows);
  const rightToLeftDiagonals = getLeftToRightDownDiagonals(flippedRows);
  let xmasCount = 0;

  //horizontals
  for (const line of rows) {
    xmasCount += findXmas(line);
    xmasCount += findXmasReversed(line);
  }

  // verticals
  for (const line of columns) {
    xmasCount += findXmas(line);
    xmasCount += findXmasReversed(line);
  }

  //left to right diagonals
  for (const line of leftToRightDiagonals) {
    xmasCount += findXmas(line);
    xmasCount += findXmasReversed(line);
  }

  //right to left diagonals
  for (const line of rightToLeftDiagonals) {
    xmasCount += findXmas(line);
    xmasCount += findXmasReversed(line);
  }

  return xmasCount;
}

function part2(input: string) {
  const rows = input.split("\n");
  let xmasCount = 0;

  for (let i = 0; i < rows.length; i++) {
    const row = rows[i];

    for (let j = 0; j < row.length; j++) {
      const char = row[j];
      const char3 = row[j + 2];
      if (!char3) {
        continue;
      }
      const nextRow = rows[i + 1];
      const nextNextRow = rows[i + 2];
      if (!nextRow || !nextNextRow) {
        continue;
      }

      const middleIndex = j + 1;
      const middleCharOnNextRow = nextRow[middleIndex];
      const charNextNextRow = nextNextRow[j];
      const char3NextNextRow = nextNextRow[j + 2];

      if (middleCharOnNextRow === "A") {
        if (
          char === "M" &&
          char3 === "M" &&
          charNextNextRow === "S" &&
          char3NextNextRow === "S"
        ) {
          xmasCount++;
        } else if (
          char === "M" &&
          char3 === "S" &&
          charNextNextRow === "M" &&
          char3NextNextRow === "S"
        ) {
          xmasCount++;
        } else if (
          char === "S" &&
          char3 === "S" &&
          charNextNextRow === "M" &&
          char3NextNextRow === "M"
        ) {
          xmasCount++;
        } else if (
          char === "S" &&
          char3 === "M" &&
          charNextNextRow === "S" &&
          char3NextNextRow === "M"
        ) {
          xmasCount++;
        }
      }
    }
  }
  return xmasCount;
}

async function getInput() {
  return Bun.file("./input.txt").text();
}

async function getExampleInput() {
  return Bun.file("./example.txt").text();
}

export {};

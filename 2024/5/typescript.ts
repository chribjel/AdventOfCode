const ITERATIONS = 100;

const exampleInput = await getExampleInput();
const input = await getInput();

function timeSolution(solution: () => number) {
  const start = Bun.nanoseconds();
  const result = solution();
  const end = Bun.nanoseconds();
  const ms = (end - start) / 1_000_000;
  return [result, ms];
}

function standardDeviation(arr: number[]) {
  const avg = arr.reduce((a, b) => a + b, 0) / arr.length;
  const squareDiffs = arr.map((a) => (a - avg) ** 2);
  const avgSquareDiff = squareDiffs.reduce((a, b) => a + b, 0) / arr.length;
  return Math.sqrt(avgSquareDiff);
}

// run solutions 1000 times and average the result and calculate delta
const times1: number[] = [];
const times2: number[] = [];
let solution1 = 0;
let solution2 = 0;
for (let i = 0; i < ITERATIONS; i++) {
  const [result1, ms1] = timeSolution(() => part1(input));
  times1.push(ms1);
  const [result2, ms2] = timeSolution(() => part2(input));
  times2.push(ms2);
  if (i === 0) {
    solution1 = result1;
    solution2 = result2;
  }
}
const ms1 = times1.reduce((a, b) => a + b, 0) / ITERATIONS;
const ms1TwoDecimals = ms1.toFixed(2);
const ms2 = times2.reduce((a, b) => a + b, 0) / ITERATIONS;
const ms2TwoDecimals = ms2.toFixed(2);

const sd1 = standardDeviation(times1);
const diff1 = ms1 - Math.min(...times1);
const diff1TwoDecimals = diff1.toFixed(2);
const sd1TwoDecimals = sd1.toFixed(2);
const sd2 = standardDeviation(times2);
const diff2 = ms2 - Math.min(...times2);
const diff2TwoDecimals = diff2.toFixed(2);
const sd2TwoDecimals = sd2.toFixed(2);

console.log("-------------------------------------");
console.log("PART 1:");
console.log("Solution:", solution1);
console.log("Time:", `${ms1TwoDecimals}ms +-`, sd1TwoDecimals);
console.log("Samples:", times1.length);
console.log("-------------------------------------");
console.log("PART 2:");
console.log("Solution:", solution2);
console.log("Time:", `${ms2TwoDecimals}ms +-`, sd2TwoDecimals);
console.log("Samples:", times2.length);
console.log("-------------------------------------");

function getRules(input: string) {
  const [rules] = input.split("\n\n");
  const lines = rules.split("\n");
  return lines;
}

function getRuleMap(input: string) {
  const rules = getRules(input);
  const ruleMap: {
    before: Record<string, string[]>;
    after: Record<string, string[]>;
  } = {
    before: {},
    after: {},
  };
  for (const rule of rules) {
    const [before, after] = rule.split("|");
    if (!ruleMap.before[before]) {
      ruleMap.before[before] = [after];
    } else {
      ruleMap.before[before].push(after);
    }
    if (!ruleMap.after[after]) {
      ruleMap.after[after] = [before];
    } else {
      ruleMap.after[after].push(before);
    }
  }
  return ruleMap;
}

function getUpdates(input: string) {
  const [, updates] = input.split("\n\n");
  const lines = updates.split("\n");
  return lines;
}

function getMiddleElement(arr: string[]) {
  return arr[Math.floor(arr.length / 2)];
}

function isUpdateValid(
  update: string[],
  ruleMap: {
    before: Record<string, string[]>;
    after: Record<string, string[]>;
  }
) {
  for (let j = 0; j < update.length - 1; j++) {
    const instruction = update[j];
    const nextInstructions = update.slice(j + 1);
    if (
      ruleMap.after[instruction] &&
      nextInstructions.some((nextInstruction) =>
        ruleMap.after[instruction].includes(nextInstruction)
      )
    ) {
      // invalid
      return false;
    }
    if (
      nextInstructions.some((nextInstruction) =>
        ruleMap.before[nextInstruction]?.includes(instruction)
      )
    ) {
      // invalid
      return false;
    }
  }
  return true;
}

function attemptFixUpdate(
  update: string[],
  ruleMap: {
    before: Record<string, string[]>;
    after: Record<string, string[]>;
  }
) {
  for (let j = 0; j < update.length - 1; j++) {
    const instruction = update[j];
    const nextInstructions = update.slice(j + 1);
    if (
      ruleMap.after[instruction] &&
      nextInstructions.some((nextInstruction) =>
        ruleMap.after[instruction].includes(nextInstruction)
      )
    ) {
      // swap instruction and the next instruction
      const nextInstruction = nextInstructions[0];
      update[j] = nextInstruction;
      update[j + 1] = instruction;
    }
    if (
      nextInstructions.some((nextInstruction) =>
        ruleMap.before[nextInstruction]?.includes(instruction)
      )
    ) {
      // swap instruction and the next instruction
      const nextInstruction = nextInstructions[0];
      update[j] = nextInstruction;
      update[j + 1] = instruction;
    }
  }
  return update;
}

function part1(input: string) {
  const ruleMap = getRuleMap(input);
  const updates = getUpdates(input);
  let result = 0;

  for (let i = 0; i < updates.length; i++) {
    const update = updates[i].split(",");

    if (isUpdateValid(update, ruleMap)) {
      const middleElement = getMiddleElement(update);
      result += Number.parseInt(middleElement);
    }
  }
  return result;
}

function part2(input: string) {
  const updates = getUpdates(input);
  const ruleMap = getRuleMap(input);
  let result = 0;

  for (let i = 0; i < updates.length; i++) {
    const update = updates[i].split(",");

    if (isUpdateValid(update, ruleMap)) {
      continue;
    }

    let fixedUpdate = attemptFixUpdate(update, ruleMap);
    while (!isUpdateValid(fixedUpdate, ruleMap)) {
      fixedUpdate = attemptFixUpdate(fixedUpdate, ruleMap);
    }
    const middleElement = getMiddleElement(fixedUpdate);
    result += Number.parseInt(middleElement);
  }
  return result;
}

async function getInput() {
  return Bun.file("./input.txt").text();
}

async function getExampleInput() {
  return Bun.file("./example.txt").text();
}

export {};

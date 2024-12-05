const input = await getInput();

console.log("Part 1 (example):", part1(await getExampleInput()));
console.log("Part 1:", part1(input));
console.log("Part 2 (example):", part2(await getExampleInput()));
console.log("Part 2:", part2(input));

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
    console.log(`update ${i + 1}/${updates.length}`);
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

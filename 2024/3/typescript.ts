const input = await getInput();

console.log(
  "Part 1 (example):",
  part1(
    "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
  )
);
console.log("Part 1:", part1(input));
console.log(
  "Part 2 (example):",
  part2(
    "mul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
  )
);
console.log("Part 2:", part2(input));

function part1(input: string) {
  const muls = input.match(/mul\(\d+,\d+\)/g);
  const sumsOfMuls = muls?.reduce((acc, mul) => {
    const [a, b] = mul
      .replace("mul(", "")
      .replace(")", "")
      .split(",")
      .map(Number);
    return acc + a * b;
  }, 0);
  return sumsOfMuls;
}

function part2(input: string) {
  let sum = 0;
  const dontSplit = input.split("don't()");
  const firstMuls = part1(dontSplit[0]);
  sum += firstMuls ?? 0;
  for (const dont of dontSplit.slice(1)) {
    const lastDoIndex = dont.indexOf("do()");
    const sliced = dont.slice(lastDoIndex);
    const muls = part1(sliced);
    sum += muls ?? 0;
  }
  return sum;
}

async function getInput() {
  return Bun.file("./input.txt").text();
}

export {};

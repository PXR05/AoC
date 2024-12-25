# Advent of Code 2024

Solutions for Advent of Code 2024.

## Performance

Based on profiling results, most solutions run in under 1 second. The following days take longer and could benefit from optimization:

| Day | Time (seconds) |
| --- | -------------- |
| 9   | 64.08          |
| 16  | 22.94          |
| 7   | 17.48          |
| 20  | 6.21           |
| 22  | 4.38           |
| 18  | 3.16           |
| 19  | 2.74           |
| 6   | 2.72           |
| 14  | 2.17           |
| 23  | 1.94           |

All other solutions complete in under 1 second.

> Some solutions may need updated parameters when using the full input. (d14, d18)

> The above times are from running the solutions with my input on a Lenovo Legion 5 Pro with an AMD Ryzen 7 5800H processor.

## Usage

Run any day's solution:

```bash
./run.sh {day_number}   # e.g. ./run.sh 1
./run.sh -a             # Run all solutions
```

The solution will read from the `input` file in that day's directory and print the answers for both parts of the puzzle including the execution time.

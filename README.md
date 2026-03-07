# Programming Assignment 2: Greedy Algorithms

**Student Name:** Semyon Baykov

**UFID:** 65667853

## Instructions to Run
To run the code, you must have python installed and use the following command:
```bash
python src/greedy_algs.py <input_file>
```
```bash
python src/greedy_algs.py data/example.in
```

## Question 1: Empirical Comparison
| Input File | k | m | FIFO Misses | LRU Misses | OPTFF Misses |
|---|---|---|---|---|---|
| `test1.in` | 3 | 60 | 38 | 20 | 20 |
| `test2.in` | 3 | 56 | 28 | 30 | 16 |
| `test3.in` | 4 | 60 | 55 | 55 | 39 |

**Comments:**
- **Does OPTFF have the fewest misses?**

  Yes, in every test case, OPTFF consistently has the fewest misses.

- **How does FIFO compare to LRU?**

  The comparison depends on the access pattern:
  - In `test1.in`, LRU performs much better than FIFO because the sequence frequently reuses the same two items. LRU keeps these items because they are "recent," while FIFO evicts them because they were the "oldest" insertions.
  - In `test2.in`, FIFO performs slightly better than LRU. This happens because LRU evicts the least recently used, and if that specific item is needed again soon it backfires, while FIFO's simpler "oldest first" logic might keep it by chance.
  - In `test3.in`, which is a random pattern, they perform identically.
  - LRU generally outperforms FIFO in real-world workloads (more inputs and such).

## Question 2: Bad Sequence for LRU or FIFO
For (k=3), a sequence where OPTFF incurs strictly fewer misses:

**Sequence:** `1 2 3 4 1 2 3 4 1 2 3 4` (m=12) 

- **FIFO/LRU misses:** 12
- **OPTFF misses:** 6

**Reasoning:**
- In this sequence, there are 4 unique items being requested in a cycle of size (k+1).
- LRU/FIFO: Each time an item is requested, it has just been evicted to make room for the previous three. This results in a cache miss for every single request.
- OPTFF: When item 4 arrives, OPTFF looks ahead and sees that 1 and 2 are needed sooner than 3. It evicts 3 (the one farthest in the future). This allows it to hit on 1 and 2, reducing the total number of misses.

## Question 3: Prove OPTFF is Optimal
**Proof:**

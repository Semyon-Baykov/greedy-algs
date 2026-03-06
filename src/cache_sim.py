import sys
import collections


# Read file and returns k (capacity int) and requests (list of strings)
def parse_input(file_path):
    try:
        with open(file_path, 'r') as f:

            # Setup + don't read whitespace
            lines = f.readlines()
            lines = [line.strip() for line in lines if line.strip()]

            # Handle cases
            # Could be same line split
            if len(lines) < 2:
                content = " ".join(lines).split()
                if len(content) < 2: raise ValueError("Input file too short.")
                k = int(content[0])
                m = int(content[1])
                requests = content[2:]
            # Normal input
            else:
                header = lines[0].split()
                k = int(header[0])
                m = int(header[1])
                requests = []
                for line in lines[1:]:
                    requests.extend(line.split())

            # Out
            return k, requests

    except FileNotFoundError:
        print(f"Error: '{file_path}' not found.")
        sys.exit(1)

    except Exception as e:
        print(f"Input error: {e}")
        sys.exit(1)


# FIFO
def run_fifo(k, requests):
    pass


# LRU
def run_lru(k, requests):
    pass


# OPTFF
def run_optff(k, requests):
    pass



def main():
    # Check input
    if len(sys.argv) != 2:
        print("Usage: python src/cache_sim.py <input_file>")
        sys.exit(1)

    # Get input, parse it
    file_path = sys.argv[1]
    k, requests = parse_input(file_path)
    
    # Run simulations
    fifo_misses = run_fifo(k, requests)
    lru_misses = run_lru(k, requests)
    optff_misses = run_optff(k, requests)
    
    # Output results
    print(f"FIFO : {fifo_misses}")
    print(f"LRU : {lru_misses}")
    print(f"OPTFF : {optff_misses}")

if __name__ == "__main__":
    main()

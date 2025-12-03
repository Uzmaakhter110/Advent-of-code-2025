def max_joltage(bank: str) -> int:
    # bank is a string of digits, e.g. "2215452689..."
    max_val = 0
    n = len(bank)
    for i in range(n - 1):
        for j in range(i + 1, n):
            val = int(bank[i] + bank[j])  # form two-digit number
            if val > max_val:
                max_val = val
    return max_val

def main():
    total = 0
    with open("Day3\input.txt", "r") as f:
        for line in f:
            bank = line.strip()
            if not bank:
                continue
            total += max_joltage(bank)
    print(total)

if __name__ == "__main__":
    main()

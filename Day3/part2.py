def max_k_subsequence_digits(s: str, k: int) -> int:
    """
    Return the maximum possible integer formed by keeping exactly k digits
    from the digit string s, preserving their original order.
    """
    to_drop = len(s) - k           # how many digits we are allowed to remove
    stack = []

    for ch in s.strip():
        # While we can still drop digits and the last chosen digit is smaller
        # than the current one, drop it to get a larger resulting number.
        while to_drop > 0 and stack and stack[-1] < ch:
            stack.pop()
            to_drop -= 1
        stack.append(ch)

    # If we did not drop enough (e.g. non-decreasing string), trim from the end
    if len(stack) > k:
        stack = stack[:k]

    return int("".join(stack))


def main():
    k = 12  # exactly twelve batteries per bank

    total = 0
    with open("Day3\input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += max_k_subsequence_digits(line, k)

    print(total)


if __name__ == "__main__":
    main()

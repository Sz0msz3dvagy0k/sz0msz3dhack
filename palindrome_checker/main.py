import re


def is_palindrome(s):
  return s == s[::-1]


def count_unique_alnum(s):
  return len(set(s))


def process_string(s):
  filtered = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

  if not filtered:
    return "NO, -1"

  palindrome_result = "YES" if is_palindrome(filtered) else "NO"

  unique_count = count_unique_alnum(filtered) if palindrome_result == "YES" else -1

  return f"{palindrome_result}, {unique_count}"


def main():
  input_file = 'input.txt'
  with open(input_file, 'r') as file:
    lines = file.read().splitlines()

  for line in lines:
    result = process_string(line)
    print(result)


if __name__ == "__main__":
  main()
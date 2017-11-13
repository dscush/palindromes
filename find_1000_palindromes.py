import palindromes
import csv

if __name__ == "__main__":
    output = [("decimal", "smallest base in which the number is a palindrome")]
    for n in range(1, 1001):
        output.append((n, palindromes.find_lowest_palindrome_base(n)))
    with open('output.csv', 'w') as file_out:
        csv_out = csv.writer(file_out, quoting=csv.QUOTE_NONNUMERIC)
        csv_out.writerows(output)

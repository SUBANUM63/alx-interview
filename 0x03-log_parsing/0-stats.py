#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import sys


def print_stats(total_size, status_codes):
    """
    Prints the accumulated metrics:
    - Total file size
    - Count of status codes
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def process_line(line, total_size, status_codes):
    """
    Process a single line of log input.
    Updates total size and status codes count
    if the line is correctly formatted.
    """
    try:
        parts = line.split()
        if len(parts) < 9:
            return total_size

        # Extract the file size and status code
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        # Update total file size
        total_size += file_size

        # Update the count for the status code
        if status_code in status_codes:
            status_codes[status_code] += 1

    except (ValueError, IndexError):
        # If the line is not correctly formatted or parsing fails, we skip it
        pass

    return total_size


def main():
    total_size = 0
    status_codes = {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue

            total_size = process_line(line, total_size, status_codes)
            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        # Print the final stats when interrupted by CTRL+C
        print_stats(total_size, status_codes)
        raise

    # Print final stats after all lines are processed
    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()

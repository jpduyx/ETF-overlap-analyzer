import argparse
import petl as etl


def analyze_overlap(etf1_file, etf2_file, cache_file=None, output_file=None):
    # Load the ETF data
    etf1 = etl.fromcsv(etf1_file)
    etf2 = etl.fromcsv(etf2_file)

    # Perform overlap analysis
    overlap = etl.intersection(etf1, etf2)

    # Save results if output file is specified
    if output_file:
        etl.tocsv(overlap, output_file)
        print(f"Overlap results saved to {output_file}")
    else:
        # Print to console
        print(etl.look(overlap))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analyze ETF overlap.')
    parser.add_argument('etf1', help='Path to the first ETF CSV file')
    parser.add_argument('etf2', help='Path to the second ETF CSV file')
    parser.add_argument('--cache', help='Path to cache file (optional)', default=None)
    parser.add_argument('--output', help='Path to output file (optional)', default=None)

    args = parser.parse_args()

    analyze_overlap(args.etf1, args.etf2, args.cache, args.output)
import argparse
from generator import generate

def main():
    parser = argparse.ArgumentParser(description="AI Document Generator")
    parser.add_argument("--type", required=True, choices=["prd", "test_plan", "meeting_summary"])
    parser.add_argument("--input", required=True, help="Raw input text")
    parser.add_argument("--out", default="", help="Optional output file")
    args = parser.parse_args()

    doc = generate(args.type, args.input)
    print(doc)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(doc)

if __name__ == "__main__":
    main()

import sys
import predict
import pandas as pd
# imp.reload(LAD)


def main():
    inp = sys.argv[1]
    inp = pd.read_csv(inp)['0']
    detector = predict.LAD()
    detector.predict_results(inp)


if __name__ == "__main__":
    main()

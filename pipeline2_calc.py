import numpy as np
import re
from pathlib import Path

def main():
    fileList = Path("./lecture_files/pipe2_result").glob("pipe_perf2_*.txt")
    caseNum = 2

    cases = []

    for filePath in fileList:
        case = []
        with open(filePath) as f:
            lines = []
            for line in f:
                line = line.rstrip()
                lines.append(line)

            for l in lines:
                if ("Case" in l):
                    case.append(float(re.findall(r"\d+\.*\d*", l)[1]))

        cases.append(case)

    casesArray = np.array(cases)
    result = np.mean(casesArray, axis=0)

    for i in range(caseNum):
        print("Case " + str(i+1) + ":    " + str(result[i]))


if __name__ == "__main__":
    main()

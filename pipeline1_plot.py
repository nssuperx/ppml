import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import re
from pathlib import Path

def main():
    fileList = Path("./lecture_files/pipe1_result").glob("pipe_perf1_*.txt")
    caseNum = 5

    cases = []

    for filePath in fileList:
        case = []
        with open(filePath) as f:
            lines = []
            for line in f:
                line = line.rstrip()
                lines.append(line)

            for i in range(caseNum):
                    case.append(float(re.findall(r"\d+\.*\d*", lines[i])[2]))

        cases.append(case)

    casesArray = np.array(cases)
    result = np.mean(casesArray, axis=0)

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_title('time (ns)')
    ax.bar(range(1, caseNum + 1), result)
    plt.show()

    for i in range(caseNum):
        print("Case " + str(i+1) + ":    " + str(result[i]))


if __name__ == "__main__":
    main()

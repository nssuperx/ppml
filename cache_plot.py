import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import re

def main():
    sizeList = (128, 256, 512, 1024, 2048, 4096, 8192)
    caseNum = 5

    memSizes = []
    cases = {}
    
    for size in sizeList:
        memSize = []
        case = []
        for i in range(1, 6):
            times = []
            with open('./lecture_files/cache_result/norm_' + str(size) + '_' + str(i) + '.txt') as f:
                lines = []
                for line in f:
                    line = line.rstrip()
                    lines.append(line)

                memSize.append(int(re.findall(r"\d+", lines[0])[0]))

                for i in range(1, 6):
                    times.append(float(re.findall(r'\d+\.*\d*', lines[i])[1]))
            case.append(times)
        cases[str(size)] = case
        memSizes.append(memSize)

    caseArray = []
    for size in sizeList:
        caseArray.append(np.array(np.mean(cases[str(size)], axis=0)))
    caseArray = np.array(caseArray)
    memSizeArray = np.array(memSizes)
    plotMemSizeArray = np.mean(memSizeArray, axis=1)
    plotCaseArray = caseArray.T

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_title('time (ns)')
    ax.set_xscale('log', base=2)
    ax.set_xticks(sizeList)
    ax.set_xlabel('N')
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.grid(axis='both')
    for i in range(caseNum):
        ax.plot(sizeList, plotCaseArray[i], label='case ' + str(i+1))
    ax.legend()
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_title('Occupied memory size')
    ax.set_xscale('log', base=2)
    ax.set_yscale('log', base=2)
    ax.set_xticks(sizeList)
    ax.set_xlabel('N')
    ax.grid(axis='both')
    ax.plot(sizeList, plotMemSizeArray)
    plt.show()


if __name__ == "__main__":
    main()
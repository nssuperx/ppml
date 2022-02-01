from typing import Dict, List
import numpy as np
import matplotlib.pyplot as plt
import re
from pathlib import Path

trialNum = 3
procList = (1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24, 30, 40, 60)

class Result:
    def __init__(self, MPI_Initializing: float, Data_Reading: float, Transposing: float, Producting: float, Reducing: float, File_writing: float = 0.0) -> None:
        self.MPI_Initializing = MPI_Initializing
        self.Data_Reading = Data_Reading
        self.Transposing = Transposing
        self.Producting = Producting
        self.Reducing = Reducing
        self.File_writing = File_writing


def main():
    # ファイル読み込み
    trials = []
    for trial_count in range(0, trialNum):
        procResult = {}
        for proc in procList:
            results = []
            for procNo in range(0, proc):
                filePath = Path(f"./lecture_files/mpi_matmul/result_{trial_count}_{proc}/Elapse-{procNo}.txt")
                with open(filePath) as f:
                    lines = []
                    for line in f:
                        line = line.rstrip()
                        lines.append(line)

                MPI_Initializing = 0.0
                Data_Reading = 0.0
                Transposing = 0.0
                Producting = 0.0
                Reducing = 0.0
                File_writing = 0.0

                for l in lines:
                    n = float(re.findall(r"\d+\.*\d*", l)[0])
                    if("MPI_Initializing" in l):
                        MPI_Initializing = n
                    elif("Data_Reading" in l):
                        Data_Reading = n
                    elif("Transposing" in l):
                        Transposing = n
                    elif("Producting" in l):
                        Producting = n
                    elif("Reducing" in l):
                        Reducing = n
                    elif("File_writing" in l):
                        File_writing = n
                
                results.append(Result(MPI_Initializing, Data_Reading, Transposing, Producting, Reducing, File_writing))
            procResult[proc] = results
        trials.append(procResult)
    # ここまでファイル読み込み

    # 総計算時間 = Transposing + Producting + Reducing
    result_ave = []
    for proc in procList:
        one_trial = []
        for trial_count in range(0, trialNum):
            accum = []
            for procNo in range(0, proc):
                r = trials[trial_count][proc][procNo]
                accum.append(r.Transposing + r.Producting + r.Reducing)
            accum_array = np.asarray(accum, dtype=np.float64)
            one_trial.append(accum_array.mean())
        one_trial_array = np.asarray(one_trial, dtype=np.float64)
        result_ave.append(one_trial_array.mean())

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(procList, result_ave)
    plt.show()

    # Reduceの時間
    result_ave_reduce = []
    for proc in procList:
        one_trial = []
        for trial_count in range(0, trialNum):
            accum = []
            for procNo in range(0, proc):
                r = trials[trial_count][proc][procNo]
                accum.append(r.Reducing)
            accum_array = np.asarray(accum, dtype=np.float64)
            one_trial.append(accum_array.mean())
        one_trial_array = np.asarray(one_trial, dtype=np.float64)
        result_ave_reduce.append(one_trial_array.mean())

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(procList, result_ave_reduce)
    plt.show()


if __name__ == "__main__":
    main()
import numpy as np
import matplotlib.pyplot as plt
import fire

def loadText(filename,c):
    with open(filename,"r") as f:
        return np.array([float(line.split(",")[c]) for line in f.readlines()])

class csvplot:
    def plot(self,input_file, output_file = "output.png",xc = 0,yc = 1,
            fontsize = 18, xlabel = "x-axis", ylabel = "y-axis", color = "k",
            xmax = float("nan"), xmin = float("nan"), ymax = float("nan"), ymin = float("nan")):

        # load
        y = loadText(input_file,yc)
        x = loadText(input_file,xc)
        plt.plot(x,y,'k')

        # 軸ラベル
        plt.xlabel(xlabel, fontsize = fontsize)
        plt.ylabel(ylabel, fontsize = fontsize)

        # 最大最小
        if xmax != xmax:
            xmax = float(len(x))
        if xmin != xmin:
            xmin = 0
        if ymax != ymax:
            ymax = max(y)
        if ymin != ymin:
            ymin = min(y)
        plt.xlim(xmax = xmax, xmin = xmin)
        plt.ylim(ymax = ymax, ymin = ymin)

        # いい感じに調整
        plt.tight_layout()

        # 出力
        plt.savefig(output_file)

if __name__ == '__main__':
    fire.Fire(csvplot)

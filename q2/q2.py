import csv
import random
import matplotlib.pyplot as plt

samples = [100, 1000, 10000, 100000]
datas = {
	"100": [],
	"1000": [],
	"10000": [],
	"100000": [],
}
X = [ i for i in range(1, 7) ]

def run(sample) :
	for _ in range(sample) :
		dice = random.randint(1, 6)
		datas[f"{sample}"].append(dice)


	f = open(f"sampled_{sample}.csv", "w", encoding="cp949")

	f.write("number\n")
	for num in datas[f"{sample}"] :
		f.write(str(num) + "\n")

	f.close()

def draw(sample, idx) :
	plt.subplot(2, 2, idx)

	plt.title(f"Dice Sampling {sample}")

	plt.hist(datas.get(f"{sample}"), width=0.25)
	plt.axhline(y = sample / 6, color='r', linewidth=1, label="avg")
	plt.ylabel("count")
	plt.xlabel("number")
	plt.legend()

def main() :
	plt.figure(figsize=(8,8))
	idx = 1
	for sample in samples :
		run(sample)
		draw(sample, idx)
		idx += 1
	plt.savefig("q2-1.png")
	plt.tight_layout()
	plt.show()


if __name__ == "__main__" :
	main()
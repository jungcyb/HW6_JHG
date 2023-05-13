import csv
import matplotlib.pyplot as plt

total = []
male = []
female = []
ratio = []
year = []

def readCsv(filename) :
	f = open(filename, 'r', encoding='cp949')
	data = csv.reader(f, delimiter=',')

	header = next(data)
	# 0 "시점", 1 인구 (명), 2 남자 (명), 3 여자 (명), 4 성비
	for row in data :
		if(row[0] == '' or row[1] == '' or row[2] == '' or row[3] == '' or row[4] == '') : continue
		year.append(row[0])
		total.append(int(row[1]))
		male.append(int(row[2]))
		female.append(int(row[3]))
		ratio.append(float(row[4]))
	f.close()

def main() :
	readCsv("jeju_gender.csv")
	fig, ax1 = plt.subplots()
	plt.title("Jeju Population info")
	plt.xlabel("years")
	
	ax1.bar(year, total, label="total", width=0.8, color="gray")
	ax1.bar(year, female, label="female", width=0.4)
	ax1.bar(year, male, label="male", width=0.2)
	ax1.set_ylabel("population count")
	ax1.legend()

	ax2 = ax1.twinx()
	ax2.plot(year, ratio, label="ratio", color="red")
	ax2.set_ylabel("ratio (%)")
	ax2.axhline(y = 100, color='g', linewidth=1)
	ax2.legend()

	plt.xticks(year)
	plt.savefig("q3-1.png")
	plt.show()


if __name__ == "__main__" :
	main()
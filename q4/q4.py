import csv
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] ='Malgun Gothic'
rcParams['axes.unicode_minus'] =False

ride_sort = []
off_sort = []
total_sort = []

def readCsv(filename) :
	f = open(filename, 'r', encoding='cp949')
	data = csv.reader(f, delimiter=',')

	#호선명,역ID,지하철역,07:00:00~07:59:59,,08:00:00~08:59:59,
	#,,,승차,하차,승차,하차

	next(data)
	next(data)
	# 0 호선명, 1 역ID, 2 서울역, 3 43763, 4 112497, 5 74004, 6 237172
	for row in data :
		total_sum = 0
		ride_sum = 0
		off_sum = 0

		for i in range(0, 7) :
			if row[i] == '' :
				continue		
		station = row[2] + f"\n({row[0]})"
		
		range78_ride = int(row[3])
		range78_off = int(row[4])

		range89_ride = int(row[5])
		range89_off = int(row[6])

		total_sum += range78_ride + range78_off + range89_ride + range89_off
		ride_sum += range78_ride + range89_ride
		off_sum += range78_off + range89_off

		ride_sort.append([ride_sum, station])
		off_sort.append([off_sum, station])
		total_sort.append([total_sum, station])

	f.close()


def analyze() :		
	ride_sort.sort()
	off_sort.sort()
	total_sort.sort()
	plt.figure(figsize=(16, 6))
	plt.rc('font', size=3)
	addPlt(ride_sort, 1, "ride")
	addPlt(off_sort, 2, "off")
	addPlt(total_sort, 3, "total")
	plt.savefig("q4-1.png", dpi = 500)
	plt.tight_layout()
	plt.show()

def addPlt(sorted_result, idx, title) :
	plt.subplot(3, 1, idx)
	plt.title(f"Top 30 Stations in '{title}'")
	stations = []
	cnt = []
	for i in range(len(sorted_result) - 1, len(sorted_result) - 31, -1) :
		if title == "total" :
			print(-(i - len(sorted_result)), sorted_result[i][1], sorted_result[i][0])
		stations.append(sorted_result[i][1])
		cnt.append(sorted_result[i][0])
	plt.bar(stations, cnt)
	plt.ylabel("population count")
	
	for i, v in enumerate(stations):
		plt.text(v, cnt[i], cnt[i],
				fontsize = 4, 
				color='black',
				horizontalalignment='center',
				verticalalignment='bottom')

def main() :
	readCsv("q4.csv")
	analyze()

if __name__ == "__main__" :
	main()
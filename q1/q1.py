import csv
import matplotlib.pyplot as plt

datas = {
	"all": [],
	"seoul(108)": [],
	"daejeon(133)": [],
	"busan(159)": [],
	"jeju": []
}

diffs = {
	"all": [],
	"seoul(108)": [],
	"daejeon(133)": [],
	"busan(159)": [],
	"jeju": []
}

months = [ i for i in range(1, 13) ]

def readCsv(filename, label) :
	f = open(filename, 'r', encoding='cp949')
	data = csv.reader(f, delimiter=',')

	header = next(data)
	# 0 년월, 1 지점, 2 평균기온(℃), 3 평균최저기온(℃), 4 평균최고기온(℃)
	for row in data :
		if(row[2] == '' or row[3] == '' or row[4] == '') : continue
		datas[label].append(float(row[2]))

	f.close()

def analyze(label) :
	cold_cnt = 0
	hot_cnt = 0
	same_cnt = 0
	res = [f"{i + 1}월 : " for i in range(0, 12)]
	for i in range(0, 12) :
		diff = datas.get(label)[i] -  datas.get("all")[i]
		if  diff > 0 :
			hot_cnt += 1
		elif diff < 0 :
			cold_cnt += 1
		else :
			same_cnt += 1
		res[i] += str(round(diff, 3)) + "Celcius"
	diffs[label] = res
	return { "hot": hot_cnt, "cold": cold_cnt, "same": same_cnt }

def main() :
	readCsv("temp_all.csv", "all")
	readCsv("temp_seoul.csv", "seoul(108)")
	readCsv("temp_daejeon.csv", "daejeon(133)")
	readCsv("temp_busan.csv", "busan(159)")
	readCsv("temp_jeju.csv", "jeju")

	plt.title("Average Temperature for Korean Cities (Jan ~ Dec)")

	plt.plot(months, datas.get("all"), label="all")
	plt.plot(months, datas.get("seoul(108)"), label="seoul(108)")
	plt.plot(months, datas.get("daejeon(133)"), label="daejeon(133)")
	plt.plot(months, datas.get("busan(159)"), label="busan(159)")
	plt.plot(months, datas.get("jeju"), label="jeju")

	plt.xticks(months)
	plt.ylabel("celsius")
	plt.xlabel("months")
	plt.legend()
	plt.savefig("q1-1.png")
	plt.show()

	for region in datas.keys() :
		if region == "all" : continue
		res = analyze(region)
		status = "특별히 더 춥거나 덥지 않다"
		if res["hot"] > res["cold"] :
			status = "더 더운 달이 추운 달보다 더 많아 더 덥다."
		if res["hot"] < res["cold"] :
			status = "더 추운 달이 더운 달보다 더 많아 더 춥다."
		print(f"{region} 지역은 전국에 비해\n추운 달은", res["cold"], "만큼,\n더운 달은 ", res["hot"], " 만큼 있음으로\n", status, "\n")
		print("온도차 : \n", diffs[region], "\n")
if __name__ == "__main__" :
	main()
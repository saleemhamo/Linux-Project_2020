import csv
import statistics

import numpy as np

from Loan import *

data = []

with open('data.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			line_count += 1
			continue
		# print(row[1])
		data.append(Loan(row[0], row[1], row[2], row[3], row[4], row[5]))
		line_count += 1


def find_total_amount(data):
	sum = 0
	for i in range(0, 25):  # data samples = 25
		sum += int(data[i].loan_amount)
	return sum


def find_average_amount(data):
	sum = 0
	for i in range(0, 25):  # data samples = 25
		sum += int(data[i].loan_amount)
	return sum / 25


def find_min_loan(data):
	# min_loan = min(data, key=lambda x: x.loan_amount)
	# min_loan = min(data, key=attrgetter('loan_amount'))
	min = 100000
	for i in range(0, 25):  # data samples = 25
		if min > int(data[i].loan_amount):
			min_loan = data[i]
			min = int(data[i].loan_amount)

	return min_loan


def find_max_loan(data):
	# min_loan = min(data, key=lambda x: x.loan_amount)
	# min_loan = min(data, key=attrgetter('loan_amount'))
	max = 0
	for i in range(0, 25):  # data samples = 25
		if max < int(data[i].loan_amount):
			max_loan = data[i]
			max = int(data[i].loan_amount)

	return max_loan


def find_min_loan_country(data):
	return find_min_loan(data).country_name


def find_max_loan_country(data):
	return find_max_loan(data).country_name


def variance_of_loans(data):
	loan_amounts = []
	for i in range(0, 25):
		loan_amounts.append(int(data[i].loan_amount))

	a = np.array(loan_amounts, dtype=int)
	return np.var(a, dtype=np.float)

def Avarage_Amount_of_Country(data,county):
	total = 0
	counter = 0
	for i in range(0, 25):
		if data[i].country_name.equals(county):
			total = total+data[i].loan_amount
			counter = counter+1
	result = total/counter
	return result

def Avarage_time_per_dollar(data, id):
	time = 0
	dollar = 0
	for i in range(0, 25):
		if data[i].id == id:
			time += int(data[i].time_to_raise)
			dollar += int(data[i].loan_amount)
	if dollar != 0:
		result = time / dollar
	else: result = 0
	return result
#testing only
def sortData(data):
	data.sort()
	print(data)
	return
sortData(data)

#print(Avarage_time_per_dollar(data,212763))
#Avarage_Amount_of_Country(data,"Bolivia")

	# country_set = {}
	# for i in range(0,25):
	# 	country_set.add(data[i].country_name)
	# country_set.

#
# print(find_max_loan(data).loan_amount)
# print(find_average_amount(data))

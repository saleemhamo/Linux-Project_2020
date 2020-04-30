import csv
from os import system, name
import statistics

import numpy as np
from setuptools._vendor.six import print_

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


def clear():
	# for windows
	if name == 'nt':
		_ = system('cls')
	return
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


def avarage_amount_of_country(data, county):
	total = 0
	counter = 0
	for i in range(0, 25):
		if data[i].country_name == county:
			total = total + int(data[i].loan_amount)
			counter = counter + 1
	result = total / counter
	return result


def avarage_time_per_dollar(data, id):
	time = 0
	dollar = 0
	for i in range(0, 25):
		if int(data[i].id) == int(id):
			time += int(data[i].time_to_raise)
			dollar += int(data[i].loan_amount)
	if dollar != 0:
		result = time / dollar
	else:
		result = 0
	return result


# testing only
def sortData(data):
	print("1-sort on id")
	print("2-sort on loan amount")
	print("3-sort on country name")
	print("4-sort on status")
	print("5-sort on time to raise")
	print("6-sort on num lenders total")
	choice = input("please enter your choice")
	if choice == '1':
		data.sort(key=lambda x: x.id)

	if choice == '2':
		data.sort(key=lambda x: x.loan_amount)

	if choice == '3':
		data.sort(key=lambda x: x.country_name)

	if choice == '4':
		data.sort(key=lambda x: x.status)

	if choice == '5':
		data.sort(key=lambda x: x.time_to_raise)

	if choice == '6':
		data.sort(key=lambda x: x.num_lenders_total)
	print("Ordered List :")
	for i in range(0, 25):
		print(("id:{},loan_amount{},country:{},status:{},time to raise:{},num lenders total:{},").format(data[i].id,
																									data[i].loan_amount,
																									data[
																										i].country_name,
																									  data[i].status,
																									data[
																										i].time_to_raise,
																									data[
																										i].num_lenders_total))

	return

def menu(data):
	ch='1'
	t= 0
	print("***LINUX SECOND PROJECT MENU***")
	while ch != 0:
		t = 0
		print("1-The total amount of money loaned.")
		print("2-The average loan amounts.")
		print("3-The largest/smallest loan.")
		print("4-The country got the largest/smallest loan.")
		print("5-The variance of the money loaned.")
		print("6-The average amount of loans made to people per given country")
		print("7-The average amount of time / dollar it takes to fund a loan")
		print("8-Sort the based-on user input attributes.")
		print("0-EXIT")
		ch = input("please enter your choice ~~>")
		if ch == '1':
			t=1
			print(("total  = {} ").format(find_total_amount(data)))
		if ch == '2':
			t = 1
			print(("Avarage = {}").format(find_average_amount(data)))

		if ch == '3':
			t = 1
			print(("Minmum loan ={}").format(find_min_loan(data).loan_amount))
			print(("Max loan={}").format(find_max_loan(data).loan_amount))

		if ch == '4':
			t = 1
			print(("Minmum country loan = {} ").format(find_min_loan_country(data)))
			print(("Maximum County loan = {}").format(find_max_loan_country(data)))
		if ch == '5':
			t = 1
			print(("Variance = {} ").format(variance_of_loans(data)))
		if ch == '6':
			t = 1
			county = input("please enter  the country name:")
			print(("The avarge loan amount of the country = {} ").format(avarage_amount_of_country(data, county)))
		if ch == '7':
			t = 1
			id = input("please enter the id of the loan:")
			print(avarage_time_per_dollar(data, id))
		if ch == '8':
			t = 1
			sortData(data)
		if t == 0:
			print_("INVALID CHOICE!--> Try again please")
		res = '0'
		while res != '1' :
			res = input("please enter 1 to back to menu~~>")
	return
menu(data)

from bs4 import BeautifulSoup
import requests
import re
import os
from git import Repo

SUBMISSION_BASE_URL = "https://codeforces.com/contest/"
BASE_URL = "https://codeforces.com/submissions/"

def fetch_data(url):
	"""
	Fetch HTML data from the given url
	"""
	print("Fetching Data from " , url)
	content = requests.get(url)
	soup = BeautifulSoup(content.text , 'html.parser')
	return soup


def save_local(number , name , code , lang='cpp'):
	"""
	Save the date in local file
	/number/name.lang
	"""
	curr_dir = os.getcwd()
	req_dir = os.path.join(curr_dir , number)
	if not os.path.exists(req_dir):
		os.mkdir(req_dir)
	os.chdir(req_dir)
	name += '.' + lang
	req_dir = os.path.join(req_dir , name)
	# print(req_dir)
	if os.path.exists(req_dir):
		os.chdir(curr_dir)
		return
	file = open(name , 'w')
	cnt = 0
	lines = code[0].split('\n')
	for line in lines:
		file.write(line)
	file.close()
	os.chdir(curr_dir)


def fetch_accepted_code(row , list_of_ids , file):
	"""
	Fetch the accepted solutions
	"""
	print("Fetching Accepted Solutions")
	id_cell = row.find('td' , {'class' : 'id-cell'})
	id = id_cell.get_text().strip()
	file.write(id)
	if id in list_of_ids:
		return
	td_cols = row.find_all('td' , {'class' : 'status-small'})
	problem_name = None
	for td in td_cols:
		anchorTag = td.find('a')
		if anchorTag is not None:
			problem_no = anchorTag['href'].split('/')[2]
			problem_name = problem_no + anchorTag.get_text().strip()
	print(problem_no , problem_name , sep = ' ')
	final_url = SUBMISSION_BASE_URL + problem_no + '/submission/' + id
	soup = fetch_data(final_url)
	code_area = soup.find('pre')
	code = []
	for line in code_area:
		code.append(line)
	save_local(problem_no , problem_name , code)


def find_accepted_solutions(soup , list_of_ids , file):
	"""
	Find the accepted solutions
	"""
	print("Finding Accepted Solutions")
	sol_table = soup.find('table' , {'class' : 'status-frame-datatable'})
	rows = sol_table.find_all('tr')
	cnt = 0 
	for row in rows:
		if(cnt == 0):
			cnt += 1
			continue
		if(row.find('td' , {'class' : 'status-cell'}).find('span')['submissionverdict'] == 'OK'):
			cnt += 1
			fetch_accepted_code(row , list_of_ids , file)
		# if cnt == 2:
		# 	break

def get_max_pageno(url):
	soup = fetch_data(url)
	page_indexes = soup.find_all('span' , {'class' : 'page-index'})
	max_index = 1
	for page_index in page_indexes:
		max_index = page_index.get_text()
	return max_index


def main():
	handle_name = None
	handle_name = input("Enter Handle Name(Case Sensitive) : ")
	curr_dir = os.getcwd()
	req_dir = os.path.join(curr_dir , handle_name)
	if not os.path.exists(req_dir):
		os.mkdir(req_dir)
		# repo = Repo.init(req_dir)
		filename = req_dir + '/idlist.txt'
		file = open(filename , 'w')
		file.close()
	os.chdir(req_dir)
	file = open('idlist.txt' , 'r')
	list_of_ids = []
	list_of_ids = file.readlines()
	file.close()
	final_url = BASE_URL + handle_name
	max_pages = get_max_pageno(final_url)
	print(max_pages)
	file = open('idlist.txt' , 'w')
	for i in range(int(max_pages) , 0 , -1):
		page_url = final_url + '/page/' + str(i)
		soup = fetch_data(page_url)
		find_accepted_solutions(soup , list_of_ids , file)
		# break
	file.close()


if __name__ == '__main__':
	main()

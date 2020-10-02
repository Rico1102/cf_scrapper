# cf_scrapper
Tool to create a local copy of your Accepted solutions from CodeForces and upload it into your github repo


Required Library Names is mentioned in requirements.txt
Run the following command before running the cf_scrapper

Requirements
```bash
pip install -r requirements.txt
```

To run the scrapper

```bash
git clone https://github.com/Rico1102/cf_scrapper
cd cf_scrapper
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

run
python cf_scrapper.py
```

## Current Features
--**Creates a local folder with handle_name**\
	handle_name is required as the input(Case Sensitive)\
	A local Folder is created with the handle_name which will store all the accepted results,\
	Folder Structure\
	handle_name\
		&nbsp;&nbsp;&nbsp;|\
		&nbsp;&nbsp;&nbsp;|--Contest-Number\
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|\
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--Problem No - Problem Name\
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|\
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--Accepted Solution(Latest)\
--**Upload to Github Repo**
--**Only Supports C++ submissions**


## Features to be tested
--**Upload to Github Repo**


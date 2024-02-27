from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=java&txtLocation='
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for company_name, job in enumerate(jobs):
        if "few" in job.find('span', class_='sim-posted').text:
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            skills = job.find('span', class_='srp-skills').text.strip().replace(' ', '')
            link = job.header.h2.a['href']
            with open(f'Web_Scraping/posts/{company_name}.txt', 'w') as f:
                f.write(f'Company Name: {company_name}\n')
                f.write(f'Required Skills: {skills}\n')
                f.write(f'Link To Apply: {link}\n')
                print(f'File Saved: {company_name}')
            
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 24
        print(f"Waiting {time_wait} hours...")
        time.sleep(time_wait * 60 * 60)
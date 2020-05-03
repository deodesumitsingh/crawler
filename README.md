# CRAWL-IT

  
### Overview  
Simple web crawler that can be used to generate all links of specifed URL.  
  
### UseCase  
Crawler can be used to generate sitemap of a domain.  
  
### Setup
Python Version >= 3.2
```
python3 -m venv .venv/
source .venv/bin/activate
pip install -r requirements.txt
```  
  
### Usage
Crawler can be used as.  
`python3 main.py -u/--url url_to_be_crawled -d/--depth upto_what_depth`.  
Example:-  
`pytho3 main.py --url https://github.com --depth 2`.  
In the above example we are crawling `github` upto `depth` of `2`
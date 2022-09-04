from bs4 import BeautifulSoup
import requests
import os


# Using request to get the html for nbcnews
webpage = requests.get("https://www.nbcnews.com/us-news")
doc = BeautifulSoup(webpage.text, "html.parser")

# Filtering through the html code to get all the top 14 headlines
frontlines = doc.findAll('span', attrs={'class':'tease-card__headline'})
headlines = doc.findAll('h2', attrs={'class':'wide-tease-item__headline'})



# Saving all 14 headlines in a txt file
save_path = 'nbc_scrape'
name_of_file = 'news_report'
completeName = os.path.join(name_of_file+".txt")
text_file = open(completeName,'w')


# Iterating through all the headlines and links to the headline
column = 1
count = 0

for frontline in frontlines:
    text_file.writelines([str(column) + '. ' + frontline.text,'\n' , frontlines[count].parent.get('href'), '\n','\n'])
    column += 1
    count += 1

count = 0
for headline in headlines:
    text_file.writelines([str(column) + '. ' + headline.text, '\n', headlines[count].parent.get('href'), '\n', '\n'])
    column += 1
    count += 1

text_file.close()

# Shows that the scrape was sucessful and gives the directory on where the txt is stored
print()
print('File name: ' + name_of_file + '.txt')
print('File destination: ' + save_path)

# opens the txt file when the program closes
input('Press enter to exit ')
os.startfile('news_report.txt')















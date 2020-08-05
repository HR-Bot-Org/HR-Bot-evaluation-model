import wikipediaapi
from googlesearch import search

class Parser:

    def __init__(self, skill):
        self.skill = skill

    def parseForCoursera(self):
        senteces = self.skill.split()
        search_key = ''
        
        for i in range(len(senteces)-1):
            search_key+=senteces[i]
            search_key+='%20'
        search_key+= senteces[i+1]

        return search_key

    def parseForUdemy(self):
        senteces = self.skill.split()
        search_key = ''
        
        for i in range(len(senteces)-1):
            search_key+=senteces[i]
            search_key+='+'
        search_key+= senteces[i+1]

        return search_key

    def parseForPuralsight(self):
        return Parser.parseForCoursera(self)

    def parseForLynda(self):
        return Parser.parseForUdemy(self)

class FeedBack:

    
    def __init__(self, skill, question):
        self.skill = skill
        self.question = question
        self.webSitesDictionary = {
            'Algorithms': ['www.geeksforgeeks.org'],
            'DataBase': ['www.w3schools.com'],
            'SoftWareEngineering': ['www.tutorialspoint.com', 'stackoverflow.com'],
            'DataScience': ['www.datacamp.com'],
            'machine learning': ['www.datacamp.com']
            }

    #Done
    def wikipediaSearch(self):
        wiki_wiki = wikipediaapi.Wikipedia('en')
        page_py = wiki_wiki.page(self.skill)
        print(page_py.summary)
    
    def googleSearch(self):
        skill = self.skill
        sites = self.webSitesDictionary[skill]
        question = self.question

        for site in sites:
	        query = 'site:' + site + ' ' + question + ' + ' + skill
	        for j in search(query, tld="com", num=10, stop=1, pause=2): 
		        print(j) 
    
    #Done
    def courseraSearch(self):
        p = Parser(self.skill)
        search_key = p.parseForCoursera()
        link = 'https://www.coursera.org/search?query=' + search_key
        print(link)

    #Done
    def udemySearch(self):
        p=Parser(self.skill)
        search_key = p.parseForUdemy()
        link = 'https://www.udemy.com/courses/search/?q=' + search_key
        print(link)
    
    #Done
    def pluralsightSearch(self):
        p=Parser(self.skill)
        search_key  = p.parseForPuralsight()
        link = 'https://www.pluralsight.com/search?q=' + search_key
        print(link)

    def lyndaSearch(self):
        p=Parser(self.skill)
        search_key  = p.parseForLynda()
        link = 'https://www.lynda.com/search?q=' + search_key
        print(link)

    def search(self):
        print('you want to emprove your '+ self.skill + ' skills\nso we present some titles, documents and courses to help you\n\n')
        self.wikipediaSearch()
        self.googleSearch()
        self.courseraSearch()
        self.udemySearch()
        self.pluralsightSearch()
        self.lyndaSearch()

# p = Parser('machine learning andrew eg')
# print(p.parseForCoursera())
if __name__ == "__main__":
    
    f = FeedBack('machine learning', 'what is the decision tree' )
    f.search()
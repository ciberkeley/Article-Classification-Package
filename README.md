# README #

This is the readme for the Capital Investments at Berkeley
Article Scoring Package. This package is part of the Software
Group's Spring 2016 Project on news analytics and natural language
processing. 

### Background on Package and Spring 2016 Software Group ###

* The Software Group built a set of scrapers to read and record article entries
  in the results of user selected queries
* These articles, once read and recorded, are added to a mongoDB collection
    * Future intentions include building out the infrastructure to provide 
      each club member a unique article collection to maintain and populate
* As article data is added to mongoDB, text within articles is easily queryable  
  and simple to aggregate
    * This allows for text analytics to be performed on query results


### Goal ###

* The Software Group intends to create a postive/negative article classifier
  using logistic regression

### What is this package for? ###

* This package is meant to implement CIB's mongoDB infrastructure. 
* Users of the package will be able to:
    * Add new website query results to mongoDB
    * Query articles already on mongoDB
    * Classify articles as positive/negative
    * Pull classification grade history for analysis

### How do I get set up? ###

* Open your Terminal(Mac) or  CommandLine(Windows)

* NOTE: All lines beginning with "$" indicate you should enter than line in your terminal
* NOTE: You will need a USERNAME and PASSWORD from mongoLab.
* NOTE: You will need to download "MiniConda: Python 2.7"
    * http://conda.pydata.org/miniconda.html
    (On a Mac)
    $ cd Downloads
    $ bash Miniconda2-latest-MacOSX-x86_64.sh

* NOTE: You will need to create an environment
    $ conda create -n py2k python=2.7

* NOTE: You will need to activate py2k as your environment
    $ source activate py2k

* Change directories ($ cd DESIRED-DIRECTORY) to a folder you would like to save the ArticleClassificationPackage
* Enter the following commands into your terminal
    $ git clone https://github.com/ciberkeley/Article-Classification-Package.git
        * This will copy the package into your current directory/folder
        * You can also retrieve this package by unzipping an Article-Classification-Package.zip file
          in the desired directory/folder
    $ cd Article-Classification-Package
    $ python setup.py develop
    $ python
    >>> import ArticleClassificationPackage as ACP
    >>> acp = ACP.ArticleClassificationPackage(USERNAME, PASSWORD)
    >>> article = acp.get_article()
    >>> article_text = acp.get_text(article)
    >>> acp.classify(article, _class = 0)
        * This will get an article, save the article_text, and classify the article as negative 
          under your provided user credentials

### Operation Guidelines ###

* As show in the previous section, there are methods to get and article, extract the article text for reading, and classify the article as positive (1) or negative (0).
* All articles are pulled from the 'articles' collection from the  Capital Investments at Berkeley mongoDB
* All user classifications are saved to the 'classify' collection in the Capital Investments at Berkeley mongoDB
* NOTE: You can only classify an article as positive or negative.
    * Odd Integers indicate positive articles
    * Even Integers indicate negative articles
    * Non-Integers will return an error 

### Contribution guidelines ###

* (To be edited)

### Who do I talk to? ###

* Brandon Flannery | bflannery@ciberkeley.com

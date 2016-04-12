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

* cd  ~/.../Article-Scoring-Package
* python setup.py install

### Operation Guidelines ###

* (To be edited)

### Contribution guidelines ###

* (To be edited)

### Who do I talk to? ###

* Brandon Flannery | brandon.flannery@pluribuslabs.com

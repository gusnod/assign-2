Assignment 2
============

This folder contains the starter files for Assignment 2, which is about solving a clustering problem.

Note that the training and test data files are ~220MB and therefore they are not posted on GitHub. You need to download them:

  - <http://www3.ux.uis.no/~balog/dat630/a02training.zip>
  - <http://www3.ux.uis.no/~balog/dat630/a02test.zip>

Submission is done by **pushing the necessary files to GitHub, before Oct 12, 23:59**. 
There is a website (see below) to check if you passed the required threshold. 


## Task

You receive as input the top documents retrieved by a web search engine using a person names as query. The content of each document is provided, as well as the original document ranking data (document rank, URL, title, snippet).

The output must be a clustering of the web pages, where each cluster is assumed to contain all (and only those) pages that refer to the same individual.
It might be the case that different people with the same name may be mentioned simultaneously in the same document (this happens frequently in genealogies, Wikipedia pages and lists of authors). If this is the case, the document should appear in all the necessary clusters.

**Deadline: Oct 12, 23:59**


## Data

### Training data

The training data is composed of sets of up to 100 web pages corresponding to the results from a web search engine for a person name query. The training set consists of 49 names in total.

The sample is expected to cover at least two frequently occurring ambiguity scenarios: very common names that have a high ambiguity on the web, and names of famous or historical people, which might monopolize most of the documents in web search results.

Each name set has a `person_name.xml` file with information about ranking, URL, title and snippet for each retrieved web page. (Note that title and snippet are not available for all names in the training set.)
All the web pages have been downloaded and stored in a `docs` directory. (There might be missing documents, i.e., listed in the xml file but not found under docs; these should be ignored.)

Download the training data files from <http://www3.ux.uis.no/~balog/dat630/a02training.zip>.


### Gold standard

The gold standard for each person-name document set is named as `person_name.clust.xml`. It contains a root element `<clustering>` followed by one `entity` element for each entity. The entity element has an identifier attribute (`id`) with an integer value (it has to be unique, but it does not have to be continuous). Nested in the `entity` element there are `doc` elements (pages that refer to this particular entity), each of which has a `rank` attribute that corresponds to the ranking information provided in the `person_name.xml` file described above.

Note that a document might have been clustered in more than one entity. This is the case when multiple person names referring to different entities appear in a single document. Also, note that a person name may have a namesake that is not a person (for instance an organization or a location). In those cases the non-person entity will have its own cluster.
Finally, when the annotator could not cluster a page it was included under a `discarded` element. The reasons for this might be the non-occurrence of the person name in the page (probably because the web search engine had outdated information when the corpus was built) or simply that the human annotator could not decide whether to cluster that page. Discarded pages are not taken into account for the evaluation.

Here is an example of what the gold standard files looks like:
```
<clustering>
   <entity id="0">
       <doc rank="0"/>
       <doc rank="5"/>
   </entity>
   <entity id="1">
       <doc rank="1"/>
       <doc rank="3"/>
       <doc rank="5"/>
       <doc rank="10"/>
   </entity>
   ...
   <discarded>
       <doc rank="8"/>
       <doc rank="9"/>
   </discarded>
</clustering>
```

Note that empty lines are permitted anywhere in the file. Spaces and tabs do not have any special meaning in the file.


### Baselines

Two naive baseline clusterings are provided for the training data. These are found under `training.bl`. The script used to generate the baselines is also made available (`baselines.py`).

  - One-in-one: Each document is assigned to a cluster on its own 
  - All-in-one: All documents are assigned to a single cluster 

One-in-one achieves perfect purity, while all-in-one achieves perfect inverse purity, if each document is assigned to a single cluster (which is nearly always the case).
    

### Evaluation 

The scorer, written in Java, implements the standard clustering evaluation measures of "purity" and "inverse purity". From the command line you can execute it like this:

```
$ java -cp weps_scorer.jar es.nlp.uned.weps.evaluation.Scorer person_ground_truth.xml person_clustering.xml
```

There is an additional python script `eval.py` that performs the evaluation on a set of names (e.g., the entire training set), and displays the F1-score averaged over all names in the set.  It takes as input two directories: one with the ground truth files and another with the automatically generated clusterings. 
For example, evaluating the all-in-one baseline goes as follows:

```
python eval.py training.gt training.bl/all-in-one
```


### Test data

The test data is in the same format as the training data. You are expected to provide an output clustering for each person name  set in the test set (30 names in total). The format of this output should be the same as the gold standard format described above.
The data output for each person name set should be created in one separate file.
The files should be placed under the `output` folder and named `person_name.clust.xml`. 

The baseline performance on the test data is the following

| Method      | Pur.    | Inv.pur | F-score | 
| ----------- | ------- | ------- | ------- |
| All-in-one  |   0.288 |   1.000 |   0.448 |
| One-in-one  |   0.999 |   0.475 |   0.643 |

**The minimum F-score for passing the assignment is 0.7.**

Download the test data files from <http://www3.ux.uis.no/~balog/dat630/a02test.zip>.


## Submission

You need to submit the code, output files, and report on GitHub to the repository *that will be created* for your team `uis-dat630-fall2015/{teamname}-assignment-2`.


### Online evaluation and Leaderboard

An online interface *will be provided* where you can evaluate the clustering you generated for the test data (i.e., to check if you passed the threshold and to see how you compare against other teams).

*A URL will be provided here soon.*

However, for this task, **you will be given only 3 attempts to test your performance online** (this is to avoid tuning your clustering method on the test data). 

The **best performing team gets 5 bonus points at the exam** (all members).
And, there is more. **Each team that manages to reach over 0.8 F-score gets 5 bonus points at the exam**.


## Reading

Two relevant research papers presenting some clustering approaches for this very task:

  - Resolving Person Names in Web People Search, K. Balog, L. Azzopardi, and M. de Rijke. In: R. Baeza-Yates and I. King, editors, Weaving Services, Location, and People on the WWW, pages 301-324, Springer, July 2009. [PDF](http://krisztianbalog.com/files/springer2008-webpeople.pdf)
  - Comparison of Retrieval-Based Hierarchical Clustering Approaches to Person Name Disambiguation. Christof Monz and Wouter Weerkamp. In Proceedings of the 32nd Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, pages 650-651, 2009. [PDF](https://staff.science.uva.nl/c.monz/html/publications/sigir09_monz.pdf)


## FAQ

  - **Only three attempts?? Why?**
  You are not supposed to look at performance on the test data during development at all. That is why you get only a limited number of attempts. You have to use them wisely.
  - **What happens if I/we don't reach 0.7 F-score online?**
  Nothing. It is your submission to GitHub what ulimately counts. You can make changes and generate new results even after you used up your 3 online attempts. 
  - **Is it obligatory to evaluate results online?**
  No. This is just for your information to see how you perform (if you passed the F-score threshold) and that you can compare your performance to that of others. The final results will be based on the files pushed to GitHub (the scoring will be exactly the same).
  - **Do we need to write a report as well?**
  No, there is no written report needed for this assignment.  
  - **How can we achieve good performance on this task?**
  Document preprocessing is key. The other main challenge is to figure out how many clusters to have.
  - **Any more hints?**
  You can, for example, introduce a threshold on clustering similarity. It's probably easiest to do with hierarchical agglomerative clustering: merge clusters if and only if their similarity is above a given threshold. You can use the training data to determine the value for that threshold.
  - **What can be used for this task?**
  Everything, including text-processing libraries, clustering methods in scikit-learn, etc. There are no restrictions, apart from the usual one: it has to be your code that you can explain if asked.
  - **Is it possible to get a deadline extension?**
  No. Don't even ask.
  - **Can I take the exam if I fail to complete this assignment?**
  No. So you better take it seriously.

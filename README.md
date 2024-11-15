# resume-evaluator

## Description
This project takes a resume or collection of resumes and ranks each document according to desired criteria and/or ideal resumes.

## Requirements
Latest version of `python`

## Dependencies
Install all dependencies with `pip install .`

## Usage
1) Move all resumes or resume collections into `/resumes`
2) Move ideal resume(s) into `/resumeTargets` or enter a manual query string in `config.json`
3) Index all resume documents  
`python runIndexer.py`
4) Evaluate and assign scores to all documents  
`python runEval.py`

## Output
Once documents are evaluated and scored, the top documents are saved in `/output`. The lowest scoring document is also saved for sanity check.

## Config
`config.json`  
```json
{
    "count": 20, # Top number of documents to save in output
    "useResumeTargets": true, # Boolean to use resumeTargets
    "useSynonyms": true, # Boolean to get synonyms for each word in query
    "criteria": "I like to validate. In my free time I build gaming desktops." # String to store query criteria
}
```

## Methods
The indexer takes the following steps:
1) Divide a resume collection into individual resumes using a predefined delimiter. For single resume files, take the entire file as is.
2) Remove all punctuations, special characters and any unicode characters from the documents.
3) Stem every word in the documents.
4) Create data files:
    * `dictionary.json`
    * `postingList.json`
    * `resumeCollection.json`

The Evaluator takes the following steps:
1) Retrieve query criteria and use resume targets or synonyms if enabled.
2) Remove all punctuations, special characters and any unicode characters from the query.
3) Stem every word in the query.
4) Perform Cosine Similarity on the data collection of documents and get a score for each relevant document.
5) Save the top-scoring documents to `/output`.

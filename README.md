<h1>Plagiarism Detection</h1>
<h2>Kien Ta (488494), Anh Le (488493)</h2>
<h1><a href="https://docs.google.com/document/d/1p5UACqMd2nTA0Zw2z1BCI-j3GaJ-Gfu74-aEhVmHXFk/edit">Write-up</a></h1>

<h1>File Sructure</h1>
<h2>Code</h2>
<ol>
    <li><strong>constant.py</strong>: contains constant of the project</li>
    <li><strong>data_acquisition.py</strong>: get the content of the news in <a href="https://www.kaggle.com/datasets/rmisra/news-category-dataset">kaggle</a>. Note that we do not have code to spit the news, we just move them by hand to 2 folders PATH_TO_SAMPLE_DATABASE that contains the text database, and PATH_TO_SAMPLE_ORIGINAL_PATTERN that consider the original pattern that we haven't modify to form the test cases yet </li>
    <li><strong>test_case_generator.py</strong>: generate test cases from the content of the news. Grab some files from PATH_TO_SAMPLE_DATABASE, insert into files from PATH_TO_SAMPLE_ORIGINAL_PATTERN and put it back to PATH_TO_SAMPLE_MODIFIED_PATTERN. We also generate an additional json file data.json that records which database file is chosen to put in which pattern</a> </li>
    <li><strong>database_and_pattern_generator.py</strong>: generate database by concatenating the news <strong>....TODO</strong></a> </li>
    <li><strong>word_preprocessing.py</strong>: process the news: remove punctuation, convert to lower case, expand shortened words, tokenize, remove stop words, and finally lemmatization </li>
    <li><strong>jaccard_similarity_shingling.py</strong>: use Jaccard similarity & shingles to rank the top k1 similar database text from the database </li>
    <li><strong>local_alignment_calculator.py</strong>: calculate local alignment given 2 texts </li>
    <li><strong>main.py</strong>: iterate through all pattern files, find top k1 best matches from the database with Jaccard similarity, then find k2 &#x3c; k1 top best matches with local alignment. This top k2 alignment in additional to the score is saved in <i>output.json</i> of PATH_TO_SAMPLE_MODIFIED_PATTERN folder<i></i> </li>
</ol>
<h2>Order to run them</h2>
<ol>
    <li><strong>data_acquisition.py</strong>
    <li><strong>database_and_pattern_generator.py</strong>
    <li><strong>test_case_generator.py</strong></li>
    <li><strong>main.py</strong></li>
</ol>
<h3>Citation</h3>
<ul>
    <li>https://www.kaggle.com/datasets/rmisra/news-category-dataset</li>
</ul>

<h5>export LC_CTYPE="en_US.UTF-8"</h5>

# Movie_recommendation

## Description  

Movie recommendation application based on NLP.


The NLP model was developped by Maïté Rolin.   
<a href="https://www.linkedin.com/in/mrolin/" target="_blank"><img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="15" height="15" alt="LinkedIn">Maïté Rolin</a> &nbsp; | &nbsp; <a href="https://github.com/Maite5238//movie-recommender" target="_blank"><img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="15" height="15" alt="GitHub">Maite5238</a> 


<a href="https://mymovies-ddyq.onrender.com/">Link to render application</a>
<br/>
<p align="center">
    <img src="/readme/screenshot.png"
         alt="Application screenshot">
</p>

<p align="center">
  <a href="#Application">Application</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#NLP Model">NLP Model</a> •
  <a href="#Dependencies">Dependencies</a>
</p>

## Application

The client application was developped in Javascript based on Vue.Js framework and vite development environment.  
A Flask Api for the model was also deployed with Docker on render.


## How To Use
The application is deployed on render.com,  
at <a href="https://mymovies-ddyq.onrender.com/">https://mymovies-ddyq.onrender.com/</a>  

Two ways to get a movie recommendation:  
You can switch<img src="/public/cursor/icons8-clap-48.png" alt="movie icon"> the interface between  

### favorite movie list

Enter film title in the search form and add <img src="/public/cursor/icons8-blue-heart-48.png" alt="movie icon">your favorite films the list. 
You can remove item from the list by hovering on it and click when <img src="/public/cursor/icons8-cross-mark-48.png" alt="red cross icon"> appears.
To get more informations about any film in the list, hover and click on it when the <img src="/public/cursor/icons8-movie-48.png" alt="movie icon">icon appears. 
You can only get a recommendation when the list contains 5 films.
The overview of each film in the list are sent to the model API to compute a list of 5 movies recommendation.  

### film description or keywords

Enter some film description or only 5 keywords to get a film recommendation.  

  > **Note**
  > Check the status of the API on Render.com by visiting the API's homepage or status page.  
If the API is currently offline or unavailable, wait for it to wake up.
This may take a few minutes or more, depending on the reason for the outage.
Once the API is awake and running, you can start making requests to it as usual.
The API response could take up to 2 minutes due to restricted cpu usage on the server.

## NLP Model

The movie recommender system is implemented in Python, and utilizes natural language processing (NLP) techniques to recommend movies based on their plot summaries. It uses Scikit-learn's TfidfVectorizer, a text vectorization tool, to transform the plot summaries into a matrix of term frequency-inverse document frequency (TF-IDF) features. This technique assigns a weight to each word based on its frequency in the document and the inverse frequency of the word across all documents in the dataset. The resulting matrix represents each movie as a set of weighted features that capture its most important words. The system then computes the cosine similarity between the user input and the plot summaries of all the movies in the dataset, and returns the top 3 movies that are most similar to the user input based on this similarity measure.  
<a href="https://www.linkedin.com/in/mrolin/" target="_blank"><img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="15" height="15" alt="LinkedIn">Maïté Rolin</a> &nbsp; | &nbsp; <a href="https://github.com/Maite5238//movie-recommender" target="_blank"><img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="15" height="15" alt="GitHub">Maite5238</a> 

### Time line

7 working days to discover NLP, Bert, build the app and deployment.
### Possible Improvements

- Improve 
- Improve

### Dependencies  

- Python 3.11  
- Flask 
- NumPy  
- Pandas  


---

> GitHub  [Meulemans Philippe](https://github.com/Laverdure77) &nbsp;&middot;&nbsp;
> LinkedIn  [Meulemans Philippe](https://www.linkedin.com/in/meulemans-philippe/) &nbsp;&middot;&nbsp;

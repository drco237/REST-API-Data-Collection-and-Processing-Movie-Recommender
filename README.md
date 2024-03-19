# REST API Movie Recommender

03.19.2024 REST API Data Collection and Processing with Python

In this project, I developed Python 3 code that interacts with two REST APIs, TasteDive and OMBD, to generate movie recommendations for the user. 

The Movie Recommender defines a number of functions: Three of these interact with the TasteDive API to obtain a list of 5 related movies per movie input by the user; two function interact with OMBD to obtain data about each of the related movies; the last function combines the former 5 to produce a ranked list of recommendations for the user given a list of movies they enjoyed. 

Because one of the REST APIs, TasteDive, is no longer functional, I relied on a function defined by the University of Michigan named <results_with_caching>, which stored data for a pre-selected list of movies to a permanent cache hosted on their Coursera webiste. All other code besides the <results_with_caching> function is my own. 

The project involved interacting with REST APIs and reading API documentation for key parameters as well as defining several functions that synergize to produce the final, sorted product. 

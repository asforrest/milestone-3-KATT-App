## Methodolgy

As a user of his own web app, BudgetCalc, Alexander found it easy to put himself in the shoes of potential user and this has been a benefit to him to develop useful features. 

Alexander has a background in video production which gives him a unique perspective when trying to look at a problem from multiple viewpoints as video production is often for an audience with a wide range of tastes.

The methodology of this project will be based on three core principals during development;

- #### That [Form follows function](https://en.wikipedia.org/wiki/Form_follows_function#Software_engineering).
    1. The form should first and foremost look at the engineering requirements.
    3. If the design dictates how the software should work on the back-end it may suffer from inflexibly.

- #### The principle of always delivering a [Potentially Shippable Product](https://less.works/less/framework/potentially-shippable-product-increment)
    1. This means that the product is always working after a coding session, albeit in a basic form.
    1. The product could potentially be submitted at any time.
    1. Constantly having a working product gives more room for refinement.

- #### Working with a [Product Backlog](https://en.wikipedia.org/wiki/Scrum_(software_development)#Product_backlog)
    1. As software development is an ongoing process a product backlog allows for the prioritising of information.
    1. A product backlog provides a roadmap for future development.
    1. Items completed on the product backlog will nbe moved to a completed section so that progression can be evaluated and tracked.




1. [Plotly](https://plotly.com/javascript/)
    - Plotly was used to generate graphs for the user.
1. [EmaiJS](https://www.emailjs.com/)
    - EmailJS was used for the contact form and to send a generated report to users.







### Cod

### GitHubs Role In Testing
When looking at the GitHub commits there is a pattern of the commits getting better and more consistent as the project went on. 

After checking the commits for the purpose of this readme an issue was discovered that some of the commits might have run a bit long. However, this was done purposefully so that it was easy to reference changes in the Web App in case something went wrong. 

Luckily, due to rigorous ongoing testing and committing there was only one time when data needed to be restored after accidentally deleting the js folder which contains all of the JavaScript code. It was easy to recover this code by accessing the last commit on GitHub and copying the data into the current GitPod workspace.

A system of prefixes was used to organise GitHub commits which can be used to get a glimpse of the amount of testing:

1. FEATURE
    - FEATURE was used when adding new functionality or after major changes to the web app. During implementation of these features testing was ongoing. 
2. BUG
    - BUG was used when there was an issue discovered during testing and only once the bug has been fixed.
3. TEST
    - TEST was used after a more in-depth test, sometimes bugs were also fixed before these commits.
4. UPDATE
    - UPDATE was used for small changes, primarily to supplemental material like the backlog and readme.
5. BACKUP
    - BACKUP was used for large backups before starting implementation of a new feature.
6. Various others
    - Other prefixes or text have also been used at times, however the goal for the future is to stick to the prefixes mentioned here above (1-5) as to give evaluators, colleagues, employers and users a clear overview of changes that have been made.


## Deployment

This project is saved to a [repository on GitHub](https://github.com/asforrest/milestone-2-budgetcalc) and as such is open to the public.

This project has also been [published to Heroku]((https://katt-app.herokuapp.com/) both for evaluation by Code Institute and so that users can access and use the Web App.

This is made possible by GitHub by going to the settings page of the repository and choosing a branch to publish. The master branch has been selected for this purpose.

The development version is currently the same as the deployed version, however this project is a work in progress and will be branched for continuous development while waiting for a final grade during Code Institute’s evaluation process. After the evaluation period has been completed any changes made to the project will then be committed back to the master branch and will be directly available to users.

### Running The Code Locally

If you wish to download a copy of the code in order to run the code locally, this is also possible. To do this go to the [BudgetCalc repository on GitHub](https://github.com/asforrest/milestone-2-budgetcalc) click on 'Code' in the top right and select the method you want to use to download and run the code locally.

### Running The Code Online In Your Own Environment

If you wish to look at or work on the code in an online IDE, then it's recommended to use GitPot. If your using Google Chrome and you install the [Google Chrome GitPod extension](https://chrome.google.com/webstore/detail/gitpod-dev-environments-i/dodmmooeoklaejobgleioelladacbeki?hl=en) then you will see green 'Gitpod' button above [the repository](https://github.com/Code-Institute-Solutions/readme-template) and this will load the code into your own Gitpod environment.



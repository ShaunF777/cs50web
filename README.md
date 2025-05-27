# CS50's Web Programming with Python and JavaScript

Welcome! Lets first talk about the reason for this repo: I've done the CS50x course, but did not use git as part af my daily work routine. This repo is an attempt to use git more as im getting acqainted with techniques, libraries & frameworks.
This course is an advanced follow-up to CS50x & guides you through the building blocks of modern web development – from foundational design with HTML/CSS and Git to building full-stack applications with Python, Django, SQL, JavaScript, React and beyond.

## Course Overview

Throughout this course, we will learn both front-end and back-end technologies essential for creating robust and scalable web applications. Real-world projects helps us practice concepts like responsive design, database modeling, API usage, testing, and security, culminating in a capstone project where we design and deploy your own web application.

---

## Course Contents

### Week 0: HTML & CSS
- **Topics Covered:**  
  - HTML, Document Object Model (DOM)  
  - Forms  
  - CSS and Selectors  
  - Responsive Design  
  - Bootstrap  
  - Sass

### Week 1: Git
- **Topics Covered:**  
  - Git and GitHub basics  
  - Commits, Merge Conflicts, and Branches  
  - Forks and Pull Requests  
  - GitHub Pages

### Week 2: Python
- **Topics Covered:**  
  - Python fundamentals: Variables, Sequences, and Functions  
  - Modules  
  - Object-Oriented and Functional Programming  
  - Exception Handling

### Week 3: Django - 03_DjangoTemplatesFormsSessions
- **Topics Covered:**  
  - Web Applications and HTTP  
  - Django Framework: Routes, Templates, Forms and Sessions  
- **Project:**  
  - **Wiki:** Design a Wikipedia-like online encyclopedia

### Week 4: SQL, Models and Migrations - 04_SqlDjangoModelsMigrations
- **Topics Covered:**  
  - Databases and SQL  
  - Creating Tables and Defining Models  
  - Managing Relationships and Migrations  
  - Django Admin Interface  
- **Project:**  
  - **Commerce:** Build an eBay-like auction site where users can post listings, place bids, comment, and maintain a “watchlist.”

### Week 5: JavaScript - 05_JsEventDomStorageApis
- **Topics Covered:**  
  - Core JavaScript syntax and concepts  
  - Handling Events and DOM Manipulation  
  - Working with Local Storage  
  - APIs and Data Fetching

### Week 6: User Interfaces - 06_UiDesignSPAsAnimatReact
- **Topics Covered:**  
  - Designing Intuitive User Interfaces  
  - Single-Page Applications (SPAs)  
  - Infinite Scroll and Animation  
  - Introduction to React  
- **Project:**  
  - **Mail:** Design a front-end for an email client that interacts with APIs to send and receive emails

### Week 7: Testing, CI/CD - 07_Test_CiCd_SeleniumGithubActionsDocker
- **Topics Covered:**  
  - Test-Driven Development and Unit Testing  
  - Django Testing and Selenium  
  - Continuous Integration/Continuous Deployment (CI/CD) practices  
  - GitHub Actions and Docker  
- **Project:**  
  - **Network:** Create a Threads-like social network for making posts and following users

### Week 8: Scalability and Security - 08_Scalability_Security
- **Topics Covered:**  
  - Load Balancing and Autoscaling  
  - Database Replication and Caching  
  - HTTPS, Public-Key Cryptography  
  - Mitigating Cross-Site Scripting (XSS) and Cross-Site Request Forgery (CSRF)  
- **Capstone Project:**  
  - Design and implement your own web application that integrates all of the concepts learned during the course

---

## Projects at a Glance
My projects are not for public disclosure obviously, but so you can see what's required of any person doing this course.
- **Wiki (Week 3):** A Wikipedia-like platform to showcase content organization and dynamic page generation.  
- **Commerce (Week 4):** An auction site that lets users post listings, bid, comment, and curate a watchlist.  
- **Mail (Week 6):** A front-end client for an email system using API calls to send/receive emails.  
- **Network (Week 7):** A social network enabling post creation and user following, similar to Threads.  
- **Capstone (Week 8):** Your own web application that brings together front-end and back-end skills, along with advanced scaling and security techniques.

---

## Environment Setup & Running the Projects

Each week’s practice and project is contained within its own subdirectory. To keep our repository organized and focused, detailed instructions for setting up each project’s environment can be found in the respective subdirectory’s README.md file. These subdirectory READMEs include information on the specific commands, dependencies, and configurations required for that particular project.

In general, for projects that involve Python (including Django), you will follow steps similar to the ones below:

1. **Create and Activate a Virtual Environment:**

It’s a good practice to use a virtual environment while working on Python projects. For example: `python -m venv venv`
To activate the virtual environment:

- On macOS/Linux: `source venv/bin/activate`
- On Windows: `venv\Scripts\activate`
2. **Install Python Dependencies:**

    Each project will have a requirements.txt file listing the required packages, such as Django and any supporting libraries. 
    You can install these packages by running: `pip install -r requirements.txt`
    This command reads the file and installs the exact package versions needed. For example, a typical requirements.txt might include:
    ```txt
    Django==4.2.5
    djangorestframework==3.14.0
    python-dotenv==0.21.0
    ```
3. **Run the Development Server:***

    For Django projects, after installing the dependencies, you can start the built-in development server with: `python manage.py runserver` 
    This command launches your local web server so you can test and interact with the web application.

For JavaScript or front-end projects, dependencies are usually managed through a `package.json` file. In those cases, after cloning the repository you would run: `npm install` 
This will install all required Node.js packages.

Please refer to each subdirectory's README.md for further environment-specific setup instructions and project details. This approach ensures that the root README provides a high-level overview while the individual projects contain the precise commands and configurations you need to get started.

---

## Getting Started
Each Weeks practice is contained within its respective directory. Follow the instructions in each week's directory for further environment setup and development.
To get started with this repository and follow along with the projects:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/yourrepository.git


Additional Resources
Course Website: [CS50's Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/2020/)

YouTube Playlist: [CS50's Web Programming with Python and JavaScript (CS50W)] (https://www.youtube.com/playlist?list=PLhQjrBD2T380xvFSUmToMMzERZ3qB5Ueu)

Community Forums: Leverage CS50's discussion forums and community channels for tips, questions, and collaboration.
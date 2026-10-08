"""Knowledge base: skills, aliases, job roles, learning hints and question banks."""

# canonical skill -> list of aliases (all lowercase)
SKILLS = {
    "Programming Languages": {
        "python": ["python", "python3"],
        "java": ["java"],
        "c++": ["c++", "cpp"],
        "c": ["c programming", "c language"],
        "c#": ["c#", "csharp"],
        "javascript": ["javascript", "js", "es6"],
        "typescript": ["typescript"],
        "r": ["r programming", "rstudio"],
        "kotlin": ["kotlin"],
        "php": ["php"],
    },
    "Web Development": {
        "html": ["html", "html5"],
        "css": ["css", "css3"],
        "bootstrap": ["bootstrap"],
        "react": ["react", "react.js", "reactjs"],
        "angular": ["angular", "angularjs"],
        "node.js": ["node.js", "nodejs", "node js"],
        "express": ["express", "express.js", "expressjs"],
        "django": ["django"],
        "flask": ["flask"],
        "spring boot": ["spring boot", "springboot", "spring"],
        "rest api": ["rest api", "rest apis", "restful", "api development"],
    },
    "Data & AI": {
        "pandas": ["pandas"],
        "numpy": ["numpy"],
        "matplotlib": ["matplotlib"],
        "seaborn": ["seaborn"],
        "scikit-learn": ["scikit-learn", "sklearn", "scikit learn"],
        "tensorflow": ["tensorflow"],
        "pytorch": ["pytorch"],
        "keras": ["keras"],
        "opencv": ["opencv"],
        "machine learning": ["machine learning", "ml"],
        "deep learning": ["deep learning", "neural network", "neural networks", "cnn"],
        "nlp": ["nlp", "natural language processing"],
        "statistics": ["statistics", "statistical analysis", "hypothesis testing"],
        "data visualization": ["data visualization", "data visualisation"],
        "data cleaning": ["data cleaning", "data preprocessing", "data wrangling"],
        "eda": ["eda", "exploratory data analysis"],
        "feature engineering": ["feature engineering"],
        "power bi": ["power bi", "powerbi"],
        "tableau": ["tableau"],
        "excel": ["excel", "ms excel", "advanced excel"],
    },
    "Databases": {
        "sql": ["sql"],
        "mysql": ["mysql"],
        "postgresql": ["postgresql", "postgres"],
        "mongodb": ["mongodb", "mongo db"],
        "sqlite": ["sqlite"],
        "oracle": ["oracle"],
    },
    "CS Fundamentals": {
        "data structures": ["data structures", "data structure", "dsa"],
        "algorithms": ["algorithms", "algorithm", "dsa"],
        "oop": ["oop", "oops", "object oriented", "object-oriented"],
        "dbms": ["dbms", "database management"],
        "operating systems": ["operating system", "operating systems"],
        "computer networks": ["computer network", "computer networks", "networking"],
        "system design": ["system design"],
    },
    "Tools & Cloud": {
        "git": ["git"],
        "github": ["github"],
        "docker": ["docker"],
        "linux": ["linux", "ubuntu"],
        "aws": ["aws", "amazon web services"],
        "azure": ["azure"],
        "postman": ["postman"],
        "junit": ["junit"],
        "jira": ["jira"],
    },
    "Soft Skills": {
        "communication": ["communication", "public speaking", "presentation skills"],
        "teamwork": ["teamwork", "team player", "collaboration"],
        "leadership": ["leadership", "led a team", "team lead"],
        "problem solving": ["problem solving", "problem-solving", "analytical thinking"],
        "time management": ["time management"],
    },
}

ROLES = {
    "Data Analyst": {
        "skills": ["python", "sql", "excel", "pandas", "numpy", "power bi", "tableau",
                   "statistics", "data visualization", "data cleaning", "eda", "matplotlib"],
        "description": "Data analyst role analysing business data using python sql excel pandas numpy "
                       "statistics dashboards power bi tableau data visualization data cleaning "
                       "exploratory data analysis reporting insights",
    },
    "Data Scientist / ML Engineer": {
        "skills": ["python", "machine learning", "scikit-learn", "pandas", "numpy", "statistics",
                   "deep learning", "tensorflow", "sql", "nlp", "feature engineering", "data visualization"],
        "description": "Data scientist building machine learning models with python scikit-learn pandas "
                       "numpy tensorflow deep learning nlp statistics feature engineering model evaluation",
    },
    "Python Developer": {
        "skills": ["python", "django", "flask", "sql", "git", "rest api", "oop",
                   "data structures", "docker", "linux"],
        "description": "Python developer building backend services using django flask rest api sql git "
                       "object oriented programming data structures docker linux testing",
    },
    "Java Developer": {
        "skills": ["java", "spring boot", "sql", "mysql", "oop", "data structures",
                   "algorithms", "git", "rest api", "junit"],
        "description": "Java developer building enterprise applications with spring boot rest api mysql sql "
                       "object oriented programming data structures algorithms junit git",
    },
    "Full Stack Web Developer": {
        "skills": ["html", "css", "javascript", "react", "node.js", "express", "mongodb",
                   "sql", "git", "rest api", "bootstrap"],
        "description": "Full stack developer building web applications with html css javascript react node.js "
                       "express mongodb sql rest api git responsive design",
    },
    "General Campus Placement (Fresher)": {
        "skills": ["python", "java", "c++", "data structures", "algorithms", "oop", "dbms", "sql",
                   "operating systems", "computer networks", "git", "problem solving", "communication"],
        "description": "Fresher software engineer with strong programming data structures algorithms oop dbms "
                       "sql operating systems computer networks git problem solving communication teamwork",
    },
}

# short learning hints for common missing skills
LEARNING_HINTS = {
    "python": "Finish a beginner-to-intermediate Python course (freeCodeCamp / Kaggle Learn) and solve 30 easy problems.",
    "sql": "Practice joins, group by, subqueries and window functions on LeetCode/HackerRank SQL sets.",
    "excel": "Learn pivot tables, VLOOKUP/XLOOKUP, charts and a small dashboard project.",
    "pandas": "Do Kaggle's Pandas micro-course and clean one real CSV dataset end to end.",
    "numpy": "Practise arrays, broadcasting and vectorised operations in a short notebook.",
    "power bi": "Build one sales dashboard from a public dataset and add it to your portfolio.",
    "tableau": "Use Tableau Public to publish one interactive dashboard.",
    "statistics": "Revise mean/median/variance, distributions, hypothesis tests and correlation.",
    "machine learning": "Do Andrew Ng's ML course basics and build a classification + regression mini project.",
    "scikit-learn": "Train, evaluate and tune 3 models (LogReg, RandomForest, SVM) on a Kaggle dataset.",
    "deep learning": "Build an image or text classifier with Keras/TensorFlow.",
    "tensorflow": "Follow the official TensorFlow beginner tutorials (MNIST, text classification).",
    "nlp": "Build a sentiment analyser using TF-IDF and then a simple transformer-based one.",
    "data structures": "Master arrays, strings, linked lists, stacks/queues, trees, graphs, hashing; solve on LeetCode.",
    "algorithms": "Practise sorting, searching, recursion, DP and greedy; aim for 100 solved problems.",
    "oop": "Revise 4 pillars of OOP with examples; be ready to explain with real-life analogies.",
    "dbms": "Revise normalization, ACID, indexing, transactions and ER diagrams.",
    "operating systems": "Revise process vs thread, scheduling, deadlock, paging, memory management.",
    "computer networks": "Revise OSI/TCP-IP layers, HTTP/HTTPS, DNS, TCP vs UDP.",
    "git": "Learn clone, branch, commit, merge, pull request; push all your projects to GitHub.",
    "github": "Create a clean GitHub profile with READMEs for each project.",
    "docker": "Containerise one of your apps with a Dockerfile.",
    "react": "Build a small CRUD app with hooks and a REST API.",
    "node.js": "Build a REST API with Express and connect it to MongoDB.",
    "rest api": "Build and document a small API using Flask/Express/Spring Boot and test with Postman.",
    "java": "Revise core Java, collections, exceptions, multithreading and Java 8 streams.",
    "spring boot": "Build a CRUD REST service with Spring Boot + MySQL.",
    "django": "Follow the official Django tutorial and build a blog/ToDo app.",
    "flask": "Build a small Flask API with SQLite and deploy it.",
    "communication": "Practise a 60-second self-introduction and STAR-method answers aloud.",
    "problem solving": "Solve 1-2 coding problems daily and explain your approach in words.",
}

# --- Interview questions ---------------------------------------------------
ROLE_QUESTIONS = {
    "Data Analyst": [
        "Explain the difference between INNER JOIN, LEFT JOIN and FULL JOIN.",
        "How do you handle missing values and outliers in a dataset?",
        "What is the difference between a pivot table and a group-by?",
        "Walk me through an end-to-end analysis you did. What insight did you find?",
        "What chart would you use to show trend vs comparison vs distribution?",
        "Explain correlation vs causation with an example.",
    ],
    "Data Scientist / ML Engineer": [
        "Explain bias-variance trade-off.",
        "What is overfitting and how do you prevent it?",
        "Explain precision, recall and F1-score. When is accuracy misleading?",
        "How does a Random Forest work?",
        "What is cross-validation and why is it used?",
        "How would you deploy a trained model?",
    ],
    "Python Developer": [
        "Difference between list, tuple, set and dictionary?",
        "What are decorators and generators in Python?",
        "Explain the GIL.",
        "What is the difference between deep copy and shallow copy?",
        "How do you handle exceptions in Python?",
        "Explain REST and how you would design an endpoint in Flask/Django.",
    ],
    "Java Developer": [
        "Difference between abstract class and interface?",
        "Explain how HashMap works internally.",
        "What are checked and unchecked exceptions?",
        "Explain JVM, JRE and JDK.",
        "What is dependency injection in Spring?",
        "What is the difference between == and equals()?",
    ],
    "Full Stack Web Developer": [
        "Explain the virtual DOM in React.",
        "Difference between var, let and const.",
        "What is CORS and how do you fix a CORS error?",
        "Explain the event loop in JavaScript.",
        "SQL vs NoSQL: when would you choose MongoDB?",
        "How do you secure a REST API (auth, JWT, validation)?",
    ],
    "General Campus Placement (Fresher)": [
        "Tell me about yourself.",
        "Explain OOP concepts with real-life examples.",
        "What is the difference between a process and a thread?",
        "What is normalization in DBMS?",
        "Explain time complexity of binary search and why.",
        "Explain your best project and your exact contribution.",
    ],
}

SKILL_QUESTIONS = {
    "python": "Python: What is the difference between a list and a tuple? When would you use each?",
    "sql": "SQL: Write a query to find the second highest salary from an Employee table.",
    "java": "Java: Explain method overloading vs overriding.",
    "c++": "C++: What is the difference between a pointer and a reference?",
    "pandas": "Pandas: How do you merge two DataFrames and handle duplicates?",
    "numpy": "NumPy: Why is a NumPy array faster than a Python list?",
    "machine learning": "ML: Explain supervised vs unsupervised learning with examples.",
    "react": "React: What are hooks? Explain useState and useEffect.",
    "javascript": "JavaScript: What is a closure?",
    "html": "HTML/CSS: What is the CSS box model?",
    "django": "Django: Explain the MVT architecture.",
    "flask": "Flask: How do you create routes and return JSON?",
    "git": "Git: Difference between merge and rebase?",
    "dbms": "DBMS: Explain ACID properties.",
    "data structures": "DSA: Difference between array and linked list? Where is a stack used?",
    "operating systems": "OS: What is deadlock and what are the four conditions for it?",
    "excel": "Excel: Difference between VLOOKUP and INDEX-MATCH?",
    "tensorflow": "TensorFlow: What is the difference between a Dense and a Conv2D layer?",
    "statistics": "Statistics: What is a p-value?",
}

HR_QUESTIONS = [
    "Tell me about yourself (keep it to 60-90 seconds).",
    "What are your strengths and weaknesses?",
    "Why should we hire you?",
    "Where do you see yourself in 5 years?",
    "Describe a challenge you faced in a project and how you solved it.",
    "Are you comfortable with relocation / shift work?",
    "Tell me about a time you worked in a team and handled a conflict.",
]

APTITUDE_QUIZ = [
    {"q": "A train 150 m long passes a pole in 15 seconds. What is its speed?",
     "options": ["10 m/s", "15 m/s", "20 m/s", "25 m/s"], "answer": "10 m/s",
     "why": "Speed = distance / time = 150 / 15 = 10 m/s."},
    {"q": "If 20% of a number is 60, what is 45% of that number?",
     "options": ["105", "120", "135", "150"], "answer": "135",
     "why": "Number = 60 / 0.2 = 300; 45% of 300 = 135."},
    {"q": "Find the next number: 2, 6, 12, 20, 30, ?",
     "options": ["38", "40", "42", "44"], "answer": "42",
     "why": "Differences increase by 2 (4, 6, 8, 10, 12) so next = 30 + 12 = 42."},
    {"q": "A can finish a job in 12 days, B in 24 days. Together they finish in:",
     "options": ["6 days", "8 days", "9 days", "10 days"], "answer": "8 days",
     "why": "Rate = 1/12 + 1/24 = 3/24 = 1/8, so 8 days."},
    {"q": "Time complexity of binary search on a sorted array of n elements?",
     "options": ["O(n)", "O(log n)", "O(n log n)", "O(1)"], "answer": "O(log n)",
     "why": "Each step halves the search space."},
    {"q": "Which data structure uses FIFO order?",
     "options": ["Stack", "Queue", "Tree", "Graph"], "answer": "Queue",
     "why": "A queue serves the element that was inserted first."},
]

PREP_TOPICS = [
    "Aptitude - Quantitative", "Aptitude - Logical Reasoning", "Verbal Ability",
    "Data Structures", "Algorithms", "OOP", "DBMS & SQL", "Operating Systems",
    "Computer Networks", "Core Language (Python/Java/C++)", "Projects Explanation",
    "Resume Finalised", "HR Interview Practice", "Mock Interview", "LinkedIn & GitHub Updated",
]

ACTION_VERBS = [
    "developed", "built", "designed", "implemented", "created", "analyzed", "analysed", "led",
    "managed", "optimized", "optimised", "automated", "improved", "achieved", "deployed",
    "collaborated", "organized", "organised", "trained", "reduced", "increased", "engineered",
    "integrated", "tested", "deployed", "presented", "researched", "launched", "coordinated",
    "established", "streamlined", "delivered", "visualized", "predicted", "evaluated",
]

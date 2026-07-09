# Course Recommendation Agent

## About the Project

Finding the right course can be confusing when there are so many options available. I built this Course Recommendation Agent to help users discover courses that match their existing skills and career goals.

The application takes the user's input, analyzes it using AI, and suggests relevant courses that can help them move towards their desired career path.

## Features

- Recommends courses based on skills and career goals
- AI-powered recommendation system
- Simple and easy-to-use interface
- Quick course suggestions
- Responsive web design

## Technologies Used

- Python
- Flask
- HTML
- CSS
- OpenAI API
- JSON
- Render (Deployment)

## Project Structure

```
Course-Recommendation-Agent/
│── app.py
│── agent.py
│── requirements.txt
│── data/
│   └── course.json
│── static/
│── templates/
└── README.md
```

## How to Run

1. Clone this repository.

```bash
git clone https://github.com/PrabhaKN19/course-recommendation-agent.git
```

2. Install the required packages.

```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your API key.

```
GENAI_API_KEY=YOUR_API_KEY
```

4. Start the application.

```bash
python app.py
```

5. Open the application in your browser.

```
http://127.0.0.1:5000
```

## Challenges I Faced

While developing this project, I learned how to work with Flask, integrate an AI API, manage environment variables securely, and deploy a Python application using Render. I also faced issues with dependencies and deployment, which helped me better understand the deployment process.

## Future Improvements

- Add user login
- Save recommendation history
- Improve recommendation accuracy
- Include filters based on course duration and difficulty
- Add direct links to course platforms

## Author

**Prabha K N**

GitHub: https://github.com/PrabhaKN19

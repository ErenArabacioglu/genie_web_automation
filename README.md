# Genie Web Automation

This project automates the Genie web chatbot for basic functional testing.  
It was developed using **Python**, **Selenium**, and **PyTest**.

The tests include:
- Page load check  
- Sending and receiving messages  
- New chat creation   

To run the tests:
```bash
pytest -q -m web --html=report.html --self-contained-html
The HTML report (`report.html`) shows detailed results after execution.

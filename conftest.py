import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):# Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()    
    #browser_name = request.config.getoption("browser_name")
    
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb',
                     help="Choose language, example, es")


@pytest.fixture(scope="class")
def language(request):
    language_name = request.config.getoption("language")
    print (language_name)
    language = 'None2'
    if language_name =="es":
        print("\nstart language Spanish for test..")
        language = "es"
    elif language_name =="fr":
        print("\nstart language French for test..")
        language ="fr"
    elif language_name =="ru":
        print("\nstart language Russian for test..")
        language ="ru"
    elif language_name =="en-gb":
        print("\nstart language British English for test..")
        language ="en-gb"
    else:
        raise pytest.UsageError("--language should be, example: es,fr,en-gb,ru")
    return(language)
 
@pytest.fixture(scope="class")
def sign_up():
    mail=''
    email=''
    for x in range(12):
        mail=mail+random.choice(list('12345678'))
        email=mail+'@gmail.com'
        print(email)
    password_text="test200920"
    sign_up()



import pytest
from Application.WikiApp import App
from Pages.WikiMainPage import WikiMainHelper

@pytest.fixture(scope="session")
def wikifixture():
    app = App()
    yield app
    app.destroy()

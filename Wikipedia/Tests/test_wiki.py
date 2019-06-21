import time
from confest import wikifixture


def test_wiki_main_page(wikifixture):
    client=wikifixture
    wikifixture.open_main_page()
    client.wiki.search("Футбол")
    assert client.wiki.expectation_words("table","Футбол")
    client.wiki.click_element("logo_wiki")
    assert client.wiki.expectation_words("upper_buttons","Обсуждение")
    client.superwiki.search_all_results("Авокадо")




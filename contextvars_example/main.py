from my_logging import context_set, product_context, url_context
import scrapper

if __name__ == "__main__":
    # Analiza pod kątem produktu A
    with context_set(product_context, "A"):
        with context_set(url_context, "www.wp.pl"):
            scrapper.analyze_page("www.wp.pl")
        with context_set(url_context, "www.onet.pl"):
            scrapper.analyze_page("www.onet.pl")

    # Analiza pod kątem produktu B
    with context_set(product_context, "B"):
        with context_set(url_context, "www.wp.pl"):
            scrapper.analyze_page("www.wp.pl")

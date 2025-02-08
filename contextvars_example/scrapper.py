import my_logging

def parse_html(content: str) -> int:
    my_logging.info("Parsing HTML")
    return 123

def analyze_page(url: str) -> str:
    my_logging.info("Starting page analysis")
    parse_html("... place html here ...")
    my_logging.info("Finished page analysis")
    return "OK"

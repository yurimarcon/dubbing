from urllib.parse import urlparse, parse_qs, urlencode


def validate_url(url_input):
    url = url_input

    parsed_url = urlparse(url)

    query_params = parse_qs(parsed_url.query)

    first_key = list(query_params.keys())[0]
    first_param = {first_key: query_params[first_key][0]}

    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
    new_url = f"{base_url}?{urlencode(first_param)}"

    return new_url

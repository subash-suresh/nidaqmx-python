def cleanup_docstring(docstring):
    # Removing leading/trailing whitespace.
    stripped = docstring.strip()

    # Some strings have extraneous spaces between words; clean those up.
    words = stripped.split()
    return " ".join(words)
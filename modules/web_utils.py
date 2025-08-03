import webbrowser

def open_website():
    site = input("Enter website name *website.com* : ").strip()

    if not site.startswith("http"):
        site = 'https://'+site
    

    try:
        webbrowser.open(site)
        print(f"Opening {site}")
    except Exception as e:
        print(f"Failed to open site {e}")

    
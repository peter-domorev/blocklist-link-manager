def link_cleaner(links):
    links = links.split("https://")
    
    new_links = []
    for link in links:
        if link != "":
            link = link.split("/")[0]
            new_links.append(f"https://{link}")
            
    return new_links
            

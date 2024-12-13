if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from menuitem import MenuItem
else:
    from code.menuitem import MenuItem


def clean_price(price:str) -> float:
    price = price.removeprefix('$')
    price = price.replace(',', '')
    return float(price)


def clean_scraped_text(scraped_text: str) -> list[str]:
    '''
This function should take the scraped text and clean it up, by removing any unwanted data.  First split the text on a newline `"\n"` so you have a list of strings, you will only add the desired lines to the cleaned list. "Unwanted" lines that should be omitted include:
  - empty lines of text
  - lines of text that are just "NEW!" or "NEW"
  - lines of text that are indications of Spicy, Vegan, Gluten-free, or peanut items "S", "V", "GS", "P"
 '''
    unwanted_set = {"NEW", "NEW!", "GS", "V", "P", "S"}
    scraped_text = scraped_text.split("\n")
    cleaned_text = []

    for line in scraped_text:
        line = line.strip()
        if line and line not in unwanted_set:  # Ignore empty or unwanted lines
            cleaned_text.append(line)
    return cleaned_text

    

def extract_menu_item(title:str, scraped_text: str) -> MenuItem:
    '''
    This function builds a `MenuItem` dataclass object from what was scraped.
  - The title is the scraped menu category, e.g. "Pastas"
  - The scraped_text is the text of the menu item. Again, refer to `TEST_DATA` 
  in the `test_menuitemextractor.py` file for examples of the text you will be working with.

In the function body, you should call `clean_scraped_text` to get the cleaned text 
for each item, then create a `MenuItem` object for each item. Do not forget to call 
`clean_price` to get the price as a float. Finally  check to see if there is a menu 
description (cleaned list of text has more than 2 items), when there is no description, 
use "No desciption available" as the description.'''
    cleaned_text = clean_scraped_text(scraped_text)
    return MenuItem(category=title, 
                    name=cleaned_text[0], 
                    price=clean_price(cleaned_text[1]), 
                    description=cleaned_text[2] if len(cleaned_text) > 2 else "No description available")
    


if __name__=='__main__':
    pass

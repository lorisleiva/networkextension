# Generate the documentation
This documentation explains how to use your [defined vocabulary](/docs/define-vocabulary.md) to auto-generate a documentation website using the `voc2doc.py` script.

## Make your vocabulary accessible

Wrap your vocabulary definition in a function to access it in the `voc2doc.py` file.

```python
from netcomp import getVocabulary
voc = getVocabulary()
```

Check the [netcomp.py](/scripts/netcomp.py) vocabulary definition.

## Set up the script

Edit the global variables with your directories.

```python
templateFolder = 'templates/'
websiteFolder = '../networkextension-website/'
```

For example here the `templateFolder` is in a sub-directory of the repository called 'template' and the `websiteFolder` is a sibling directory to the repository called 'networkextension-website' (which is actually a git clone of the `gh-pages` branch).

## Verify the main function

Currently the script creates:

* an index pages which contains the class hierarchy
* a page that lists all the properties
* one page per class created or extended
* one page per property created or extended

```python
if __name__ == '__main__':
    voc = getVocabulary()

    createClassHierarchyPage(voc)
    createAllPropertiesPage(voc)

    for c in voc.classes:
        createClassPage(voc.classes[c], voc)

    for p in voc.properties:
        createPropertyPage(voc.properties[p], voc)
```

## Edit the templates

Before you start executing the script, you might want to update the html templates that are used to generate the documentation. Here is a list of the different template files that are used:

* `master.tpl`: The base template that all other templates extend. Contains the doctype, the stylesheets, the scripts, etc. It also contains the content of the sidebar which **should be edited**.
* `index.tpl`: The index file that contains the class hierarchy. It also contains a short HTML description of the extension that **should be edited**.
* `property.tpl`: The page that lists all the properties created or extended.
* `class.tpl`: The page that defines the structure of each class page.
* `property.tpl`: The page that defines the structure of each property page.

## Execute the script

Finally, execute the script at the root of your repository:

```
python scripts/voc2doc.py
```




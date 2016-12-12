# Define your vocabulary
This documentation helps you understand how to use the Vocabulary class to design your own extension.

## Getting Started

Start by importing the `Vocabulary` class and instanciating one by giving the url of your documentation. Note that you can simply use github pages in a new repository to avoid hosting the documentation.

```python
from vocabulary import Vocabulary
voc = Vocabulary('https://lorisleiva.github.io/networkextension')
```

Then use the various methods listed below to define your vocabulary.

```python
voc.addClass('Fruit')
voc.comment('Any type of fruit. E.g. Banana, Strawberries, etc.')
voc.subClassOf('Thing')

voc.addProperty('hasSeeds')
voc.comment('Indicates whether a particular Fruit has some seeds.')
voc.domainIncludes('Fruit')
voc.rangeIncludes('Boolean')
```

You will notice two things:
1. The vocabulary keeps track of the last element added (class or property) so that when you do `voc.comment(...)`, it knows for which element to add the comment.
2. When mentionning an element that have not yet being defined (E.g. `Thing` or `Boolean` in our example), the vocabulary will assume that it is from the core vocabulary of Schema.org. If you define it later, the vocabulary will understand that it belongs to your extension and update the element.

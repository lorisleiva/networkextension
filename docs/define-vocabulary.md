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

## Methods available

### Methods available to create a new element:

| Method and arguments                       | Comment                                             |
| ------------------------------------------ | --------------------------------------------------- |
| `addClass(name)`                           | Defines your own class with a given unique name.    |
| `addProperty(name)`                        | Defines your own property with a given unique name. |
| `addSchemaClass(name, extends)`    | <strong>if extends is False (default):</strong> Adds a class from Schema.org for documentation purposes only. It will show the class on the tree hierachy but it will not have its own page. The class will also not appear on the RDFA file.<br><br><strong>If extends is True:</strong> Extends the class from Schema.org. The class definition will appear on the RDFA file and have its own documentation page with a link to the core documentation. |
| `addSchemaProperty(name, extends)` | <strong>if extends is False (default):</strong> Adds a property from Schema.org for documentation purposes only. It will show the property on each appropriate class page but the link will redirect to Schema.org. The property will also not appear on the RDFA file.<br><br><strong>If extends is True:</strong> Extends the property from Schema.org. The property definition will appear on the RDFA file and have its own documentation page with a link to the core documentation. |


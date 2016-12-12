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

| Method and arguments               | Comment                                             |
| ---------------------------------- | --------------------------------------------------- |
| `addClass(name)`                   | Defines your own class with a given unique name.    |
| `addProperty(name)`                | Defines your own property with a given unique name. |
| `addSchemaClass(name, extends)`    | <strong>if extends is False (default):</strong> Adds a class from Schema.org for documentation purposes only. It will show the class on the tree hierachy but it will not have its own page. The class will also not appear on the RDFA file.<br><br><strong>If extends is True:</strong> Extends the class from Schema.org. The class definition will appear on the RDFA file and have its own documentation page with a link to the core documentation. |
| `addSchemaProperty(name, extends)` | <strong>if extends is False (default):</strong> Adds a property from Schema.org for documentation purposes only. It will show the property on each appropriate class page but the link will redirect to Schema.org. The property will also not appear on the RDFA file.<br><br><strong>If extends is True:</strong> Extends the property from Schema.org. The property definition will appear on the RDFA file and have its own documentation page with a link to the core documentation. |

### Methods available to detail a class:

| Method and arguments          | Comment                                             |
| ----------------------------- | --------------------------------------------------- |
| `comment(description)`        | Gives a description to the class. This will render in the documentation as well as in the RDFA file as a `rdfs:comment` property |
| `subClassOf(parentClassName)` | Defines the parent class by giving its name. If the parent class has not been defined yet, it will be added for documentation purposes only.<br>(Equivalent to `addSchemaClass(parentClassName, False)`). If it is defined later on, the class will be updated accordingly.<br>This will render in the documentation as the class hierarchy and in the RDFA file as the `rdfs:subClassOf` property. |

### Methods available to detail a property:

| Method and arguments          | Comment                                             |
| ----------------------------- | --------------------------------------------------- |
| `comment(description)`        | Gives a description to the property. This will render in the documentation as well as in the RDFA file as a `rdfs:comment` property |
| `domainIncludes(domainName)`  | Adds the property to a class (domain). You can use this methods multiples times if a property is defined is multiple classes.<br>This will render in both the documentation and the RDFA file as the `http://schema.org/domainIncludes` property. |
| `rangeIncludes(rangeName)`    | Adds a type of value (range) that the property can be set as. You can use this methods multiples times if a property has multiple types of value.<br>This will render in both the documentation and the RDFA file as the `http://schema.org/rangeIncludes` property. |
| `inverseOf(inversePropertyName)` | Defines the inverse relationship of the property.<br>This will render in both the documentation and the RDFA file as the `http://schema.org/inverseOf` property. |

Just like in the `subClassOf()` method, if the class given to the methods `domainIncludes()`, `rangeIncludes()` and `inverseOf()` has not been yet defined, then it will be added for documentation purposes only.<br>(Equivalent to `addSchemaClass(parentClassName, False)`). And if it is defined later on, the class will be updated accordingly.

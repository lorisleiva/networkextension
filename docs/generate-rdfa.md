# Generate the RDFA file
This documentation explains how to use your [defined vocabulary](/docs/define-vocabulary.md) to auto-generate the RDFA file using the `voc2rdfa.py` script.

## Make your vocabulary accessible

Wrap your vocabulary definition in a function to access it in the `voc2rdfa.py` file.

```python
from netcomp import getVocabulary
voc = getVocabulary()
```

Check the [netcomp.py](/scripts/netcomp.py) vocabulary definition.

## Verify the main function

Edit the filename of the generated file.

```python
if __name__ == '__main__':
    parseVocabulary(getVocabulary(), 'netcomp.rdfa')
```

## Execute the script

Finally, execute the script at the root of your repository:

```
python scripts/voc2rdfa.py
```

This will output the generated RDFA file at the root of your repository.

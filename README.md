# NetComp Extension
An external Schema.org extension that described components from Computer Networks inspired by [Bro][Bro official website].

&gt;&gt; [Start browsing the extension][documentation] &lt;&lt;

This extension raised from the need to apply Semantic Web technics to network management applications. The properties of this extension are influenced a lot by the Bro network management system and its logs. The description of a lot of properties have been inspired by the Brownian's [broLogTypes.py][Brownian log file] file.

## Extension's data and documentation

The final data of this extension is available as a RDFA file (`netcomp.rdfa`) that does not include the core Schema.org vocabulary by only the new or extended classes and properties.

You can browse through the various classes and properties of the extension via the [documentation website][documentation].

## How to create my own schema.org extension?

To design this extension with maximum flexibility, some python scripts have been developped to auto-generate the RDFA file and the entire documentation from a `Vocabulary` python's class.

If you want to extends the Schema.org vocabulary with your own extension, feel free to use those scripts. You can learn more about them if the following documentation file: [Define your own vocabulary](/docs/define-vocabulary.md).

[documentation]: https://lorisleiva.github.io/networkextension
[Bro official website]: https://bro.org
[Brownian log file]: https://github.com/grigorescu/Brownian/blob/master/Brownian/view/utils/broLogTypes.py

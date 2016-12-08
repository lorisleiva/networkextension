%rebase templates/master

<div 
    id="mainContent" 
    vocab="http://schema.org/" 
    typeof="rdfs:Class" 
    resource="http://schema.org/{{ element.name }}"
>

    <h1 property="rdfs:label" class="page-title">{{ element.name }}</h1>

    <h4>
        <span class='breadcrumbs'>
            <link  property="rdfs:subClassOf" href="http://schema.org/Thing" />
            <a href="http://schema.org/Thing">Thing</a> 
            &gt; 
            <a href="{{ element.getUrl }}">{{ element.name }}</a>
        </span>
    </h4>

    <div property="rdfs:comment">{{ element.comment }}</div>

    <table class="definition-table">
        <thead>
            <tr>
                <th>Property</th>
                <th>Expected Type</th>
                <th>Description</th>               
            </tr>
        </thead>

        <tbody class="supertype">

            <tr class="supertype">
                <th class="supertype-name" colspan="3">
                    Properties from <a href="/{{ element.name }}.html">{{ element.name }}</a>
                </th>
            </tr>

            % for property in element.properties:
                <tr typeof="rdfs:Property" resource="{{ property.getSchemaUrl() }}">
                    <th class="prop-nam" scope="row">
                        <code property="rdfs:label">
                            <a href="{{ property.getUrl() }}">{{ property.name }}</a>
                        </code>
                    </th>
                    <td class="prop-ect">
                        % for index, type in enumerate(property.ranges):
                            % if index > 0:
                                &nbsp;or<br>
                            % end
                            <link property="rangeIncludes" href="{{ type.getSchemaUrl() }}" />
                            <a href="{{ type.getUrl() }}">{{ type.name }}</a>
                        % end

                        % for domain in property.domains:
                            <link property="domainIncludes" href="{{ domain.getSchemaUrl() }}">
                        % end
                    </td>
                    <td class="prop-desc" property="rdfs:comment">
                        {{ property.comment }}
                    </td>
                </tr>
            % end

            <tr class="supertype">
                <th class="supertype-name" colspan="3">
                    Properties from <a href="http://schema.org/Thing">Thing</a>
                </th>
            </tr>

            <tr typeof="rdfs:Property" resource="http://schema.org/additionalType">
                <th class="prop-nam" scope="row">
                    <code property="rdfs:label">
                        <a href="/additionalType">additionalType</a>
                    </code>
                </th>
                <td class="prop-ect">
                    <link property="rangeIncludes" href="http://schema.org/URL">
                    <a href="/URL">URL</a>&nbsp;<link property="domainIncludes" href="http://schema.org/Thing">
                </td>
                <td class="prop-desc" property="rdfs:comment">
                    An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. In RDFa syntax, it is better to use the native RDFa syntax - the 'typeof' attribute - for multiple types. Schema.org tools may have only weaker understanding of extra types, in particular those defined externally.
                </td>
            </tr>
        </tbody>
    </table>


</div>
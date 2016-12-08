%rebase templates/master

<div 
    id="mainContent" 
    vocab="http://schema.org/" 
    typeof="rdfs:Property" 
    resource="http://schema.org/{{ element.name }}"
>

    <h1 property="rdfs:label" class="page-title">{{ element.name }}</h1>

    <h4>
        <span class='breadcrumbs'>
            <a href="http://schema.org/Thing">Thing</a>
            &nbsp;&gt;&nbsp;
            <a href="http://meta.schema.org/Property">Property</a>
            &nbsp;&gt;&nbsp;
            <a href="{{ element.getUrl() }}">{{ element.name }}</a>
        </span>
    </h4>

    <div property="rdfs:comment">{{ element.comment }}</div>

    <table class="definition-table">
        <thead>
            <tr><th>Values expected to be one of these types</th></tr>
        </thead>
        <tbody>
            <tr>
                <td>
                    % for index, range in enumerate(element.ranges):
                        % if index > 0:
                            <br>
                        % end
                        <link property="rangeIncludes" href="{{ range.getSchemaUrl() }}">
                        <a href="{{ range.getUrl() }}" title="The '{{ element.name }}' property has values that include instances of the '{{ range.name }}' type.">
                            {{ range.name }}
                        </a>
                    % end
                </td>
            </tr>
        </tbody>
    </table>

    <table class="definition-table">
        <thead>
            <tr><th>Used on these types</th></tr>
        </thead>
        <tbody>
            <tr>
                <td>
                    % for index, domain in enumerate(element.domains):
                        % if index > 0:
                            <br>
                        % end
                        <link property="domainIncludes" href="{{ domain.getSchemaUrl() }}">
                        <a href="{{ domain.getUrl() }}" title="The '{{ element.name }}' property is used on the '{{ domain.name }}' type.">
                            {{ domain.name }}
                        </a>
                    % end
                </td>
            </tr>
        </tbody>
    </table>
</div>
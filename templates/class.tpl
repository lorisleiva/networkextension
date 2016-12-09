%rebase templates/master

<div 
    id="mainContent" 
    vocab="http://schema.org/" 
    typeof="rdfs:Class" 
    resource="http://schema.org/{{ element.name }}"
>

    <h1 property="rdfs:label" class="page-title">{{ element.name }}</h1>
    % for parent in element.parents:
        <link  property="rdfs:subClassOf" href="{{ parent.getSchemaUrl() }}" />
    % end

    <h4>
    % for breadcrumb in breadcrumbs:
        <span class='breadcrumbs'>
        % for index, parent in enumerate(breadcrumb):
            % if index > 0:
                &nbsp;&gt;&nbsp;
            % end
            <a href="{{ parent.getUrl() }}">{{ parent.name }}</a>
        % end
        </span>
    % end
    </h4>

    <div property="rdfs:comment">{{! element.comment }}</div>

    % if element.extendsSchemaOrg:
        <br>
        <p>
            <em>
                This class has been extended from 
                <a href="{{ element.getSchemaUrl() }}">Schema.org</a>
            </em>
        </p>
    % end

    <table class="definition-table">
        <thead>
            <tr>
                <th>Property</th>
                <th>Expected Type</th>
                <th>Description</th>               
            </tr>
        </thead>

        <tbody class="supertype">
        % for inheritance in inheritances:
            % if not inheritance.properties:
                % continue
            % end
            <tr class="supertype">
                <th class="supertype-name" colspan="3">
                    Properties from <a href="{{ inheritance.getUrl() }}">{{ inheritance.name }}</a>
                </th>
            </tr>

            % for property in inheritance.properties:
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
                        {{! property.comment }}
                        % if property.inverseOf:
                            <br>
                            Inverse property: 
                            <a href="{{ property.inverseOf.getUrl() }}">
                                {{ property.inverseOf.name }}
                            </a>
                        % end
                    </td>
                </tr>   
            % end
        % end
        </tbody>
    </table>

    % if element.rangeOf:
        <br>
        <p>
            Instances of 
            <a href="{{ element.getUrl() }}">{{ element.name }}</a> 
            may appear as values for the following properties:
        </p>

        <table class="definition-table">
            <thead>
                <tr>
                    <th>Property</th>
                    <th>On Types</th>
                    <th>Description</th>               
                </tr>
            </thead>

            <tbody class="supertype">
            % for property in element.rangeOf:
                <tr typeof="rdfs:Property" resource="{{ property.getSchemaUrl() }}">
                    <th class="prop-nam" scope="row">
                        <code property="rdfs:label">
                            <a href="{{ property.getUrl() }}">{{ property.name }}</a>
                        </code>
                    </th>
                    <td class="prop-ect">
                    % for index, domain in enumerate(property.domains):
                        % if index > 0:
                            &nbsp;or<br>
                        % end
                        <a href="{{ domain.getUrl() }}">{{ domain.name }}</a>
                    % end
                    </td>
                    <td class="prop-desc" property="rdfs:comment">
                        {{! property.comment }}
                        % if property.inverseOf:
                            <br>
                            Inverse property: 
                            <a href="{{ property.inverseOf.getUrl() }}">
                                {{ property.inverseOf.name }}
                            </a>
                        % end
                    </td>
                </tr>   
            % end
            </tbody>
        </table>
    % end
</div>
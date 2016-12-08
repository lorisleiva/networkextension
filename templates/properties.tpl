%rebase templates/master

<h1>All properties</h1>

<div id="thing_tree">
    <h3>netcomp extension without core vocabulary</h3>
    <ul class="no-border">
    % for property in properties:
        <li id="{{ property.name }}">
            <a href="{{ property.getUrl() }}">
                {{ property.name }}
            </a>
        </li>
    % end
    </ul>
</div>
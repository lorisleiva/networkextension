def createComment(comment, identLevel = 0):
    return ('\t' * identLevel) + '<!-- ' + comment + ' -->'

def createTag(tag, attributes = [], content = None, identLevel = 0, opennedTag = False):
    tabs = "\t" * identLevel

    if attributes:
        attr = " ".join([k + '="' + v + '"' for k, v in attributes])
        attr = " " + attr
    else:
        attr = ""

    if content is None:
        return tabs + "<" + tag + attr + " />" 

    contentLines = content.split("\n")
    if len(contentLines) > 1:
        content = "\n".join(map(lambda l: tabs + "\t" + l, contentLines))
        opennedTag = True
    elif opennedTag:
        content = tabs + "\t" + content

    if opennedTag:
        s = tabs + "<" + tag + attr + ">\n" + content + "\n" + tabs + "</" + tag + ">" 
    else:
        s = tabs + "<" + tag + attr + ">" + content + "</" + tag + ">" 

    return s

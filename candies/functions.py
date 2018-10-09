from lxml import etree


def dict_to_xml(raw):
    s = ""
    for k, v in raw.items():
        s += "<{0}>{1}</{0}>".format(k, v)
    s = "<xml>{0}</xml>".format(s)
    return s.encode("utf-8")


def xml_to_dict(content):
    raw = {}
    root = etree.fromstring(content.encode("utf-8"),
                            parser=etree.XMLParser(resolve_entities=False))
    for child in root:
        raw[child.tag] = child.text
    return raw
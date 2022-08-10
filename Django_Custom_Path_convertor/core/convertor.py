
class YearConvertor(object):

    regex="\d{4}"

    def to_python(self,value):
        return int(value)

    def to_url(self,value):
        return f"{value:4d}"


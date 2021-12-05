import abc

class Article(metaclass=abc.ABCMeta):
        @property
        @abc.abstractmethod
        def section(self):
            pass

        @property
        @abc.abstractmethod
        def subsection(self):
            pass

        @property
        @abc.abstractmethod
        def title(self):
            pass

        @property
        @abc.abstractmethod
        def abstract(self):
            pass
        
        @property
        @abc.abstractmethod
        def byline(self):
            pass

        @property
        @abc.abstractmethod
        def url(self):
            pass

        @property
        @abc.abstractmethod
        def uri(self):
            pass

        @property
        @abc.abstractmethod
        def updated_date(self):
            pass

        @property
        @abc.abstractmethod
        def created_date(self):
            pass

        @property
        @abc.abstractmethod
        def published_date(self):
            pass

        @property
        @abc.abstractmethod
        def material_type_facet(self):
            pass

        @property
        @abc.abstractmethod
        def kicker(self):
            pass

        @property
        @abc.abstractmethod
        def des_facet(self):
            pass

        @property
        @abc.abstractmethod
        def org_facet(self):
            pass

        @property
        @abc.abstractmethod
        def per_facet(self):
            pass

        @property
        @abc.abstractmethod
        def geo_facet(self):
            pass

        @property
        @abc.abstractmethod
        def short_url(self):
            pass
            
class Image(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def url(self):
        pass

    @property
    @abc.abstractmethod
    def format(self):
        pass

    @property
    @abc.abstractmethod
    def caption(self):
        pass

    @property
    @abc.abstractmethod
    def copyright(self):
        pass

    @property
    @abc.abstractmethod
    def media_type(self):
        pass

    @property
    @abc.abstractmethod
    def width(self):
        pass

    @property
    @abc.abstractmethod
    def height(self):
        pass
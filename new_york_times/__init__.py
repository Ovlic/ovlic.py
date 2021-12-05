import requests, urllib
from .. import errors
from . import abc



class nyt:
    def __init__(self, key):
        self.key = key


    class response(object):
        def __init__(self, _dict):
            if isinstance(_dict, (nyt.nytattr, nyt.response)): _dict = _dict.__dict__
            else: _dict = {k[0].lower()+k[1:]: v for k, v in _dict.items()}
            for key in _dict:
                if key == "key" or key == "copyright": continue
                else: setattr(self, key, _dict[key])

        def __repr__(self):
            return f'<response status={self.status} num_results={self.num_results} results>'
            
        def json(self): return self.__dict__


    class nytattr(object):
        """convert :class:`dict` to :class:`class`"""
        def __init__(self, _dict:dict):
            if isinstance(_dict, nyt.nytattr): _dict = _dict.__dict__
            else: _dict = {k[0].lower()+k[1:]: v for k, v in _dict.items()}
            for key in _dict:
                if _dict[key] is not None: setattr(self, key, _dict[key])

        def json(self): return self.__dict__

    class image(abc.Image):
        def __init__(self, media:dict):
            media['media_type'] = media['type']
            del media['type']
            self.media = media

        def __repr__(self):
            return "<image media_type={0[media_type]!r} format={0[format]!r} height={0[height]!r} width={0[width]!r} caption={0[caption]!r} copyright={0[copyright]!r} url={0[url]!r}".format(self.media)

        @property
        def url(self):
            return self.media['url']

        @property
        def format(self):
            return self.media['format']

        @property
        def caption(self):
            return self.media['caption']

        @property
        def copyright(self):
            return self.media['copyright']

        @property
        def media_type(self):
            return self.media['type']

        @property
        def width(self):
            return self.media['width']

        @property
        def height(self):
            return self.media['height']

        def json(self): return self.__dict__


    class article(abc.Article):
        def __init__(self, _article:dict):
            _article = {k[0].lower()+k[1:]: v for k, v in _article.items()}
            self.article = _article
            self.media = nyt.article.media(self.article['media'])

        def __repr__(self) -> str:
            return super().__repr__()

        @property
        def section(self):
            return self.article['section']

        @property
        def subsection(self):
            return self.article['subsection']

        @property
        def title(self):
            return self.article['title']

        @property
        def abstract(self):
            return self.article['abstract']
        
        @property
        def byline(self):
            return self.article['byline']

        @property
        def url(self):
            return self.article['url']

        @property
        def uri(self):
            return self.article['uri']

        @property
        def updated_date(self):
            return self.article['updated_date']

        @property
        def created_date(self):
            return self.article['created_date']

        @property
        def published_date(self):
            return self.article['published_date']

        @property
        def material_type_facet(self):
            return self.article['material_type_facet']

        @property
        def kicker(self):
            return self.article['kicker']

        @property
        def des_facet(self):
            return self.article['des_facet']

        @property
        def org_facet(self):
            return self.article['org_facet']

        @property
        def per_facet(self):
            return self.article['per_facet']

        @property
        def geo_facet(self):
            return self.article['geo_facet']

        @property
        def short_url(self):
            return self.article['self_url']

        def json(self): return self.__dict__

        class media(object):
            def __init__(self, _media:list):
                fcheck = ["Normal", "superJumbo", "Standard Thumbnail", "mediumThreeByTwo210", "mediumThreeByTwo440"]
                fcorr = ["default", "large", "thumbnail_default", "small", "medium"]
                formats = []
                for i in range(0, len(_media)):
                    _format = _media[i]['format']
                    for j in fcheck:
                        if _format == j:
                            _format = fcorr[fcheck.index(j)]
                    _format = _format.replace(" ", "_")
                    formats.append(_format)
                for f in formats:
                    setattr(self, f, nyt.image(_media[formats.index(f)]))

            def __repr__(self):
                base_list = []
                for i in [a for a in self.__dict__ if not a.startswith('__')]:
                    base_list.append("{0}={1}".format(i, object.__repr__(getattr(self, i))))

                return '<media {}>'.format(' '.join(base_list))

            def json(self): return self.__dict__


    def get(self, url):
        res = requests.get(url).json()
        if "fault" in res:
            if res['fault']['faultstring'] == "Invalid ApiKey": raise errors.InvalidKey()
            raise errors.NYTError(res['fault']['faultstring'])

        for k in range(0, len(res['results'])):
            mediatype = "multimedia" if "multimedia" in res['results'][k] else "media-metadata" if "media-metadata" in res['results'][k] else None
            print(mediatype, end="\n")
            if not mediatype: continue
            res['results'][k]['media'] = res['results'][k].pop(mediatype)
            res['results'][k] = nyt.article(res['results'][k])

        return nyt.response(res)

    
    def topstories(self, section="home"):
        """Default Section: "home". Sections: ["arts", "automobiles", "books", "business", "fashion", "food", "health", "home", "insider", "magazine", "movies", "nyregion", "obituaries", "opinion", "politics", "realestate", "science", "sports", "sundayreview", "technology", "theater", "t-magazine", "travel", "upshot", "us", "world"]"""
        sections = ["arts", "automobiles", "books", "business", "fashion", "food", "health", "home", "insider", "magazine", "movies", "nyregion", "obituaries", "opinion", "politics", "realestate", "science", "sports", "sundayreview", "technology", "theater", "t-magazine", "travel", "upshot", "us", "world"]
        if section not in sections: raise ValueError("Invalid section.")
        url = f"https://api.nytimes.com/svc/topstories/v2/home.json?api-key={self.key}"
        res = nyt.get(self, url=url)
        return res


    def mostpopular(self, days:int=1):
        """days must be either 1, 7, or 30."""
        if days not in [1, 7, 30]: raise ValueError("Invalid Day.")
        res = nyt.get(self, url=f"https://api.nytimes.com/svc/mostpopular/v2/viewed/7.json?api-key={self.key}")
        return res


    def newswire(self, section:str="home page", source:str="all", limit:int=1):
        sections = ['admin', 'arts', 'automobiles', 'books', 'briefing', 'business', 'climate', 'corrections', 'crosswords & games', 'education', 'en español', 'fashion', 'food', 'guides', 'health', 'home & garden', 'home page', 'job market', 'lens', 'magazine', 'movies', 'multimedia/photos', 'new york', 'obituaries', 'opinion', 'parenting', 'podcasts', 'reader center', 'real estate', 'science', 'smarter living', 'sports', 'style', 'sunday review', 't brand', 't magazine', 'technology', 'the learning network', 'the upshot', 'the weekly', 'theater', 'times insider', 'today’s paper', 'travel', 'u.s.', 
'universal', 'video', 'well', 'world', 'your money']
        source = source.lower()
        section = section.lower()
        if source not in ["all", "nyt", "inyt"]: raise ValueError("source must be 'all', 'nyt', or 'inyt'")
        if section not in sections: raise ValueError("Invalid section.")
        res = nyt.get(self, url=f"https://api.nytimes.com/svc/news/v3/content/{source}/{urllib.parse.quote(str(section))}.json?limit={limit}&api-key={self.key}")
        return res
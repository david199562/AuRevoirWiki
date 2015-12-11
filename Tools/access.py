# "The hardest thing is to go to sleep at night, when there are so many urgent
#  things needing to be done. A huge gap exists between what we know is possible
#  with today's machines and what we have so far been able to finish."
#  - Donald Knuth


class UserAccess:
    """Get Create Edit Delete"""
    def __init__(self, pat: str):
        self.__pat = pat

    def get(self, cache_id: str):
        pass

    def edit(self, cache_id: str, new_content: str):
        pass

    def create(self):
        pass

    def delete(self, cache_id: str):
        pass

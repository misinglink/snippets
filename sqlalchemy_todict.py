class DictMixIn:
    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            if not isinstance(getattr(self, column.name), 
datetime.datetime)
            else getattr(self, column.name).isoformat()
            for column in self.__table__.columns
        }
